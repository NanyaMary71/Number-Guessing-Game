https://roadmap.sh/projects/number-guessing-game
Number Guessing Game (Python)

A simple and fun command-line Number Guessing Game built in Python.
The game includes difficulty levels, helpful hints, and a high-score tracking system that records your best performance for each level.

✨ Features
🔢 1. Difficulty Levels

Choose from three difficulty levels, each with different chances:

Easy – 10 attempts

Medium – 5 attempts

Hard – 3 attempts

🏆 2. High Score Tracker

The game automatically tracks your best performance for each difficulty based on:

Fewest number of attempts, and

Fastest completion time

At the start of each round, the game displays your best high score (if any) for that difficulty.

💡 3. Smart Hint System

After each guess, you receive hints based on:

How close your guess is (Hot, Warm, Cold)

Whether the secret number is odd or even

This helps guide you toward the correct answer.

⏱️ 4. Time Tracking

The game measures how long it takes you to guess the correct number and uses this to update high scores.

🔁 5. Play Again Loop

After each game round, you can choose to:

Play again, or

Quit and see all final high scores

📂 How to Run the Game

Make sure you have Python 3 installed.

Save the script as:

number_game.py


Run the game:

python number_game.py

🧠 How the Game Works

A random number between 1 and 100 is generated.

You select a difficulty level.

You guess the number, and the game gives you:

“Too high” / “Too low”

Hint about closeness (Hot, Warm, Cold)

Whether the number is odd or even

You win if you guess correctly within the allowed attempts.

High scores update automatically when you achieve a new record.

📊 High Score Rules

A new high score is recorded if:

You use fewer attempts than your previous record
OR

You use the same number of attempts but finish in less time

High scores are stored in memory while the program is running.

🖼️ Sample Output
=== NUMBER GUESSING GAME ===

Choose difficulty:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)

High Score for Easy: 3 attempt(s) in 12.55 seconds!
You have 10 chances. Good luck!

📌 Requirements

Python 3.x

No external libraries needed (only random and time)

📜 License

This project is free to use, modify, and learn from.
