# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
from contextlib import nullcontext

names = []
letter = nullcontext
placeholer = "[name]"

with open("./Input/Names/invited_names.txt") as name_file:
    for line in name_file:
        names.append(line.strip())


with open("./Input/Letters/starting_letter.txt") as letter_file:
    content = letter_file.read()


for name in names:
    file_name = f"./Output/ReadyToSend/letter-{name}.txt"
    with open(file_name, mode="w") as ready_to_send:
        content = content.replace("[name]", name)
        ready_to_send.write(content)
