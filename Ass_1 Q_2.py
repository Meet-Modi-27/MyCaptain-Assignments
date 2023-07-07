file = input("Give file name: ")
dot = "."
ex = file.rfind(dot) #ex = file.rfind(".")
print("Your extension is:", file[(ex+1)::])
