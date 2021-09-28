#A program that displays profit made from revenue made

def profit_made():
    TotRev = int(input("Enter the total revenue made: "))
    profit = TotRev * (23/100)
    print("Profit made is: ", profit)


profit_made()