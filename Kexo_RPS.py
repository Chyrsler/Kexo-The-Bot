import random

white = "\033[0;37m"
red = "\033[0;31m"

def KexoRPS():
  Kexo_Rigged = [["tree", "people"], ["people", "carbondioxide"], ["carbondioxide", "tree"]]
  Kexo_Caught = ["What!? i would never!!", "I play legit, i never cheat!", "I'm a not programmed to cheat, i swear!", "I must be lucky, i'm not cheating!", "Nah i just have Dream's luck i think", "you're probably just unlucky! i'm not cheating!"]
  
  print("Kexo: Let me explain the rules real quick, so this is something that resembles Rock Paper Scissors. You know that game right? here, the Tree beats Carbondioxide, the People beats the Tree, and Carbondioxide beats the People. It's fairly simple!")
  print(f"Kexo: Here's a special offer for ya, if you manage to beat me even once i'll give you {red}100$ (press enter to continue){white}")
  input()
  
  print(f"Kexo: By the way, if you want to quit the game just type {red}'quit'{white} below. You can quit at any moment")

  while True:
    caught = False #return it back to false.
    
    KexoRPS = input("> ").strip().lower()
    for advantage in ["unfair", "rigged", "cheat", "hack"]:
      if advantage in KexoRPS:
        Kexo_Message = random.choice(Kexo_Caught)
        print(f"Kexo: {Kexo_Message} \n")
        caught = True #detects that this part of the code has been activated.
        #NOTE: adding continue here won't work because it'll loop to the same piece of code over and over and then executes the code below (which is not what i want for it to do.)

    if caught: #if the above code is executed, then it'll start over.
      continue
  
    if KexoRPS == "":
      KexoRPS = random.choice(Kexo_Rigged[0])
      print("Kexo: You didn't pick anything, so i picked it for you!")
    
    for options in Kexo_Rigged:
      if KexoRPS[0] == options[0][0]:
        print(f"Kexo: i picked {options[1]}!, {options[1]} beats {options[0]}!! \n")
        continue
  
    if KexoRPS == "quit":
      break