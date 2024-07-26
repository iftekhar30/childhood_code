import time

text = "A lazy dog is sleeping in the streets"
words = text.split()
print(text)

if type(input("press any key to start. ")) == str:
    start = time.time()
    user = input("text: ")
    user_words = user.split()
    correct = set(words) & set(user_words)
    end = time.time()
    total = end-start
    speed = len(correct)/total*60
    acc = len(correct)/len(words)*100

    print(f"Your typing speed is {round(speed)} WPM")
    print(f"Accurecy: {acc}%")

