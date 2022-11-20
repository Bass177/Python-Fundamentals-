def fizzbuzz(num):
    for num in range(1, num):
        if num % 3 == 0 and num % 5 ==0:
            print('FizzBuzz') 
        elif num % 5 == 0:
            print('Buzz')
        elif num % 3 ==0:
            print('Fizz') 
        else:
            print(num)


num = int(input('Run a number!'))
fizzbuzz(num)