# Calculate the multiplication and sum of two numbers
# specify datatype using int() for input
# simple if & else loop
number1 = int(input("Input number 1:"))
number2 = int(input("Input number 2:"))

sum = number1 + number2
product = number1 * number2

if product > 1000 :
  print(f"Product of {number1} & {number2}")
  print(product)
else :
  print(f"Sum of {number1} & {number2}")
  print(sum)

