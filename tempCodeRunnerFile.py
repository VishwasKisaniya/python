import os
import random
import string
import time
import csv


os.makedirs("assignment_3", exist_ok=True)

def random_string(length=20):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

file_count = 500
lines_per_file = 20000

for i in range(1, file_count + 1):
    file_name = f"assignment_3/file_number{i}.txt"
    with open(file_name, "w") as file:
        for _ in range(lines_per_file):
            line = random_string()
            file.write(line + "\n")

print("ALL ")

#for time execution

def convert_to_uppercase_and_measure_time(file_path):
    start_time = time.time()
    with open(file_path, "r") as file:
        lines = file.readlines()
    lines = [line.upper() for line in lines]
    with open(file_path, "w") as file:
        file.writelines(lines)
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time


execution_times = []
for i in range(1, file_count + 1):
    file_name = f"assignment_3/file_number{i}.txt"
    execution_time = convert_to_uppercase_and_measure_time(file_name)
    execution_times.append([f"file_number{i}.txt", execution_time])

# Saving the outputs to csv file
with open("question2_output.csv", "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["File Name", "Execution Time (seconds)"])
    csvwriter.writerows(execution_times)



















    