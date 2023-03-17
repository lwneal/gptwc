## gptwc: wc for GPT tokens

A simple utility for counting tokens.
It's like `wc` which counts words, except it uses `tiktoken` to count tokens.

It's useful for checking the number of tokens in a string, in order to remain under the token limit (eg. 4097 for the GPT3 API)

```
usage: gptwc [-h] [--files0-from F] [--model MODEL] [-c] [--version] [FILE ...]

Count tokens in text files using OpenAI's tiktoken library.

positional arguments:
  FILE             Text files to count tokens in

options:
  -h, --help       show this help message and exit
  --files0-from F  Read input from the files specified by NUL-terminated names in file F
  --model MODEL    Model name to use for tokenization (default: text-davinci-003)
  -c, --clipboard  Read input from the system clipboard
  --version        show program's version number and exit
```

Example Usage:

```
$ cat README.md  | wc -w
54

$ cat README.md  | gptwc
180


$ curl -s 'https://gist.githubusercontent.com/phillipj/4944029/raw/75ba2243dd5ec2875f629bf5d79f6c1e4b5a8b46/alice_in_wonderland.txt' | wc -w
26470

curl -s 'https://gist.githubusercontent.com/phillipj/4944029/raw/75ba2243dd5ec2875f629bf5d79f6c1e4b5a8b46/alice_in_wonderland.txt' | gptwc
40085


$ cat README.md | gptwc --model text-davinci-003
517
$ cat README.md | gptwc --model gpt-3.5-turbo
434


$ cat README.md | pbcopy
$ gptwc -c
517
```


