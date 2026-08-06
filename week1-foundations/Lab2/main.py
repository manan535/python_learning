import string
from collections import Counter


# Task 1
def word_count(text):
    text = text.lower()

    for ch in string.punctuation:
        text = text.replace(ch, "")

    words = text.split()

    counts = {}

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts


# Task 2
def word_count_counter(text):
    text = text.lower()

    for ch in string.punctuation:
        text = text.replace(ch, "")

    words = text.split()

    return Counter(words)


# Task 3
def flatten(nested):
    result = []

    for sublist in nested:
        for item in sublist:
            result.append(item)

    return result


# Task 4
def flatten_comprehension(nested):
    return [item for sublist in nested for item in sublist]


# Task 5
def mean_of_file(path):
    numbers = []

    try:
        with open(path, "r") as file:
            for line in file:
                numbers.append(float(line.strip()))

        if len(numbers) == 0:
            return None

        return sum(numbers) / len(numbers)

    except FileNotFoundError:
        print("Error: File not found.")
        return None

    except ValueError:
        print("Error: File contains non-numeric data.")
        return None


# Task 6
if __name__ == "__main__":

    sample = "Hello, hello! Python is great. Python!"

    print("Task 1")
    print(word_count(sample))

    print("\nTask 2")
    print(word_count_counter(sample))

    nested = [[1, 2], [3, 4], [5, 6]]

    print("\nTask 3")
    print(flatten(nested))

    print("\nTask 4")
    print(flatten_comprehension(nested))

    print("\nTask 5")
    print(mean_of_file("numbers.txt"))