#!/usr/bin/env python3
"""Validator for doctrine/protocol/instruction/runner prompt YAMLs.

This script discovers YAML files and validates them by their `schema` field,
using the corresponding JSON Schema files in this directory.
"""
import argparse
import json
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

SCHEMA_MAP = {
    "mcp.doctrine/v1": "doctrine-schema.json",
    "mcp.protocol/v1": "protocol-schema.json",
    "mcp.instruction/v1": "instruction-schema.json",
    "mcp.prompt/v1": "runner-prompt-schema.json",
}

HERE = Path(__file__).resolve().parent


def load_schema(name: str):
    path = HERE / name
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def load_yaml(path: Path):
    with open(path, "r", encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def find_yaml_files(root: Path):
    for p in sorted(root.rglob("*.yaml")):
        yield p


def validate_one(path: Path):
    data = load_yaml(path)
    if not data or "schema" not in data:
        print(f"Skipping {path}: missing 'schema' field")
        return True
    schema_key = data["schema"]
    schema_file = SCHEMA_MAP.get(schema_key)
    if not schema_file:
        print(f"No schema mapping for {schema_key} (file: {path}). Skipping.")
        return False
    schema = load_schema(schema_file)
    validator = Draft202012Validator(schema)
    errors = list(validator.iter_errors(data))
    if errors:
        print(f"Validation errors for {path} against {schema_key}:")
        for e in errors:
            print(f" - {e.message} (at {'/'.join(map(str,e.absolute_path))})")
        return False

    # Warning-level checks for raw* fields
    raw_present = any(k in data for k in ("raw", "raw_ref", "raw_hash"))
    if not raw_present:
        print(f"WARNING: {path} does not include 'raw', 'raw_ref', or 'raw_hash' — consider adding a raw_ref for traceability.")

    # Validate raw_ref if present
    raw_ref = data.get("raw_ref")
    if raw_ref:
        try:
            from urllib.parse import urlparse

            parsed = urlparse(raw_ref)
            if not parsed.scheme:
                print(f"WARNING: {path} has 'raw_ref' but it does not appear to be a valid URI: {raw_ref}")
        except Exception as ex:
            print(f"WARNING: error parsing raw_ref for {path}: {ex}")

    # Validate raw_hash if present
    raw_hash = data.get("raw_hash")
    if raw_hash:
        import re

        if not re.fullmatch(r"[A-Fa-f0-9]{64}", raw_hash):
            print(f"WARNING: {path} has 'raw_hash' that does not look like a SHA-256 hex: {raw_hash}")

    # Scan embedded raw for obvious secret markers (warning only)
    raw = data.get("raw")
    if raw and any(tok in raw.upper() for tok in ("SECRET", "PRIVATE_KEY", "PASSWORD", "AWS_SECRET", "API_KEY")):
        print(f"WARNING: {path} 'raw' appears to contain secret-like tokens; ensure content is sanitized or use 'raw_ref' instead.")

    return True


def main():
    p = argparse.ArgumentParser(description="Validate instruction schemas under a directory.")
    p.add_argument("root", nargs="?", default="docs/implementation/instructions/v2", help="Root dir to search for YAML files")
    args = p.parse_args()

    root = Path(args.root).resolve()
    ok = True
    for f in find_yaml_files(root):
        r = validate_one(f)
        if not r:
            ok = False
    if not ok:
        sys.exit(2)


if __name__ == "__main__":
    main()
