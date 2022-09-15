import pdb
import numpy as np
import matplotlib.pyplot as plt

file_name = 'wca_data.txt'

def plot():
    plt.plot(times, v_values)
    plt.axis('equal')
    plt.ylim(0, 3.3)
    plt.show()


def find_period(times, v_values):
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
    time_high = times[index]
    period = (time_high-time_low)*2
    # print(f'Period: {(time_high-time_low)*2}s')
    return period

periods = []

with open(file_name, 'r') as txt_file:
    lines = txt_file.readlines()
    index = 0
    while index < len(lines):
        times = np.array([])
        v_values = np.array([])
        if lines[index][0] == 't' or lines[index][0] == 'S':
            index += 1
            continue
        while index < len(lines) and lines[index][0] != 'S':
            current_list = lines[index].split()
            times = np.append(times, float(current_list[0]))
            v_values = np.append(v_values, float(current_list[1]))
            index += 1
        periods.append(find_period(times, v_values))

max_period = np.max(periods)
min_period = np.min(periods)

print(f'Max Period is {max_period}s')
print(f'Min Period is {min_period}s')