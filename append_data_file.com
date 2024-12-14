with open("/content/PREETHI S.txt","a")as file:
  file.write("Let's learn file handling.\n")
with open("/content/PREETHI S.txt","r")as file:
  print(file.read())
