'''Write a Python program that iterates the integers from 1 to 50. For multiples of three print "Fizz" 
instead of the number and for multiples of 
five print "Buzz". For numbers that are multiples of three and five, print "FizzBuzz".'''

#divisible by 3 Fuzz
#divisible by 5 Buzz
'''def multiple3():
    if(number%3==0):
        print("Fizz")
def multiple5():
    if(number%5==0):
        print("Buzz")
def multiple35():
    if(number%3==0 & number%5==0):
        print("FizzBuzz")
#main function
for i in range(1,50):
    print(multiple3(i))
    print(multiple5(i))
    print(multiple35(i))'''

'''for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)'''

'''Write a Python program that iterates the integers from 1 to 50. For multiples of three print "Fizz" 
instead of the number and for multiples of 
five print "Buzz". For numbers that are multiples of three and five, print "FizzBuzz".'''
def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return str(num)

def main():
    for num in range(1, 51):
        print(fizzbuzz(num))

if __name__ == "__main__":
    main()




