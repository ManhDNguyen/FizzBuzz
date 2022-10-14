#FizzBuzz
#Created By: Manh Nguyen

print("This program outputs 100 numbers incrementally, replacing any number divisible by three with the word 'Fizz', and any number divisible by five with the word 'Buzz'")
print("If the number is divisble by both three and five, the number will be replaced with the word 'FizzBuzz'")

for numbers in range(1,101):
    if numbers % 3 == 0 and numbers % 5 == 0:
      print("FizzBuzz!")
      continue
    elif numbers % 3 == 0:
        print("Fizz")
        continue
    elif numbers % 5 == 0:
      print("Buzz")
      continue
    print(numbers)

print("\nGoodbye!")
