# Let's create a journal\
with open("journal.txt", "a") as journal:
    while True: # Infinite loop until q is pressed
        text = input("Enter a journal entry: (press q to quit): ")
        if text == "q":
            break
        journal.write(text.capitalize()+"\n") # need to add new line

