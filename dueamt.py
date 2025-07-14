inpt = float(input("Enter bill amount: "))
inpt2 = float(input("Enter the amount you payed: "))
due = inpt-inpt2
if due > 0:
    print(due,"dollers is due")
elif due==0:
    print(due,"dollers is due")
elif due < 0:
    print(due,"dollers is due")
else:
    print("INVALID INPUT")