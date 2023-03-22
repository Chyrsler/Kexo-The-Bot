#Submission for Code Olympiad, made by Christopher Sebastian H.
#I tried placing as many notes as possible on how certain code blocks work.

import os, random

#declaring the variables
white = "\033[0;37m"
red = "\033[0;31m"
blue = "\033[0;34m"

#File Scan
Files = ["Kexo The Bot.py", "Kexo_JapanL.py", "Kexo_Lesson.py", "Kexo_Games.py", "Kexo_Recycle.py", "KexoList.py"]
Exist = [f for f in Files if not os.path.isfile(f)]

if Exist != []: #if 'Exist' is not an empty list (which means there's missing files.)
  print(f"Kexo: I have detected some missing files from your device. Please download it through this gibhut link: {blue}https://github.com/Chyrsler/Kexo-The-Bot.{white} Click on {red}code{white} and click on {red}download ZIP{white}. Alternatively, you can go to the file that you think is missing and download it from there.")
  exit()

#importing from other files
from Kexo_Games import KexoPOP, KexoRPG, KexoRPS, KexoStickFigure
from Kexo_Lesson import LessonArt, LessonArt2
from Kexo_JapanL import KexoJP
from KexoList import KexoDoList
from Kexo_Recycle import KexoMachine

MessageContinue = f"{red}(press enter to continue){white}"
Fact = []

#Introduction
if not os.path.isfile("SaveFile/KexoIntroduction.text"): #Check if the user has gone through the introduction with Kexo or not.
  print("""\
 __                                            __                    __     
/  |                                          /  |                  /  |    
$$ |   __   ______   __    __   ______        $$ |____    ______   _$$ |_   
$$ |  /  | /      \ /  \  /  | /      \       $$      \  /      \ / $$   |  
$$ |_/$$/ /$$$$$$  |$$  \/$$/ /$$$$$$  |      $$$$$$$  |/$$$$$$  |$$$$$$/   
$$   $$<  $$    $$ | $$  $$<  $$ |  $$ |      $$ |  $$ |$$ |  $$ |  $$ | __ 
$$$$$$  \ $$$$$$$$/  /$$$$  \ $$ \__$$ |      $$ |__$$ |$$ \__$$ |  $$ |/  |
$$ | $$  |$$       |/$$/ $$  |$$    $$/       $$    $$/ $$    $$/   $$  $$/ 
$$/   $$/  $$$$$$$/ $$/   $$/  $$$$$$/        $$$$$$$/   $$$$$$/     $$$$/  
""")
  
  print(f"Kexo: Hello! Welcome to the Kexo Chat Experience! {MessageContinue}")
  input()
  
  print(f"Kexo: Before we start, please use this program on FULL SCREEN mode otherwise some assets might not fit onto the console. {MessageContinue}")
  input()

  print("Kexo: Fit this long line below onto one line on your screen by expanding it.")
  print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")
  input()

  print("Kexo: I need to know your name! please input it below! (max: 20 characters)")
  
  while True:
    name = input("> ")
    
    if name.count("") > 20: #.count() needs one argument for it to work, so we enter '""' for it to count the strings.
      print("Kexo: You can't have more than 20 characters! Please input a shorter name!")
      continue
  
    elif name.count("") < 2:
      print("Kexo: A minimum of atleast 1 character is also required!")
      continue
  
    else:
      break
  
  New_Folder = os.mkdir("SaveFile")
  with open("SaveFile/KexoIntroduction.text", "w") as f:
    f.write(name)
  
  with open("SaveFile/KexoTrophy.text", "a") as f:
    f.write("Trophy Of The Beginnings, 'Wow that's brand new!'. Achieved by getting to know Kexo.\n")
  
  print(f"Kexo: {name} huh? what a wonderful name! i'll start calling you that from now on!")
  print(f"Kexo: {name}, to get started, type in {red}'help'{white} below and see the list of my commands! \n")

#If KexoIntroduction.text exist then the user skips the introduction.

with open("SaveFile/KexoIntroduction.text", "r") as f:
  name = f.read().capitalize() #get the name of the user

KexoMessage = [f"Hello {name}", "Need a list of my commands? type in 'help' below", f"Good evening {name}", f"Good morning {name}", f"Good afternoon {name}",  f"Have fun learning new stuff {name}", f"Take a break whenever you need it {name}"]

