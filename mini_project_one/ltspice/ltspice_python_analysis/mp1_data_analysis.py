import pdb
import numpy as np
import matplotlib.pyplot as plt
import os

FILE_NAME = f'{os.getcwd()}/ltspice/ltspice_data/refined_sweep.txt'

def find_period(times, v_values, current_resistor):
    index = 0
    t_val = times[0]
    v_val = v_values[0]
    while t_val < 2.0 and v_val < 1.65:
        index += 1
        t_val = times[index]
        v_val = v_values[index]
    while v_val > 1.65:
        index += 1
        v_val = v_values[index]
    time_low = times[index]
    while v_val < 1.65:
        index += 1
        v_val = v_values[index]
    while v_val > 1.65:
        index += 1
        v_val = v_values[index]
    time_high = times[index]
    period = (time_high-time_low)
    print(f'Period of {current_resistor} is: {period}s')
    return period

def main():
    periods = []

    with open(FILE_NAME, 'r') as txt_file:
        lines = txt_file.readlines()
        index = 0
        current_resistor = ''
        while index < len(lines):
            times = np.array([])
            v_values = np.array([])
            if lines[index][0] == 't':
                index += 1
                continue
            if lines[index][0] == 'S':
                current_resistor = lines[index][18:-15]
                index += 1
                continue
            while index < len(lines) and lines[index][0] != 'S':
                current_list = lines[index].split()
                times = np.append(times, float(current_list[0]))
                v_values = np.append(v_values, float(current_list[1]))
                index += 1
            periods.append(find_period(times, v_values, current_resistor))

    # print(f'Max Period is {np.max(periods)}s')
    # print(f'Min Period is {np.min(periods)}s')

if __name__ == '__main__':
    main()