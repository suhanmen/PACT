Here is the Python function to find the first adverb and their positions in a given sentence:

```python
import re

def find_adverb_position(sentence):
    # Regular expression pattern to match adverbs
    pattern = r'\b\w+ly\b'
    match = re.search(pattern, sentence)
    if match:
        start = match.start()
        end = match.end()
        adverb = match.group()
        return (start, end, adverb)
    else:
        return None

# Test the function
print(find_adverb_position("clearly!! we can see the sky"))
```

This function uses a regular expression to find the first adverb in the sentence. The regular expression pattern `\b\w+ly\b` matches any word ending with 'ly'. The `re.search()` function is used to find the first match in the sentence. If a match is found, the function returns a tuple containing the start and end positions of the match and the matched adverb. If no match is found, the function returns `None`.
