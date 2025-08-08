#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


def create_letter(name: str, blueprint: str):
    clean_name = name.strip("\n")
    new_letter = blueprint.replace("[name]", clean_name).replace("Angela", "Stan")
    with open(f"./Output/ReadyToSend/invitation_{clean_name}.txt", "w") as letter:
        letter.write(new_letter)

def main() -> None:
    with open("./Input/Names/invited_names.txt") as file:
        names = file.readlines()

    with open("./Input/Letters/starting_letter.txt") as file:
        blueprint = file.read()

    for name in names:
        create_letter(name, blueprint)

if __name__ == "__main__":
    main()