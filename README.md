# Terminal Wordle with Recommendation Engine

This is the first app I thought of to test the coding and reasoning capabilities of the new ChatGPT o3 model. One-shotted in 1 minute 55 seconds with no bugs using the prompt in o3-prompt.md.

## Quick Start
Clone the repository, run `pip install requirements.txt` and then `python3 main.py`. The only dependency is colorama, which gives text color in the terminal.

## Recommendation Engine
After each turn, the the user is given an opportunity to see the top 10 recommendations for the next guess. These are the valid (using already-guessed green and yellow letters) guesses that shrink the space of possible answers the most.

## Acknowledgements
The word list used is the original Wordle solution list (2315 words). When NYT bought the game they changed the word list slightly.

