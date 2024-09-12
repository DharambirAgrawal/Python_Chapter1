# Write a Python program that can take a positive integer greater than 2 as
# input and write out the number of times one must repeatedly divide this
# number by 2 before getting a value less than 2.


def divide_by_two(n):
    count=0
    if n==2:
        count+=1
        return count
    while n>2:
        n=n/2
        count+=1
    return count




num=int(input("Enter a number greater than 2: "))

divide_by_two(num)
