#!/usr/bin/env python3
import sys
import argparse
import tiktoken
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description="Count tokens in text files using OpenAI's tiktoken library.")
    parser.add_argument("files", metavar="FILE", nargs="*", type=Path, help="Text files to count tokens in")
    parser.add_argument("--files0-from", metavar="F", type=Path, help="Read input from the files specified by NUL-terminated names in file F")
    parser.add_argument("--model", default="text-davinci-003", metavar="MODEL", help="Model name to use for tokenization (default: text-davinci-003)")
    parser.add_argument("-c", "--clipboard", action="store_true", help="Read input from the system clipboard")
    parser.add_argument("--version", action="version", version="%(prog)s 1.2.1")

    args = parser.parse_args()

    enc = tiktoken.encoding_for_model(args.model)

    if args.files0_from:
        with args.files0_from.open("r", encoding="utf-8") as file_list:
            args.files.extend(Path(line.strip()) for line in file_list)

    if args.clipboard:
        import pyperclip
        input_text = pyperclip.paste()
        print(len(enc.encode(input_text)))
    elif not args.files:
        input_text = sys.stdin.read()
        print(len(enc.encode(input_text)))
    else:
        for file_path in args.files:
            with file_path.open("r", encoding="utf-8") as input_file:
                input_text = input_file.read()
                print(f"{file_path}: {len(enc.encode(input_text))}")

if __name__ == "__main__":
    main()

