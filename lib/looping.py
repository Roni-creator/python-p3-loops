#!/usr/bin/env python3

def happy_new_year():
    i=10
    while i>0:
        print(i)
        i-=1
    print ("Happy New Year!")
    pass

def square_integers(int_list):
    for i in range (len(int_list)):
        int_list[i] =int_list[i]*int_list[i]
    return int_list
    pass

def fizzbuzz():
    for number in range(1, 101):
        if(number % 3 ==0 and number % 5 == 0):
            print("FizzBuzz")
        elif(number % 5 == 0):
            print("Buzz")
        elif(number % 3 == 0):
            print("Fizz")
        else:
            print(number)
    pass
