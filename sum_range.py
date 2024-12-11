start = int(input("Enter the start of the range:"))
end = int(input("Enter the end of the range:"))
sum = 0
for i in range(start, end + 1):
  sum += i
print("The sum is:", sum)
