# Write a Python program that can “make change.” Your program should
# take two numbers as input, one that is a monetary amount charged and the
# other that is a monetary amount given. It should then return the number
# of each kind of bill and coin to give back as change for the difference
# between the amount given and the amount charged. The values assigned
# to the bills and coins can be based on the monetary system of any current
# or former government. Try to design your program so that it returns as
# few bills and coins as possible.

def change_bill(given_amt,charge_amt,bills=[100,50,20,10,5,2,1]):
    change=[]
    diff=given_amt-charge_amt
    if diff<0:
        print("Insufficient anount given")
        return
    else:
        for bill in bills:
            factor=diff//bill
            if factor>0:
                for _ in range(factor):
                    change.append(bill)
                diff = diff-bill*factor
            if diff==0:
                break
        return change
            




charge_amt=int(input("Enter the Charge amount given: "))
given_amt=int(input("Enter the Given amount given: "))

print(change_bill(given_amt,charge_amt))
