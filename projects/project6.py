# A common punishment for school children is to write out a sentence multiple times. Write a Python stand-alone program that will write out the
# following sentence one hundred times: “I will never spam my friends
# again.” Your program should number each of the sentences and it should
# make eight different random-looking typos.
import random as rnd

def print_punish():
    for i in range(1,101):
        str="I will never spam my friends again."
        words = str.split()
    
        for _ in range (8):
            choice=rnd.choice(words)
            choice_arr=list(choice)
            if rnd.randint(0,1)==1:
                choice_arr.insert(rnd.randint(0,len(choice_arr)-1),rnd.choice('abcdefghijklmnopqrstuvwxyz'))
                # ' '.join(choice_arr) #converting again array to string
                # words.index(choice) # finding index of the choice
                words[words.index(choice)]=''.join(choice_arr) # replacing the choice with the new choice
            else:
                index=choice_arr.index(rnd.choice(choice_arr))
                # print(index)
                if(index>0):
                    choice_arr.pop(index)
                  
                words[words.index(choice)]=''.join(choice_arr) # replacing the choice with the new choice
                
        print(f"{' '.join(words)}")

print_punish()
