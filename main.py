from game import WordleGame

def main():
    print("""============================
Terminal Wordle (with hints)
============================

Rules:
 • Guess the 5‑letter word in 6 tries.
 • After each guess the letters show:
     green  — correct letter, correct spot
     yellow — present elsewhere
     gray   — absent
""")
    game = WordleGame()
    while True:
        game.play()
        if not input("Play again? (y/n): ").strip().lower().startswith('y'):
            print("Thanks for playing!")
            break
        game.reset()

if __name__ == '__main__':
    main()
