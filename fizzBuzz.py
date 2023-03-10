# Write a program that prints the numbers from 1 to 100.
# But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”.
# For numbers which are multiples of both three and five print “FizzBuzz”


# A number is divisible by another number if it can be divided equally by that number; that is, if it yields a whole number when divided by that number. For example, 6 is divisible by 3 (we say "3 divides 6") because 6/3 = 2, and 2 is a whole number.

for x in range(1, 101):
    if x%3 == 0 and x%5 == 0:
        print("FizzBuzz")
    elif x%3 == 0:
        print("Fizz")
    elif x%5 == 0:
        print("Buzz")
    else:
        print(x)
    x += 1