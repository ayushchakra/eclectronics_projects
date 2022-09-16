import numpy as np
import os

# To analyze initial sweep data (R=10k to R=10M), uncomment this file.
# FILE_NAME = f'{os.getcwd()}/ltspice/ltspice_data/initial_sweep.txt'

# To analyze refined sweep data (R=1M to R=10M), uncomment this file.
# FILE_NAME = f'{os.getcwd()}/ltspice/ltspice_data/refined_sweep.txt'

# To analyze worst case analysis data, uncomment this file. Additionally,
# when running wca, uncomment lines 61 and 62 to display minimum and maximum
# periods.
# FILE_NAME = f'{os.getcwd()}/ltspice/ltspice_data/wca_data.txt'


def find_period(times, v_values, current_resistor):
    high_indexes = np.where(v_values>1.65)[0]
    low_indexes = np.where(v_values<1.65)[0]

    for index, value in enumerate(high_indexes):
        if high_indexes[index+1]-value == 1:
            continue

        start_time = times[index + 1]
        end_time = times[low_indexes[np.where(low_indexes>high_indexes[index+1])[0][0]]]

        print(f"Period of {current_resistor} is: {end_time-start_time}s")
        return end_time - start_time


def main():
    periods = []

    with open(FILE_NAME, "r") as txt_file:
        lines = txt_file.readlines()
        index = 0
        current_resistor = ""
        while index < len(lines):
            times = np.array([])
            v_values = np.array([])
            if lines[index][0] == "t":
                index += 1
            elif lines[index][0] == "S":
                current_resistor = lines[index].split(' ')[2]
                index += 1
            else:
                while index < len(lines) and lines[index][0] != "S":
                    current_list = lines[index].split()
                    times = np.append(times, float(current_list[0]))
                    v_values = np.append(v_values, float(current_list[1]))
                    index += 1
                periods.append(find_period(times, v_values, current_resistor))

    print(f'Max Period is {np.max(periods)}s')
    print(f'Min Period is {np.min(periods)}s')


if __name__ == "__main__":
    main()
