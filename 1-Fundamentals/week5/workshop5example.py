import random

def gues_random_number(tries,start,stop):
   number = random.randint(start,stop)
   while tries !=0:
        guess =float(input("guess a number: "))
        print(number)
        if number == guess:
            print("You guessed it")
            return
        elif number < guess:
            print("guess lower")
            tries -= 1
        elif number > guess:
            print( "guess higher")
            tries -= 1
            #tries
        if tries == 0:
            print("Out of tries")
#gues_random_number(5,3,8)
#task 2
def guess_random_num_linear(tries,start,stop):
    number_2 = random.randint(start,stop)
    a_list = list(range(start,stop))
    print(number_2)
    print(a_list)
#linear algo
    for x in range(len(a_list)):
        print(x)
        if a_list[x] == number_2:
            print("Found at index", x)
            return x
            break
        if number_2 == x:
            print("You guessed it")
            return
            break
        elif number_2 < x:
            print("guess lower")
            tries -= 1
        elif number_2 > x:
            print( "guess higher")
            tries -= 1
        if tries == 0:
            print("Out of tries")
            break
    return -1
#task 3
def guess_random_num_binary(tries,start,stop):
    number_3 = random.randint(start,stop)
    b_list = list(range(start,stop))
    print(number_3)
    print(b_list)
    lower_bound = 0
    upper_bound = len(b_list) - 1
    while lower_bound <= upper_bound:
        pivot = (lower_bound + upper_bound) // 2
        pivot_value = b_list[pivot]
        if pivot_value == number_3:
            print("you guesed it")
            return pivot
        if pivot_value > number_3:
            upper_bound = pivot - 1
        else:
            lower_bound = pivot + 1
#tries thing        
        #if number_3 == pivot:
        #    print("You guessed it")
        #    break
        if number_3 < pivot:
            print("guess lower")
            tries -= 1
        elif number_3 > pivot:
            print( "guess higher")
            tries -= 1
        if tries == 0:
            print("Out of tries")
            break
    return -1
guess_random_num_binary(5,0,10)
#guess_random_num_linear(5,0,5)