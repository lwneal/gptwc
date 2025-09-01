## gptwc: wc for GPT tokens

The `wc` utility counts words or characters. The `gptwc` utility functions similarly but counts tokens.
Tokens are smaller than words but larger than characters, and are a more compact representation of text used by large language models.

Use `gptwc` to check the number of tokens in a string, in order to remain under the token limit for your large language model API. Uses [`tiktoken`](https://github.com/openai/tiktoken).


## Installation
```
$ pip install gptwc

$ echo "Simple is better than complex." | gptwc
6
```

## Example Usage

```
$ cat LICENSE | gptwc
200
$ cat LICENSE | wc -c
1059
$ cat LICENSE | wc -w
165


$ curl -s 'https://gist.githubusercontent.com/phillipj/4944029/raw/75ba2243dd5ec2875f629bf5d79f6c1e4b5a8b46/alice_in_wonderland.txt' | wc -w
26470

curl -s 'https://gist.githubusercontent.com/phillipj/4944029/raw/75ba2243dd5ec2875f629bf5d79f6c1e4b5a8b46/alice_in_wonderland.txt' | gptwc
38071


$ cat LICENSE | gptwc --model o200k_base
200
$ cat LICENSE | gptwc --model cl100k_base
201


$ cat README.md | pbcopy
$ gptwc -c
517
```

## Options

```
usage: gptwc [-h] [--files0-from F] [--model MODEL] [-c] [--version] [FILE ...]

Count tokens in text files using OpenAI's tiktoken library.

positional arguments:
  FILE             Text files to count tokens in

options:
  -h, --help       show this help message and exit
  --files0-from F  Read input from the files specified by NUL-terminated names in file F
  --model MODEL    Encoding or model to use for tokenization (default: o200k_base, used by GPT-5 and GPT-4o)
  -c, --clipboard  Read input from the system clipboard
  --version        show program's version number and exit
```

## Which Tokenizer Does Each Model Use?

See [tiktoken/model.py](https://github.com/openai/tiktoken/blob/main/tiktoken/model.py) for an up-to-date list.
