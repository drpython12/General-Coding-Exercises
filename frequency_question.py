# Frequency Question

import statistics

entered_digits = []
num_of_digits = int(input(("How many numeric digits would you like to enter? ")))

while (len(entered_digits) < num_of_digits):
    entered_digits.append(int(input("Enter digit: ")))

most_freq_digit = statistics.mode(entered_digits)

if len(statistics.multimode(entered_digits)) > 1:
    print("Data was multimodal")
else:
    counter = 0
    i = 0
    for i in range(0, len(entered_digits)):
        if (entered_digits[i] == most_freq_digit):
            counter += 1
    print("The most frequently entered digit occured", counter, "times.")