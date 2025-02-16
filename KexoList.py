#declarating file variable
FileList = "SaveFile/KexoToList.text"

def ShowAllList(file_index):
    with open(FileList, "r") as f:
        all_list = f.readlines()

    for lists in all_list:
        lists = lists.strip("\n")
        print(f"{file_index}. {lists}")
        file_index += 1

def KexoDoList(name):
    #creating the file if it doesn't exist
    if not os.path.isfile(FileList):
        with open(FileList, "w") as f:
            pass

        print("Kexo: Looks like you're new to this! Let me guide you a bit!")
        print("""
LIST FORMAT
> Type in 'create' below to make a new list!
> You will bet asked to type in a category for sorting purposes, use this to your advantage!
> a due date is required, enter the date the way you like it.
> All of the above must be seperated by a comma.

EXTRA NOTES
> You can show a certain type of category by typing it down below.
> You can show all the current list that is stored by typing in 'all'""")

    #main program
    while True:
        file_index = 0

        with open(FileList, "r") as f:
            all_list = f.readlines()

        print("type in 'help' for the full list of commands.")
        KexoInput = input("> ").strip().lower()
        print()

        if KexoInput == "quit" or KexoInput == "4": #placed up here to prevent any of the codes below from executing and instantly exits.
            break

        if KexoInput == "help":
            print(f"""Kexo: Hello {name}, these are the commands for everything related to this part of the program.
    1. Create -> Create another to do list
    2. Finish -> If an assignment/activity is done
    3. All -> Shows every list you have stored in the data
    > *Category Name* -> Shows that spesific type of category
    4. Quit -> Exits this section of the program
""")
            continue

        elif KexoInput == "create" or KexoInput == "1":
            print("Format: To-do activity/assignment, category, date\nEx. English assignment, school, 20 January 2023")
            try:
                Activity, Category, Due = input("> ").strip().lower().split(", ") #splitted into 3 so the program knows there's 3 data being inputted here
            except ValueError:
                print("Kexo: Hey! i can't help but tell that you input more or less data. Please stick with the list format i gave you otherwise it won't work. \n")
                continue

            with open(FileList, "a") as f:
                f.write(f"{Activity}, {Category}, {Due}\n")
            
            print()
            continue

        if all_list == []:
            print("Kexo: You have no lists yet! Make sure to create one right now! \n")
            continue

        elif KexoInput == "finish" or KexoInput == "2":
            ShowAllList(file_index)

            print("Kexo: Finish an activity/assignment by inputting their desired number.")

            try:
                KexoListDelete = int(input("> "))
            except ValueError:
                print(f"Kexo: Please enter a number that ranges from 0 to {len(all_list) - 1} \n")
                continue

            with open(FileList, "w") as f:
                for lists in all_list:                
                    if file_index != KexoListDelete:
                        f.write(lists)
                    file_index += 1
            
            print("Kexo: successfully deleted. \n")
            continue
            
        elif KexoInput == "all" or KexoInput == "3":
            ShowAllList(file_index)
            
            print()
            continue
            
        for lists in all_list:
            lists = lists.strip("\n").split(", ")
            Category = lists[1]

            if KexoInput == Category:
                print(f"- {lists[0]} is due: {lists[2]}")