#!/usr/bin/env python3
import sys
import tiktoken

def main():
    enc = tiktoken.encoding_for_model("text-davinci-003")

    input_text = sys.stdin.read()
    print(len(enc.encode(input_text)))

if __name__ == "__main__":
    main()

