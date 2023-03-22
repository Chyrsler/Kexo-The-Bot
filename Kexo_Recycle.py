import os, random

File_inv = "RecycleFit/KexoGarbageCollect.text"
File_qst = "RecycleFit/KexoQuest.text"
File_clt = "RecycleFit/KexoCollection.text"

def KexoInvRec(UserFile, ListOfItems=[]):
    global TotalItem
    TotalItem = [] #stores the total of the items data

    with open(UserFile, "r") as f:
        UserInv = f.readlines()

    #counts how many item there is
    for i in range(len(ListOfItems)):
        total = 0

        for AllItems in UserInv:
            AllItems = AllItems.strip('\n')

            if ListOfItems[i] == AllItems:
                total += 1
            
        TotalItem.append(total)
    
    #outputs the total to the user
    for i in range(len(ListOfItems)):
        print(f"{i + 1}. {ListOfItems[i]}: {TotalItem[i]}")

def KexoMachine(name):
    all_garbage = ["plastic spoon", "plastic fork", "plastic plate", "old tv", "broken phone", "shredded paper", "plastic bag", "broken door"]
    all_places = [["game", "1"], ["lesson", "3"], ["japanese", "4"], ["to-do", "6"], ["update", "7"], ["credits", "8"]]

    if not os.path.isfile(File_inv) and not os.path.isfile(File_qst):
        os.mkdir("RecycleFit")

        with open(File_inv, "w") as f:
            pass

        with open(File_qst, "w") as f:
            pass

        with open(File_clt, "w") as f:
            pass
        
        print(f"Kexo: Well {name}, you might be asking: 'what's this all about'. To which i say, erm... I don't know, i didn't really thought of this...")

    while True:
        print("Kexo: Type in 'help' for a full list of commands.")
        KexoInput = input("> ").strip().lower()
        print()

        if KexoInput == "quit" or KexoInput == "5": #placed up here to prevent any of the codes below from executing and instantly exits.
            break

        if KexoInput == "help":
            print(f"""Kexo: Hello {name}, here's the full list of commands here!
    1. Quest: Search around the program for 'garbage' to collect!
    2. Inventory: Check your 'garbage' collection!
    3. Combine: Turn those junk of yours into an item of a higher value! What can you do with it? I guess it's just for collection
    4. Collection: The result of your junk-transforming! Very cool! Getting all the collection will reward you a SPECIAL trophy, haha made just for you!
    5. Quit: Quite literally quits this part of the program \n""")

        if KexoInput == "quest" or KexoInput == "1":
            with open(File_qst, "r") as f:
                OngoingQuest = f.readlines()
            
            if OngoingQuest == []:
                garbage = random.choice(all_garbage)
                place = random.choice(all_places)

                print(f"Kexo: Welcome {name}, i've heard there's a piece of {garbage} found in '{place[0]}', can you go grab it for me?")

                with open(File_qst, "w") as f:
                    f.write(f"{garbage}, {place[0]}, {place[1]}")

            else:
                with open(File_qst, "r") as f:
                    quest_specs = f.readlines()

                    for quests in quest_specs:
                        quests = quests.split(", ")

                print(f"Kexo: Finish your current quest first!: Reward: {quests[0]}, found in: '{quests[1]}'")

        elif KexoInput == "inventory" or KexoInput == "2":
            KexoInvRec(File_inv, ListOfItems=["plastic spoon", "plastic fork", "plastic plate", "old tv", "broken phone", "shredded paper", "plastic bag", "broken door"])

        elif KexoInput == "combine" or KexoInput == "3":
            InventoryInputted = 0 #keeps track of how many items the user has inputted
            CombinatedItems = [] #garbage that are gonna be combined stored here
            CollectionItem = ["golden chair", "golden phone", "golden table", "golden piano", "golden computer", "golden plug", "golden shirt"]

            print("Kexo: AAAAND BEHOLD OUR MACHINE-TRASH-COMBINER 2.0!")
            print("""
    _.,-----/=\-----,._
   (__ ~~~'''''''~~~ __)

                
    | ~~~'''''''''~~~ |
    | |  ; ,   , ;  | |
    | |  | |   | |  | |
    | |  | |   | |  | |
    | |  | |   | |  | |
    | |  | |   | |  | |
    | |  | |   | |  | |
    | |  | |   | |  | |
    | |  | |   | |  | |
    |. \_| |   | |_/ .|
    `-,.__ ~~~ __.,-'""")

            print("Kexo: Wait, a trash can? that's so lame... Benny! could've atleast grabbed an art of a time machine and label it something like... 'The Junk Transformer', seriously.. A trash can?? (enter to continue)")
            input()
            
            print("Kexo: Whatever, combine THREE trash of yours and you'll get something completely new! Enter your garbage based on their index! remember, once you put in your item, there is no going back! (enter to show inventory)")
            input()

            #this long process is literally just trying to get the user to input the items they want to combine.
            while InventoryInputted != 3:
                KexoInvRec(File_inv, ListOfItems=["plastic spoon", "plastic fork", "plastic plate", "old tv", "broken phone", "shredded paper", "plastic bag", "broken door"])

                try:
                    UserCombination = int(input("> "))
                    ItemIndex = UserCombination - 1

                    if UserCombination < 1 or UserCombination > 8:
                        raise ValueError()

                except ValueError:
                    print("Kexo: Enter a valid number from within the list. \n")
                    break
                
                print()
                print(f"Kexo: So you have chosen {all_garbage[ItemIndex]}, how many do you want to input it?")

                try:
                    UserMultiplication = int(input("> "))
                    
                    if UserMultiplication <= 0 or InventoryInputted + UserMultiplication > 3:
                        raise ValueError()

                    if TotalItem[ItemIndex] >= UserMultiplication:
                        InventoryInputted += UserMultiplication
                        CombinatedItems.append(f"{UserMultiplication}. {all_garbage[ItemIndex]}") #for later use.
                        
                        #Removing the item after the user selected it.
                        with open(File_inv, "r") as f:
                            UserInv = f.readlines()
                    
                        for i in range(UserMultiplication):
                            with open(File_inv, "w") as f:
                                for Inv in UserInv:
                                    if all_garbage[ItemIndex] != Inv.strip("\n"):
                                        f.write(Inv)
                            
                    print()
                    
                except ValueError:
                    print("Kexo: Please enter a positive integer below 4 based on your total items in your inventory.\n")
                    break
            
            if InventoryInputted == 3:
                print("Kexo: So, combining", *CombinatedItems, "gets you..")
                print("Kexo: Drumroll please *bum* *bum* (enter to reveal)")
                input()
                
                prize = random.choice(CollectionItem)

                with open(File_clt, "a") as f:
                    f.write(f"{prize}\n")

                print(f"Kexo: {prize}! Congratulations, it has been added to your collection!")

        elif KexoInput == "collection" or KexoInput == "4":
            KexoInvRec(File_clt, ListOfItems=["golden chair", "golden phone", "golden table", "golden piano", "golden computer", "golden plug", "golden shirt"])

            if 0 not in TotalItem:
                with open("SaveFile/KexoTrophy.text", "r") as f:
                    trophies = f.readlines()

                    boolean_check = []

                    for content in trophies:
                        boolean_check.append("The Golden Trophy" not in content)
                        
                        if False not in boolean_check:
                            print()
                            print("Kexo: I see that you have gotten every single item, psst i'm here to give you a reward: 'THE GOLDEN TROPHY'. Type in 'trophies' or '9' in the main menu to view your current trophies.")

                            with open("SaveFile/KexoTrophy.text", "a") as f:
                                f.write("The Golden Trophy, 'ooooh shiny..'. Achieved by getting all golden items.\n")