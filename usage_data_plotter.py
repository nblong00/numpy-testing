import numpy as np
import csv


def gather_user_input():
    user_input = input('Enter file relative or absolute path: ')
    return user_input


def array_generation(user_input):
    with open(user_input, mode="r") as f:
        reader = csv.reader(f)
        first_row = next(reader)
        usage_data = np.array([
            first_row
        ], np.uint16)
        for row in reader:
            usage_data = np.append(usage_data, [row], axis=0)
        print(usage_data)


def main():
    user_input = gather_user_input()
    array_generation(user_input)


if __name__ == "__main__":
    main()
