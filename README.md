## gptwc: wc for GPT tokens

A simple utility for counting tokens.
It's like `wc` which counts words, except it uses `tiktoken` to count tokens.

It's useful for checking the number of tokens in a string, in order to remain under the token limit (eg. 4097 for the GPT3 API)

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
```

