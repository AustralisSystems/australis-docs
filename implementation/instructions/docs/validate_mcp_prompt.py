#!/usr/bin/env python3
"""Validate runner prompt YAML files against runner-prompt-schema.json."""
import argparse
import json
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator, ValidationError

SCHEMA_PATH = Path(__file__).resolve().parent / "runner-prompt-schema.json"


def load_schema(path: Path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_yaml(path: Path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def validate_file(schema, path: Path):
    data = load_yaml(path)
    validator = Draft202012Validator(schema)
    errors = list(validator.iter_errors(data))
    if errors:
        for err in errors:
            print(f"Validation error in {path}: {err.message}")
        return False

    # Warning-level checks for raw* fields (similar to instruction validator)
    raw_present = any(k in data for k in ("raw", "raw_ref", "raw_hash"))
    if not raw_present:
        print(f"WARNING: {path} does not include 'raw', 'raw_ref', or 'raw_hash' — consider adding a raw_ref for traceability.")

    raw_ref = data.get("raw_ref")
    if raw_ref:
        try:
            from urllib.parse import urlparse

            parsed = urlparse(raw_ref)
            if not parsed.scheme:
                print(f"WARNING: {path} has 'raw_ref' but it does not appear to be a valid URI: {raw_ref}")
        except Exception as ex:
            print(f"WARNING: error parsing raw_ref for {path}: {ex}")

    raw_hash = data.get("raw_hash")
    if raw_hash:
        import re

        if not re.fullmatch(r"[A-Fa-f0-9]{64}", raw_hash):
            print(f"WARNING: {path} has 'raw_hash' that does not look like a SHA-256 hex: {raw_hash}")

    raw = data.get("raw")
    if raw and any(tok in raw.upper() for tok in ("SECRET", "PRIVATE_KEY", "PASSWORD", "AWS_SECRET", "API_KEY")):
        print(f"WARNING: {path} 'raw' appears to contain secret-like tokens; ensure content is sanitized or use 'raw_ref' instead.")

    return True


def main():
    p = argparse.ArgumentParser(description="Validate MCP runner prompt YAML files.")
    p.add_argument("paths", nargs="+", help="Files or directories to validate")
    args = p.parse_args()

    schema = load_schema(SCHEMA_PATH)
    paths = [Path(pp) for pp in args.paths]

    ok = True
    for pp in paths:
        if pp.is_dir():
            for f in sorted(pp.glob("*.yaml")):
                if not validate_file(schema, f):
                    ok = False
        else:
            if not validate_file(schema, pp):
                ok = False

    if not ok:
        sys.exit(2)


if __name__ == "__main__":
    main()
