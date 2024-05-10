PLACEHOLDER = "[name]"

# first method readlines method
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

# second method replace method
with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        # third method strip takes away anything at the beginning and end of string thus takes \n out
        stripped_name = name.strip()
        # Replaces old [name] with new name from names list
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)




