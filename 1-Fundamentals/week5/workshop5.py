import random

def guess_random_number(tries, start, stop):

    number = random.randint(start,stop)
    
    while tries != 0:
        guess = float(input("Guess a number!"))
        print(number)

        if number == guess:
            print("You guessed it! Congrats")
            return 
        elif number < guess:
            print("Guess lower!")
            tries -= 1
        elif number > guess:
            print("Guess higher")
            tries -= 1
        elif tries == 0:
            print("Out of tries")
#driver code
guess_random_number(10,0,10)

def guess_random_num_linear(tries, start, stop):
    number_2 = random.randint(start,stop) 
    a_list = list(range(start, stop))
    print(number_2)
    print(a_list)
    #linearsearch function
    for x in range(len(a_list)):
        print(x)
        if a_list[x] == number_2:
            print("Found at index" , x)
            return x 
        tries -= 1 
        break
   
    if number_2 == x:
            print("You guessed it! Congrats")
            return 
    elif number_2 < x:
            print("Guess lower!")
            tries -= 1
    elif number_2 > x:
            print("Guess higher")
            tries -= 1
    elif tries == 0:
            print("Out of tries")
    else:
        print("Try another input!")

#guess_random_num_linear(10,0,5)

#task3

def guess_random_num_binary(tries, start, stop):
    number_3 = random.randint(start,stop) 
    b_list = list(range(start, stop))
    print(number_3)
    print(b_list)
    lower_bound = 0
    upper_bound = len(b_list) - 1
    while lower_bound <= upper_bound:
        pivot = (lower_bound + upper_bound) // 2
        pivot_value =b_list[pivot]
        if pivot == number_3:
            print("You guessed it!")
            return pivot
        if pivot_value > number_3:
            upper_bound  = pivot - 1  
        else:
             lower_bound = pivot + 1
        # if number_3 == pivot:
        #      print("You guessed it! Congrats")
        
        if number_3 < pivot:
            print("It's lower!")
            tries -= 1

        elif number_3 > pivot:
            print("It's higher!")
            tries -= 1

        elif tries == 0:
            print("Out of tries")
            return -1


#guess_random_num_binary(2,0,50)

def guess_random_num_opt(tries, start, stop):
    







# #input lines for parameters
# tries = int(input('How many tries?'))
# start = int(input('Where are we starting?'))
# stop = int(input('Where are we starting?'))
# guess_random_num_opt    