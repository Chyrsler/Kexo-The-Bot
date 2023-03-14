#Submission for Code Olympiad, made by Christopher Sebastian H.
#Submission Date: -- UNFINISHED --

#I tried placing as many notes as possible on how certain code blocks work.

import os, random
from Kexo_PopQuiz import KexoPOP
from Kexo_RPS import KexoRPS
from Kexo_RPG import KexoRPG
from Kexo_Lesson1 import LessonArt
from Kexo_JapanL import KexoJP

white = "\033[0;37m"
red = "\033[0;31m"
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
  with open("SaveFile/KexoIntroduction.text", "a") as f:
    f.write(name)
  
  print(f"Kexo: {name} huh? what a wonderful name! i'll start calling you that from now on!")
  print(f"Kexo: {name}, to get started, type in {red}'help'{white} below and see the list of my commands! \n")

#If KexoIntroduction.text exist then the user skips the introduction.

with open("SaveFile/KexoIntroduction.text", "r") as f:
  name = f.read().capitalize() #get the name of the user

KexoMessage = [f"Hello {name}", "Need a list of my commands? type in 'help' below", f"Good evening {name}", f"Good morning {name}", f"Good afternoon {name}"]

while True:
  Kexo = random.choice(KexoMessage)
  print(f"Kexo: {Kexo}!")
  KexoCmds = input("> ").strip().lower()

  print()

  if "help" in KexoCmds:
    print(f"""Kexo: Hey {name}! Here are the list of my commands that you can use:
1. Game
   > RPS
   > RPG
   > PopQuiz
2. Fact
   > Interesting
3. Lesson
4. Japanese
5. Credits\n""") 

  elif "game" in KexoCmds or "1" in KexoCmds:    
    print("Kexo: There's 3 games that you can pick from! I will explain the rules once you choose! (enter a number from 1-3!!)")
    print("""
1. PopQuiz 
2. Air rpg 
3. Tree, People, Carbondioxide""")
  
    game_choice = input("> ")
    print()

    if game_choice == "1":
      KexoPOP()

    elif game_choice == "2":
      KexoRPG(name)

    elif game_choice == "3":
      KexoRPS()

    else:
      print("Kexo: Oh silly! choose a number from 1-3. \n")

  elif "fact" in KexoCmds or "2" in KexoCmds:
    FactRun = True
    while FactRun:
      fact = ["The atmosphere is filled with 78% of nitrogen, 21% of oxygen, and 1% of other gasses", "Breathing in a large amount of carbondioxide or methane can be fatal", "We breathe in nitrogen but it actually doesn't react with our body", "Clean air will create stable environment for us and future generations", "Vehicles are 27% of total greenhouse gas emissions"] #i placed this list here so that everything works in runtime instead of the user having to re run the program everytime for this feature to work.
  
      if not os.path.isfile("SaveFile/KexoFactBin.text"):
        with open("SaveFile/KexoFactBin.text", "w") as f: #creates this file if KexoFactBin.text wasn't found to prevent errors.
          f.write("")
  
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
    print("1. The Annoying Gasses.")
    LessonCmds = input("> ")

    if LessonCmds == "1":
      print("Kexo: NUMBER 1 CHOSEN..")
      
      route_choice = random.randint(0,1) #decides the route of the user
      LessonArt(name, route_choice, red)

    else:
      print("Kexo: Oh i guess you didn't want to choose, that's okay! maybe next time! \n")

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
    
  elif "credits" in KexoCmds or "5" in KexoCmds:
    print(f"""-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-
{'-- SCRIPTER --': >35}
-> Sebastian, Christopher.

{'-- ASCII ARTIST --': >37}
-> Joan Stark - Mountain View
-> Steve Maddison - Small Village

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
-> YOU
   > for using this program ;)
-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-\n""")

  else:
    print("Kexo: Confused on what to do? type in 'help' to get a list of my commands!\n")