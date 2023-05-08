import argparse

import romdb.create
import romdb.ingest


def main() -> None:
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest="command", required=True)
    subparser.add_parser("ingest")
    create_subparser = subparser.add_parser("create")
    create_subparser.add_argument("--schema-only", action="store_true")
    args = parser.parse_args()
    if args.command == "ingest":
        romdb.ingest.ingest()
    else:
        romdb.create.create(args.schema_only)


if __name__ == "__main__":
    main()
