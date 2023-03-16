## gptwc: wc for GPT tokens

A simple utility for counting tokens. Uses `tiktoken`

Example Usage:

```
cat logs.txt | gptwc

gptwc < input.txt
```

Prints the number of tokens in the input stdin text, similar to how `wc` prints the number of words.
