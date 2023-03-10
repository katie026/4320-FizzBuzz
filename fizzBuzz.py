# Write a program that prints the numbers from 1 to 100.
# But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”.
# For numbers which are multiples of both three and five print “FizzBuzz”

def fizzBuzz(min, max):
    for x in range(min, max+1):
        output = ""
        if x % 3 == 0:
            output = output + "Fizz"
        if x % 5 == 0:
            output = output + "Buzz"
        if x % 5 != 0 and x % 3 != 0:
            output = output + str(x)
        print(output)

def main():
    fizzBuzz(1, 100)

main()