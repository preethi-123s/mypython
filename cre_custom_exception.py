class NegativeNumberError(Exception):
  pass

def check_positive(number):
  if number < 0:
    raise NegativeNumberError("Negative number entered.")

try:
  num = int(input("enter a positive number:"))
  check_positive(num)
  print("Valid positive number:", num)
except NegativeNumberError as e:
  print(e)
