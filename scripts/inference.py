"""Compatibility wrapper for legacy script entrypoint."""

from infer import main


if __name__ == "__main__":
    raise SystemExit(main())
