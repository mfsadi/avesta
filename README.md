# Avesta

Tools for text and language processing

This is a library for text and language (pre) processing.

**Similarity**

**Lexical Similarity**
Sample usage:

```Python
from tools.similarity.lexical_sim import lexical_synonym_checker

res = lexical_synonym_checker("پیراهن مردانه سایز 12 قرمز", "پیراهن قرمز       مردانه سایز ۱۲")
print(res)
```

**Character based Similarity**

```Python

# Character based similarity gives the distance between two strings. 

from tools.similarity.cbs import similarity

sim = similarity()
status = sim.char_based_similarity("avesta", "a vesta", threshold=1)
print(status)
# True
````
