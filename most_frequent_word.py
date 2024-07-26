from collections import Counter


def most_frequent_word(file_name, n): 
    words = []


    with open("Plain Text.txt", 'r') as f:
        for i in f:
            for word in i.rstrip().split():

                words.append(word.lower())
            

    counter = Counter(words)
    return ', '.join([tup[0] for tup in counter.most_common(n)])


def main():
    file_path = "Plain Text.txt"
    most_common_word = most_frequent_word(file_path, 1)
    if len(most_common_word.split(',')) == 1:
        print(f"Most common word in the file is '{most_common_word}'")
    elif len(most_common_word.split(',')) > 1:
        print(f"Most common words in the file are '{most_common_word}'")


if __name__ == "__main__":
    main()