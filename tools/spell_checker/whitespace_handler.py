import pickle
from collections import Counter
from multiprocessing import Pool
from nltk import word_tokenize
from nltk import bigrams
from tqdm import tqdm
from pathlib import Path

current_path = Path(__file__).resolve()
project_root = current_path.parent.parent.parent

with open(f'{project_root}/resources/ngrams/word_freqs.pkl', 'rb') as words_freq:
    words_freq = pickle.load(words_freq)
with open(f'{project_root}/resources/ngrams/bigram_freqs.pkl', 'rb') as bigram_freq:
    bigram_freq = pickle.load(bigram_freq)


def generate_ngrams():
    def process_sentence(sentence):
        tokens = word_tokenize(sentence)
        return tokens

    sentences = []
    with Pool(40) as pool:
        tokenized_sentences = pool.map(process_sentence, sentences)
    words_freq = Counter()
    for tokens in tqdm(tokenized_sentences):
        words_freq.update(tokens)
    print(f"Number of unique words: {len(words_freq)}")
    with open('{project_root}/resources/ngrams/word_freqs.pkl', 'wb') as f:
        pickle.dump(words_freq, f)
    bigram_counts = Counter()
    for tokens in tokenized_sentences:
        bigram_counts.update(bigrams(tokens))

    print(f"Number of unique bigrams: {len(bigram_counts)}")
    with open('{project_root}/resources/ngrams/bigram_freqs.pkl', 'wb') as f:
        pickle.dump(bigram_counts, f)


def correct_spacing(text):
    try:
        corrected_text = []
        for phrase in text.split():
            whole_freq = words_freq.get(phrase, 0)
            best_freq = whole_freq
            best_split = phrase
            for i in range(1, len(phrase)):
                part1, part2 = phrase[:i], phrase[i:]
                if part1 in words_freq and part2 in words_freq:
                    split_freq1 = words_freq[part1]
                    split_freq2 = words_freq[part2]
                    bigram_prob = bigram_freq.get((part1, part2), 0)
                    if bigram_prob > (split_freq1 + split_freq2):
                        best_freq = bigram_prob
                        best_split = f"{part1} {part2}"
                    else:
                        max_split_freq = max(split_freq1, split_freq2)
                        if max_split_freq > best_freq:
                            best_freq = max_split_freq
                            best_split = f"{part1} {part2}"
            whole_word_bias_threshold = 0.1 * best_freq
            if whole_freq >= whole_word_bias_threshold:
                corrected_text.append(phrase)
            else:
                corrected_text.append(best_split)
        return ' '.join(corrected_text)
    except Exception as e:
        print(e)
        return None

