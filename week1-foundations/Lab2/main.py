"""
Lab 2: Word Counter Program

Build fluency by writing small current functions
"""
import string
from collections import Counter

def word_count(text):
    text = text.lower()

    for i in string.punctuation:
        text = text.replace(i, " ")
    words = text.split()
    word_frequency = {}

    for word in words:
        if word not in word_frequency:
            word_frequency[word] = 1
        else:
            word_frequency[word] += 1
    return word_frequency


def word_count_counter(text):
    text = text.lower()
    for i in string.punctuation:
        text = text.replace(i, " ")
    words = text.split()
    return Counter(words)


def flatten(nested_list):
    flat_list = []
    for sublist in nested_list:
        for element in sublist:
            flat_list.append(element)
    return flat_list


def flatten_list_comprehension(nested_list):
    return [element for sublist in nested_list for element in sublist]


def mean_of_file(file_name):
    values = []

    try:
        with open(file_name, "r") as file:
            for line in file:
                values.append(float(line.strip()))
        if len(values) == 0:
            return None
        return sum(values) / len(values)
    except FileNotFoundError:
        print("File not found.")

    except ValueError:
        print("Invalid data.")
    return None


if __name__ == "__main__":

    text = "Hello, hello! My name is Manan!.my What > is your name?"

    print("Task 1")
    print(word_count(text))

    print("\nTask 2")
    print(word_count_counter(text))

    sample_list = [[1, 2], [3, 4], [5, 6]]

    print("\nTask 3")
    print(flatten(sample_list))

    print("\nTask 4")
    print(flatten_list_comprehension(sample_list))

    print("\nTask 5")
    print(mean_of_file("numbers.txt"))
