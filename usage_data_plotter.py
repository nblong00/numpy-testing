import numpy as np
import csv


def gather_user_input():
    user_input = input('Enter file relative or absolute path: ')
    return user_input


def convert_array_values_to_int(row):
    coverted_row = [int(i) for i in row]
    return coverted_row


def calc_mean(usage_data):
    usage_mean = usage_data.mean(axis=2)
    return usage_mean


def calc_min_max(usage_data):
    calc_min = usage_data.min(axis=2)
    calc_max = usage_data.max(axis=2)
    return calc_min, calc_max


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
        return usage_data


def main():
    user_input = gather_user_input()
    usage_data = array_generation(user_input)
    usage_mean = calc_mean(usage_data)
    (calc_min, calc_max) = calc_min_max(usage_data)
    print(usage_mean)
    print(calc_min)
    print(calc_max)


if __name__ == "__main__":
    main()
