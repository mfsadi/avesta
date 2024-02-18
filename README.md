# Avesta
tools for text and language processing


This is a library for text and language (pre) processing.

```Python
Similarity

# Character based similarity distance between two strings. 

from tools.similarity.cbs import similarity

sim = similarity()

distance = sim.char_based_similarity("avesta", "a vesta", threshold=1)

print(distance)

````
