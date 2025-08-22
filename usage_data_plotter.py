import numpy as np
import csv


def gather_user_input():
    user_input = input('Enter file relative or absolute path: ')
    return user_input


def convert_array_values_to_int(row):
    coverted_row = [int(i) for i in row]
    return coverted_row


def array_generation(user_input):
    with open(user_input, mode="r") as f:
        reader = csv.reader(f)
        first_row = next(reader)
        usage_data = np.array([[
            first_row
        ]], np.uint16)
        for row in reader:
            converted_row = convert_array_values_to_int(row)
            usage_data = np.append(usage_data, [[converted_row]], axis=1)
        print(usage_data)


def main():
    user_input = gather_user_input()
    array_generation(user_input)


if __name__ == "__main__":
    main()
