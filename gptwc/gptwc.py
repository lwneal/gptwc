#!/usr/bin/env python3
import sys
import argparse
import tiktoken
from pathlib import Path


def get_encoding(model_or_encoding):
    try:
        return tiktoken.get_encoding(model_or_encoding)
    except ValueError:
        return tiktoken.encoding_for_model(model_or_encoding)

def token_count(text, encoding):
    return len(encoding.encode(text))


def main():
    parser = argparse.ArgumentParser(description="Count tokens in text files using OpenAI's tiktoken library.")
    parser.add_argument("files", metavar="FILE", nargs="*", type=Path, help="Text files to count tokens in")
    parser.add_argument("--files0-from", metavar="F", type=Path, help="Read input from the files specified by NUL-terminated names in file F")
    parser.add_argument("--model", default="o200k_base", metavar="MODEL", help="Encoding or model to use for tokenization (default: o200k_base, used by GPT-4o. Use cl100k_base for GPT-3.5 and GPT-4)")
    parser.add_argument("-c", "--clipboard", action="store_true", help="Read input from the system clipboard")
    parser.add_argument("--version", action="version", version="%(prog)s 1.2.6")
    args = parser.parse_args()

    if args.files0_from:
        with args.files0_from.open("r", encoding="utf-8") as file_list:
            args.files.extend(Path(line.strip()) for line in file_list)

    encoding = get_encoding(args.model)

    if args.clipboard:
        import pyperclip
        input_text = pyperclip.paste()
        print(token_count(input_text, encoding))
    elif not args.files:
        input_text = sys.stdin.read()
        print(token_count(input_text, encoding))
    else:
        total = 0
        did_error = False
        for file_path in args.files:
            input_text = ""
            try:
                with file_path.open("r", encoding="utf-8") as input_file:
                    input_text = input_file.read()
            except (OSError, UnicodeDecodeError) as e:
                print(f"gptwc: {file_path}: {e}", file=sys.stderr)
                did_error = True
            count = token_count(input_text, encoding)
            total += count
            print(f"{count} {file_path}")
        if len(args.files) > 1:
            print(f"{total} total")
        sys.exit(1 if did_error else 0)

if __name__ == "__main__":
    main()

