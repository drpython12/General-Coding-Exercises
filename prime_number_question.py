# Prime number question

def is_prime(number):
    if number <= 1:
        print("Not greater than 1.")
    else:
        for i in range(2, number):
            if (number % i) == 0:
                print("Is not prime.")
                break
            else:
                print("Is prime.")
                break

x = True 
while (x == True):
    is_prime(int(input("Enter a number: ")))
    print("1) Enter another number")
    print("2) Quit")
    if (int(input("Enter choice: ")) == 1):
        x = True
    else:
        x = False