import random


def main():
    count = 0
    lvl = get_level()
    while count != 10:
        score = 0
        a, b = generate_integer(lvl)
        c = 0

        while c < 3:
            try:
                user = int(input(f"{a} + {b} = "))
                if user == a + b:
                    score += 1
                    c += 1
                    break
                else:
                    c += 1
                    if c == 3:
                        print(f"{a} + {b} = {a + b}")
                    else:
                        print("EEE")
            except:
                print("EEE")
                c += 1
                pass


        count += 1

    print(score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 1 < level > 3:
                raise ValueError
            else:
                break
        except:
            pass
    return level


def generate_integer(level):
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
    elif level == 1:
        x = random.randint(100,999)
        y = random.randint(100,999)

    return x, y


main()