#  The birthday paradox says that the probability that two people in a room
# will have the same birthday is more than half, provided n, the number of
# people in the room, is more than 23. This property is not really a paradox,
# but many people find it surprising. Design a Python program that can test
# this paradox by a series of experiments on randomly generated birthdays,
# which test this paradox for n = 5,10,15,20,...,100.


def probability_no_shared_birthday(n):
    days = 365
    probability = 1.0
    for i in range(n):
        probability *= (days - i) / days
    return probability



for n in range(5,101,5):
    prob_no_shared = probability_no_shared_birthday(n)
    prob_shared = 1 - prob_no_shared
    print(f"Probability of no shared birthday for {n} people: {prob_no_shared:.4f}")
    print(f"Probability of at least one shared birthday for {n} people: {prob_shared:.4f}")
    print('\n\n')


"""
Their are 365 days so total possible combinations = 365^n

For the first person, there are 365 choices.
For the second person, there are 364 choices (to avoid the first persons birthday).
For the third person, there are 363 choices, and so on.
This continues until the 
n-th person, who has  365-n+1 choices.
so favourable outcome= 365*364*363*...*(365-n+1)  =  365!/(365-n)!

so Probability of no shared birthday = favourable outcome/total possible combinations
= 365!/(365-n)! * 1/365^n

P(no shared birthday)=365/365 * 364/365 * 363/365 * ... * (365-n+1)/365
"""

