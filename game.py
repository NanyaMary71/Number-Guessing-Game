import random
import time

high_scores = {
    "Easy": {"attempts": None, "time": None},
    "Medium": {"attempts": None, "time": None},
    "Hard": {"attempts": None, "time": None}
}

def display_welcome():
    print("\n=== NUMBER GUESSING GAME ===\n")
    print("I'm thinking of a number between 1 and 100.\n")

def select_difficulty():
    print("Choose difficulty:")
    print("1. Easy   (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard   (3 chances)")
    while True:
        c = input("\nEnter 1, 2, or 3: ").strip()
        if c == "1": return 10, "Easy"
        if c == "2": return 5, "Medium"
        if c == "3": return 3, "Hard"
        print("Invalid choice!")

def give_hint(guess, secret):
    diff = abs(guess - secret)
    parity = "even" if secret % 2 == 0 else "odd"
    if diff <= 5:   return f"Very hot! It's {parity}."
    if diff <= 15:  return f"Hot! It's {parity}."
    if diff <= 30:  return f"Warm. It's {parity}."
    return f"Cold. It's {parity}."

def play_game():
    display_welcome()
    chances, level = select_difficulty()

    # THIS IS THE FIX — safe high score display
    score = high_scores[level]
    if score["attempts"] is not None:
        print(f"High Score for {level}: {score['attempts']} attempt(s) "
              f"in {score['time']:.2f} seconds!\n")
    else:
        print(f"No high score for {level} yet — can you set the record?\n")

    print(f"You have {chances} chances. Good luck!\n")

    secret = random.randint(1, 100)
    attempts = 0
    start = time.time()

    while attempts < chances:
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("Numbers only!\n")
            continue

        attempts += 1

        if guess == secret:
            duration = time.time() - start
            print(f"\nCORRECT! You win in {attempts} attempt(s)!")
            print(f"Time: {duration:.2f} seconds\n")

            # Update high score
            old = high_scores[level]
            if (old["attempts"] is None or 
                attempts < old["attempts"] or 
                (attempts == old["attempts"] and duration < old["time"])):
                high_scores[level] = {"attempts": attempts, "time": duration}
                print(f"NEW HIGH SCORE FOR {level.upper()}!!!\n")
            return

        print("Too high!" if guess > secret else "Too low!")
        print(give_hint(guess, secret))
        print(f"→ {chances - attempts} chance(s) left\n")

    print(f"Game over! The number was {secret}.\n")

# Main loop
while True:
    play_game()
    if input("Play again? (y/n): ").strip().lower() not in ["y", "yes"]:
        print("\nFinal High Scores:")
        for level, data in high_scores.items():
            if data["attempts"]:
                print(f"  {level}: {data['attempts']} attempts ({data['time']:.2f}s)")
            else:
                print(f"  {level}: No record yet")
        print("\nThanks for playing!")
        break

