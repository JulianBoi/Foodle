from typing import List, Tuple
def word_frequencies(sentence: str, n: int) -> List[Tuple[str, int]]:
    freq = {}
    for word in sentence.split():
        freq[word] = freq.get(word, 0) + 1

    sorted_words = sorted(freq.items(), key=lambda x: (-x[1], x[0]))

    return sorted_words[:n]