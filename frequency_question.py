# Frequency Question
from statistics import mode

entered_digits = []
num_of_digits = int(input(("How many numeric digits would you like to enter? ")))
while (len(entered_digits) < num_of_digits):
    entered_digits.append(int(input("Enter digit: ")))
most_freq_digit = mode(entered_digits)
if entered_digits.most_common(1) != entered_digits.most_common():
    print("Data was multimodal")
counter = 0
i = 0
for i in entered_digits:
    if (entered_digits[i] == most_freq_digit):
        counter += 1
print("The most frequently entered digit occured", counter, "times.")