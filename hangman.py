import sys
import random
def play_again():
    while True:
        response = input("Do you want to play again? (y)es or (n)o -> ").lower()
        if response == 'y':
            play_hangman()
            break
        elif response == 'n':
            print("See you later...")
            exit()
        else:
            pass


def play_game(word, hidden, count):
    chs = list(enumerate(word))
    while count != 4:
        guess = input(f"Enter your guess({4-count}), {hidden}---> ").strip()
        if guess in word and len(guess) == 1:
            for i in chs:
                if i[1] == guess:
                    hidden = hidden[0:i[0]] + i[1] + hidden[i[0]+1:]
                    chs.remove(i)
                    break
            
        elif guess not in word:
            count += 1
            if count == 1:
                print("wrong answer")
                print("   |")
                print("   |")
                print("   |")
                print("   |")
                print("   |")
                print("   |")
                print("___|___")
            elif count == 2:
                print("wrong answer")
                print("    ____")
                print("   |")
                print("   |")
                print("   |")
                print("   |")
                print("   |")
                print("   |")
                print("___|___")
            elif count == 3:
                print("wrong answer")
                print("    ____")
                print("   |    |")
                print("   |    |")
                print("   |")
                print("   |")
                print("   |")
                print("   |")
                print("___|___")
            elif count == 4:
                print("wrong answer")
                print("    ____")
                print("   |    |")
                print("   |    |")
                print("   |    0")
                print("   |   /|\ ")
                print("   |   / \ ")
                print("   |")
                print("___|___")
                print("You are hanged!")
                play_again()
        else:
            print("Invalid")
        print(hidden)
        if hidden == word:
                print("Congratulations! you guessed the word")
                play_again()
    

def play_hangman():
    count = 0
    words_to_guess = [
       'banana'
    ]
    word = random.choice(words_to_guess)
    hidden = "_"*len(word)
    play_game(word, hidden, count)

    
print(play_hangman())