#program starts
while True:
  Kexo = random.choice(KexoMessage)
  print(f"Kexo: {Kexo}!")
  KexoCmds = input("> ").strip().lower()

  print()

  if "help" in KexoCmds:
    print(f"""Kexo: Hey {name}! Here are the list of my commands that you can use:
1. Game
   > RPS (Clean Air)
   > RPG (Clean Air)
   > PopQuiz (Clean Air & Sustainable Lifestyle)
   > Stickman (Sustainable Lifestyle)
2. Fact
   > Interesting
3. Lesson
4. Japanese
5. Recycle
   > Quest
   > Inventory
   > Combine
6. To-Do
   > Create
   > Finish
   > All
   > *Category Name*
7. Update
8. Credits
9. Trophies\n""") 

  elif "game" in KexoCmds or "1" in KexoCmds:    
    print("Kexo: There's 3 games that you can pick from! I will explain the rules once you choose! (enter a number from 1-3!!)")
    print("""
1. PopQuiz 
2. Air rpg 
3. Tree, People, Carbondioxide
4. Stickman""")
  
    game_choice = input("> ")
    print()

    if game_choice == "1":
      KexoPOP()

    elif game_choice == "2":
      KexoRPG(name)

    elif game_choice == "3":
      KexoRPS()
    
    elif game_choice == "4":
      KexoStickFigure()

    else:
      print("Kexo: Oh silly! choose a number from 1-4. \n")

  elif "fact" in KexoCmds or "2" in KexoCmds:
    FactRun = True
    while FactRun:
      fact = ["The atmosphere is filled with 78% of nitrogen, 21% of oxygen, and 1% of other gasses", "Breathing in a large amount of carbondioxide or methane can be fatal", "We breathe in nitrogen but it actually doesn't react with our body", "Clean air will create stable environment for us and future generations", "Vehicles are 27% of total greenhouse gas emissions", "The US throws enough plastic bottles to encircle the earth 5 times", "Recycling a single 330 ml aluminium bottle has enough energy to power a TV for more than 3 hours.", "There are about 5.25 trillion micro and macro pieces of plastic in our ocean.", "There are about 46,000 pieces of plastic every square mile of ocean", "8 million pieces of plastic makes their way into the earth's ocean every day.", "There are about 1.4 billion tons of food wasted all over the world every year", "Food waste itself accounts for 8% of all emissions when it ends up in landfills", "The meat industry is one of the most destructive industries on the planet", "By growing your own food, you can be healtier, use less energy, and produce less food waste", "One's man trash can be another person's treasure, that's why if you don't need of a certain item you can donate them away instead of throwing it away"] #i placed this list here so that everything works in runtime instead of the user having to re run the program everytime for this feature to work.
  
      if not os.path.isfile("SaveFile/KexoFactBin.text"):
        with open("SaveFile/KexoFactBin.text", "w") as f: #creates this file if KexoFactBin.text wasn't found to prevent errors.
          pass
  
      with open("SaveFile/KexoFactBin.text", "r") as f:
        FactBin = f.readlines() 
  
      for KnowFact in FactBin:
        fact.remove(KnowFact.strip("\n")) #my idea here is so that Kexo won't pump out the same fact when the user already knows it
    
      try:
        random_fact = random.choice(fact)
      except IndexError:
        print("Kexo: Sorry! i got no more facts that i can tell you!")
        print("Kexo: Do you wanna reset your bin so you can see the facts again? (your interesting tabs won't be resetted) (y/n)") 
        
        KexoCmds = input("> ") #the user is given the choice to either reset the Bin file so the Kexo can give facts again or... not i guess 
        print()
  
        if KexoCmds == "y":
          os.remove("SaveFile/KexoFactBin.text")
          print("Kexo: Fact bin resetted! \n")
          continue
  
        else:
          continue
        
      print(f"Kexo: Okay i got my fact ready! {MessageContinue}")
      input()
   
      print(f"Kexo: Did you know: {random_fact}! \n'+' removes the fact (you will never see it again), '!' adds this to the interesting tab, alternatively, if you don't want to do anything with the fact just press enter.")
      
      KexoCmds = input("> ").strip().lower()
  
      if KexoCmds == "+":
        print("Kexo: Alright!\n")
        
        with open("SaveFile/KexoFactBin.text", "a") as f:
          f.write(f"{random_fact}\n") #stores the fact that the user already knows about
  
      elif KexoCmds == "!":
        if not os.path.isfile("SaveFile/KexoInterestingFact.text"):
          with open("SaveFile/KexoInterestingFact.text", "w") as f:
            f.write("")
          
        with open("SaveFile/KexoInterestingFact.text", "r") as f:
          InterestingFact = f.readlines()
  
        for Facts in InterestingFact:
          Facts = Facts.strip("\n")
          Fact.append(Facts)
          
        if random_fact in Fact:
          print("Kexo: You already have this fact pinned! \n")

        elif random_fact not in Fact:
          print("Kexo: Cool! you can see this fact whenever by typing in 'Interesting' in the menu! \n")
          with open("SaveFile/KexoInterestingFact.text", "a") as f:
            f.write(f"{random_fact}\n")

      FactContinue = input("Continue to the next fact (y/n)? > ")

      if FactContinue == "n":
        FactRun = False
        
      print()

  elif "interesting" in KexoCmds:
    if not os.path.isfile("SaveFile/KexoInterestingFact.text"):
      print("Kexo: You have no interesting facts yet!")
      continue

    with open("SaveFile/KexoInterestingFact.text", "r") as f:
      InterestingFact = f.readlines()

    for Facts in InterestingFact:
      print("- {}".format(Facts.strip("\n")))
    print()

  elif "lesson" in KexoCmds or "3" in KexoCmds:
    print("Kexo: Alright! booting up lessons..")
    print("""1. The Annoying Gasses.
2. How to Have a Sustainable Lifestyle""")
    LessonCmds = input("> ")

    if LessonCmds == "1":
      route_choice = random.randint(0,1) #decides the route of the user
      LessonArt(name, route_choice, red)

    elif LessonCmds == "2":
      LessonArt2(name, red)

    else:
      print("Kexo: That option doesn't exist or isn't available yet, don't worry you can try again! \n")

  elif "japanese" in KexoCmds or "4" in KexoCmds:
    print("""
        おはよう ございます！
___________________________________
|                                 |
|              `;,                |
|               ;;                |
|          `;;;;;;;;;;'           |
|               ;;     ,          |
|               ;;`''''';,        |
|             ,;`;  ,'   ;,       |
|            ;;  ;,'     ;;       |
|            `; ,'`;;   ,;        |
|              `       ,;         |
|_________________________________|\n""")

    KexoJP(name)

  elif "recycle" in KexoCmds or "5" in KexoCmds:
    KexoMachine(name)

  elif "to-do" in KexoCmds or "6" in KexoCmds:
    KexoDoList(name)
    
  elif "update" in KexoCmds or "7" in KexoCmds:
    print(f"""Kexo: Hey {name}! Here are the recent changes made to the program:
1. FILE DETECTION SYSTEM
   > Whenever the program is run, it'll scan if a file is missing or not. It will ask the user to download the program again from a given link and stop the program.
2. SAVE FILE ORGANIZED
   > To tidy things up, i've decided the save file containing texts and stuff will be placed in a folder where it can be easily accessable.
3. An update to the old feature regarding the sustainable lifestyle theme, to list all of them:
   > Added 10 new questions and a category section for POPQUIZ, one for clean air and one for the new category.
   > Added a bunch new facts with the new category.
   > Added a new lesson with the new category.
   > Added new japanese words for the new category.
4. Added 'update' as a new command, moved credits to the 6th sloth.
5. NEW COMMANDS! Full list:
   > Added 'To-do' List: Sort your list by category!
    -> NEW COMMANDS FOR THIS SECTION: create, finish, all.
   > Added 'stickman' as a guessing word game! (Sustainable Lifestyle related)
   > Added 'recycle', combine your garbage into something of a higher value!
6. SCAVENGER TRASH HUNT!!
   > Oh how dirty is this program! There's trashes left and right. Can you help Kexo pick up the trash? Kexo will tell you the location of one by claiming a quest in the recycle option!
7. TROPHIES!
   > Shiny trophies! gotta collect them all!!!\n""")

  elif "credits" in KexoCmds or "8" in KexoCmds:
    print(f"""-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-
{'-- SCRIPTER --': >35}
-> Sebastian, Christopher.

{'-- ASCII ARTIST --': >37}
-> Joan Stark - Mountain View
-> Steve Maddison - Small Village
-> Dan Furlani - Legendary Trash Bin
-> Elissa Potier - Tea

{'-- BUG FINDER/TESTER --': >40}
-> Raditya, Nicholas.
-> Widya, Chandra.

{'-- SPECIAL THANKS --': >38}
-> Kexo 
   > mascot of this whole project
-> https://emojicombos.com/oil-rig-ascii-art
   > helped convert a bunch of emojis into ascii art
-> https://patorjk.com/software/taag
   > helped convert a bunch of text into ascii art
-> https://www.asciiart.eu/
   > quite literally 50% of the used ascii arts here
-> YOU
   > for using this program ;)
-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-\n""")

  elif "trophies" in KexoCmds or "9" in KexoCmds:
    with open("SaveFile/KexoTrophy.text", "r") as f:
      Trophies = f.readlines()

    print("----- YOUR TROPHY COLLECTION -----")
    for Trophy in Trophies:
      print(Trophy.strip('\n'))
    
    print()

  if os.path.isfile("RecycleFit/KexoQuest.text"):
    with open("RecycleFit/KexoQuest.text", "r+") as r:
      Quest = r.readlines()

      if Quest != []:
        for content in Quest:
          content = content.split(", ")
        
        if KexoCmds == content[1] or KexoCmds == content[2]:
          print(f"Kexo: Congratulations! you found {content[0]}!")
          
          with open(f"RecycleFit/KexoGarbageCollect.text", "a") as f:
            f.write(f"{content[0]}\n")
          
          r.truncate(0)

else: #no commands found
    print("Kexo: Confused on what to do? type in 'help' to get a list of my commands!\n")