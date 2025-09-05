#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Letters/starting_letter.txt") as letter_file:
    start_text = letter_file.read()

with open("./Input/Names/invited_names.txt") as name_file:
    list_of_receivers = name_file.readlines()

for receiver in list_of_receivers:
    receiver = receiver.strip()
    personalized_text = start_text.replace("[name]", receiver)
    personalized_text = personalized_text.replace("Angela", "Silje")
    with open(f"./Output/ReadyToSend/invite_to_{receiver}.txt", "w") as file:
        file.write(personalized_text)
    print(f"Created invite for {receiver}")

