# Avesta

Tools for text and language processing

This is a library for text and language (pre) processing.

**Installation**

````Bash
pip install avesta
````

**Usage**

**Similarity**

**Lexical Similarity**

```Python
from avesta.tools.similarity.lexical_sim import lexical_synonym_checker

status = lexical_synonym_checker("پیراهن مردانه سایز 12 قرمز", "پیراهن قرمز       مردانه سایز ۱۲")
print(status)
# Yes (they are lexically synonyms.)
```

**Semantic Similarity**

```Python
from avesta.tools.similarity.semantic_sim import semantic_synonym_checker

status = semantic_synonym_checker("پیراهن مردانه مشکی", "پیراهن سیاه مردانه")
print(status)
# Yes (they are semantically synonyms.)
```

**Character based Similarity**

```Python

# Character based similarity gives the distance between two strings. 

from avesta.tools.similarity.cbs import similarity

sim = similarity()
status = sim.char_based_similarity("avesta", "a vesta", threshold=1)
print(status)
# True (The distance is less than or equal to threshold.)
````

**Handle whitespace mistakes as part of spell checking**

```Python

# Character based similarity gives the distance between two strings. 

from avesta.tools.spell_checker.whitespace_handler import correct_spacing

print(correct_spacing("مانتوزنانه"))
# 'مانتو زنانه'
````