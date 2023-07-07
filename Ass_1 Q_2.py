file = input("Give file name: ")
dot = "."
ex = file.rfind(dot)
print("Your extension is:", file[(ex+1)::])
