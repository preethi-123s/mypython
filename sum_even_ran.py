start = int(input("Enter start of range:"))
end = int(input("Enter end of range:"))
even_sum = 0
for sum in range(start,end + 1):
  if num % 2 == 0:
    even_sum += num
print("Sum of even number:",even_sum)
