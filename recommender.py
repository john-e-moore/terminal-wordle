from collections import defaultdict

def pattern_for(guess: str, target: str) -> str:
    result = ['0'] * 5
    target_remaining = list(target)
    for i, (g, t) in enumerate(zip(guess, target)):
        if g == t:
            result[i] = '2'
            target_remaining[i] = None
    for i, g in enumerate(guess):
        if result[i] != '0':
            continue
        if g in target_remaining:
            result[i] = '1'
            target_remaining[target_remaining.index(g)] = None
    return ''.join(result)

class Recommender:
    """Ranks candidate words by expected reduction of the search space."""
    def recommend(self, remaining_words, top_k: int = 10):
        if len(remaining_words) <= top_k:
            return remaining_words
        scores = []
        for candidate in remaining_words:
            buckets = defaultdict(int)
            for target in remaining_words:
                buckets[pattern_for(candidate, target)] += 1
            expected = sum(size * size for size in buckets.values()) / len(remaining_words)
            scores.append((expected, candidate))
        scores.sort()
        return [w for _, w in scores[:top_k]]
