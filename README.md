## gptwc: wc for GPT tokens

The `wc` utility counts words or characters. The `gptwc` utility functions similarly but counts tokens.
Tokens are smaller than words but larger than characters, and are a more compact representation of text used by large language models.

Use `gptwc` to check the number of tokens in a string, in order to remain under the token limit (eg. 4097) for your large language model API. Uses `tiktoken`.


## Installation
```
$ pip install gptwc

$ echo "Simple is better than complex." | gptwc
7
```

## Example Usage

```
$ cat LICENSE  | gptwc
257
$ cat LICENSE | wc -c
1059
$ cat LICENSE | wc -w
165


$ curl -s 'https://gist.githubusercontent.com/phillipj/4944029/raw/75ba2243dd5ec2875f629bf5d79f6c1e4b5a8b46/alice_in_wonderland.txt' | wc -w
26470

curl -s 'https://gist.githubusercontent.com/phillipj/4944029/raw/75ba2243dd5ec2875f629bf5d79f6c1e4b5a8b46/alice_in_wonderland.txt' | gptwc
40085


$ cat LICENSE | gptwc --model text-davinci-003
257
$ cat LICENSE | gptwc --model gpt-3.5-turbo
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
  --model MODEL    Model name to use for tokenization (default: gpt-4)
  -c, --clipboard  Read input from the system clipboard
  --version        show program's version number and exit
```

## Which Tokenizer Does Each Model Use?

From [tiktoken/model.py](https://github.com/openai/tiktoken/blob/main/tiktoken/model.py)

```
"gpt-4o": "o200k_base",
"gpt-4": "cl100k_base",
"gpt-3.5-turbo": "cl100k_base",
"text-embedding-ada-002": "cl100k_base",

"text-davinci-003": "p50k_base",
"text-davinci-002": "p50k_base",
"code-davinci-002": "p50k_base",
"code-davinci-001": "p50k_base",
"code-cushman-002": "p50k_base",
"code-cushman-001": "p50k_base",
"davinci-codex": "p50k_base",
"cushman-codex": "p50k_base",

"text-davinci-001": "r50k_base",
"text-curie-001": "r50k_base",
"text-babbage-001": "r50k_base",
"text-ada-001": "r50k_base",
"davinci": "r50k_base",
"curie": "r50k_base",
"babbage": "r50k_base",
"ada": "r50k_base",
"text-similarity-davinci-001": "r50k_base",
"text-similarity-curie-001": "r50k_base",
"text-similarity-babbage-001": "r50k_base",
"text-similarity-ada-001": "r50k_base",
"text-search-davinci-doc-001": "r50k_base",
"text-search-curie-doc-001": "r50k_base",
"text-search-babbage-doc-001": "r50k_base",
"text-search-ada-doc-001": "r50k_base",
"code-search-babbage-code-001": "r50k_base",
"code-search-ada-code-001": "r50k_base",

"text-davinci-edit-001": "p50k_edit",
"code-davinci-edit-001": "p50k_edit",

"gpt2": "gpt2",
```
