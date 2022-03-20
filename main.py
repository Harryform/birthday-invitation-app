# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
    
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
with open("../Mail Merge Project Start/Input/Letters/starting_letter.txt", 'r') as file:
    letter = file.readlines(1)

with open("../Mail Merge Project Start/Input/Letters/starting_letter.txt", 'r') as file:
    whole_letter = file.readlines()

invitees = []
with open("../Mail Merge Project Start/Input/Names/invited_names.txt") as data:
    for line in data.readlines():
        invitees.append(line)

txt = str(letter)
for invitee in invitees:
    new_letter = txt.replace("[name]", f"{invitee}")

# new_opening = new_letter.strip()







    # new_name1 = new_letter1.strip("'[]n\\,Dear ['")
    # invitee1 = data.readlines(1)
    # invitee2 = data.readlines(2)
    # invitee3 = data.readlines(3)
    # invitee4 = data.readlines(4)
    # invitee5 = data.readlines(5)
    # invitee6 = data.readlines(6)
    # invitee7 = data.readlines(7)
    # invitee8 = data.readlines(8)


# txt = str(letter)
#
# new_letter1 = txt.replace("[name]", f"{invitee1}")
# new_letter2 = txt.replace("[name]", f"{invitee2}")
# new_letter3 = txt.replace("[name]", f"{invitee3}")
# new_letter4 = txt.replace("[name]", f"{invitee4}")
# new_letter5 = txt.replace("[name]", f"{invitee5}")
# new_letter6 = txt.replace("[name]", f"{invitee6}")
# new_letter7 = txt.replace("[name]", f"{invitee7}")
# new_letter8 = txt.replace("[name]", f"{invitee8}")
#
#
# new_name1 = new_letter1.strip("'[]n\\,Dear ['")
# new_name2 = new_letter2.strip("'[]n\\,Dear ['")
# new_name3 = new_letter3.strip("'[]n\\,Dear ['")
# new_name4 = new_letter4.strip("'[]n\\,Dear ['")
# new_name5 = new_letter5.strip("'[]n\\,Dear ['")
# new_name6 = new_letter6.strip("'[]n\\,Dear ['")
# new_name7 = new_letter7.strip("'[]n\\,Dear ['")
# new_name8 = new_letter8.strip("'[]n\\,Dear ['")
#
# revised_letter1 = txt.replace("[name]", f"{new_name1}")
# revised_letter2 = txt.replace("[name]", f"{new_name2}")
# revised_letter3 = txt.replace("[name]", f"{new_name3}")
# revised_letter4 = txt.replace("[name]", f"{new_name4}")
# revised_letter5 = txt.replace("[name]", f"{new_name5}")
# revised_letter6 = txt.replace("[name]", f"{new_name6}")
# revised_letter7 = txt.replace("[name]", f"{new_name7}")
# revised_letter8 = txt.replace("[name]", f"{new_name8}")


# print(revised_letter1)
# print(revised_letter2)
# print(revised_letter3)
# print(revised_letter4)
# print(revised_letter5)
# print(revised_letter6)
# print(revised_letter7)
# print(revised_letter8)

