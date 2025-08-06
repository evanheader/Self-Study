import random
import requests

def fetch_word(length):
    response = requests.get(f"https://random-word-api.herokuapp.com/word?length={length}")
    if response.status_code == 200:
        return response.json()[0]
    else:
        return ["python", "hangman", "challenge"]

def get_user_difficulty():
    difficulty = input("What difficulty whould you like to play on? (easy, medium or hard): ")
    while difficulty.lower() not in ["easy", "medium", "hard"]:
        difficulty = input("Invalid choice. Please enter 'easy', 'medium', or 'hard': ")
    if difficulty == "easy":
        return random.randint(4,6)
    elif difficulty == "medium":
        return random.randint(7,9)
    else:
        return random.randint(10,12)

def display_current_progress(word, guessed_letters, remaining_guesses):
    print(f"Guesses left = {remaining_guesses}")
    for letter in word:
        if letter in guessed_letters:
            print(letter, end="")
        else:
            print("_", end = "")
    print()

def play_game(word):
    guesses = []
    guesses_remaining = 6
    correct_guess = False
    game_over = 0
    win = False
    while True:
        if(guesses_remaining <= 0):
            break
        game_over = 0
        for letter in word:
            if letter in guesses:
                game_over += 1
        if game_over == len(word):
            win = True
            break
        print()
        guess = input("Guess a letter: ").lower()
        while len(guess) != 1 or not guess.isalpha():
            guess = input("Please enter a valid letter: ")
        while guess in guesses:
            guess = input("Already guessed, enter a different letter: ")
        guesses.append(guess)
        correct_guess = False
        for letter in word:
            if letter == guess:
                correct_guess = True
        if not correct_guess:
            print("Incorrect guess")
            guesses_remaining -= 1
        else:
            print("Correct guess!")
        display_current_progress(word, guesses, guesses_remaining)
        
    print()
    if win:
        print("You won!")
    else:
        print("You lost :(")
        print(f"The word was {word}")
    

def main():
    difficulty = get_user_difficulty()
    word = fetch_word(difficulty)
    play_game(word)

if __name__ == "__main__":
    main()
