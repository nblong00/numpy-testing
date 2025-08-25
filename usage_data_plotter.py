import numpy as np
import csv


def gather_user_input():
    user_input = input('Enter file relative or absolute path: ')
    return user_input


def convert_array_values_to_int(row):
    converted_row = [int(i) for i in row]
    return converted_row


def calc_mean(usage_data):
    usage_mean = usage_data.mean(axis=1)
    return usage_mean


def calc_min_max(usage_data):
    calc_min = usage_data.min(axis=1)
    calc_max = usage_data.max(axis=1)
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
        usage_data = np.squeeze(usage_data)
        return usage_data


def showcase_mean_results(usage_mean):
    print("\nAverage daily usage over two week periods:\n")
    for number, item in enumerate(usage_mean, 1):
        if number != 1:
            print(f"Week {number + 1} & {number + 2}: {np.round(item, 2)}")
        else:
            print(f"Week {number} & {number + 1}: {np.round(item, 2)}")
    print("\n----------------------------------")


def main():
    user_input = gather_user_input()
    usage_data = array_generation(user_input)
    usage_mean = calc_mean(usage_data)
    (calc_min, calc_max) = calc_min_max(usage_data)
    showcase_mean_results(usage_mean)
    # print(usage_data)
    # print(usage_mean)
    # print(calc_min)
    # print(calc_max)


if __name__ == "__main__":
    main()
