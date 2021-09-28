#a program that computes a given integer power of given number using for loop

def main():
    number = int(input("Enter a number:" ))
    expo = int(input("Enter the power: "))

    for expo in range(expo+1):
        answer = number ** expo
        print("answer is: ", answer)

main()