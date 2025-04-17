import random
from wordlist import WORD_BANK, ALLOWED_WORDS
try:
    from colorama import Back, Fore, Style, init
    init(autoreset=True)
    GREEN = Back.GREEN + Fore.BLACK
    YELLOW = Back.YELLOW + Fore.BLACK
    GRAY = Back.WHITE + Fore.BLACK
    RESET = Style.RESET_ALL
except ImportError:
    GREEN = YELLOW = GRAY = RESET = ''

def pattern_for(guess: str, target: str) -> str:
    """Return a 5‑char pattern ('2' green, '1' yellow, '0' gray)."""
    result = ['0'] * 5
    target_remaining = list(target)
    # greens
    for i, (g, t) in enumerate(zip(guess, target)):
        if g == t:
            result[i] = '2'
            target_remaining[i] = None
    # yellows
    for i, g in enumerate(guess):
        if result[i] != '0':
            continue
        if g in target_remaining:
            result[i] = '1'
            target_remaining[target_remaining.index(g)] = None
    return ''.join(result)

def colorize(guess: str, pattern: str) -> str:
    out = []
    for ch, p in zip(guess.upper(), pattern):
        if p == '2':
            out.append(f"{GREEN}{ch}{RESET}")
        elif p == '1':
            out.append(f"{YELLOW}{ch}{RESET}")
        else:
            out.append(f"{GRAY}{ch}{RESET}")
    return ''.join(out)

class WordleGame:
    MAX_GUESSES = 6

    def __init__(self):
        self.reset()

    def reset(self):
        self.target = random.choice(WORD_BANK)
        self.remaining = WORD_BANK.copy()

    def play(self):
        from recommender import Recommender  # local import avoids circularity
        remaining = self.remaining
        for attempt in range(1, self.MAX_GUESSES + 1):
            guess = self._prompt_guess(attempt)
            pattern = pattern_for(guess, self.target)
            print(colorize(guess, pattern))
            if guess == self.target:
                print(f"\n🎉 Correct! You solved it in {attempt} guess{'es' if attempt > 1 else ''}.\n")
                return
            # narrow search space
            remaining = [w for w in remaining if pattern_for(guess, w) == pattern]
            # offer recommendation
            if self._yes_no("Would you like a recommendation for your next guess? (y/n): "):
                rec = Recommender().recommend(remaining)
                print("Top suggestions:", ', '.join(rec), "\n")
        print(f"😞 Out of guesses! The word was {self.target.upper()}.\n")

    def _prompt_guess(self, attempt: int) -> str:
        while True:
            guess = input(f"Guess {attempt}/{self.MAX_GUESSES}: ").strip().lower()
            if len(guess) != 5 or not guess.isalpha():
                print("Enter a valid 5‑letter word.")
            elif guess not in ALLOWED_WORDS:
                print("Word not in list; try another.")
            else:
                return guess

    def _yes_no(self, prompt: str) -> bool:
        return input(prompt).strip().lower().startswith('y')
