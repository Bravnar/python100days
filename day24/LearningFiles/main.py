

# This is a simple way to read the file
file = open("my_file.txt")
contents = file.read()
print(contents)
file.close()


# Different way to open files, better and simpler
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# writing to a file
# "w" will replace
# "a" will append
# if file doesn't exist, a new file will be created
with open("my_file.txt", mode="a") as file:
    file.write("\nNew text.")


with open("new_file.txt", mode="w") as file:
    file.write("Hello World!\nI am a new file!")
