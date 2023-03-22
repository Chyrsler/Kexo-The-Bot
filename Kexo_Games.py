import random

white = "\033[0;37m"
red = "\033[0;31m"
blue = "\033[0;34m"
cyan = "\033[0;94m"

def TrophyHandOut(TypeTrophy, Description):
   with open("SaveFile/KexoTrophy.text", "r") as f:
    trophies = f.readlines()

    boolean_check = []

    for content in trophies:
      boolean_check.append(TypeTrophy not in content)
      
    if False not in boolean_check:
      with open("SaveFile/KexoTrophy.text", "a") as f:
          f.write(Description)

def KexoPOP():
  Kexo_Air = [["the 2 particle that fills up most of the atmosphere is ________", "Nitrogen and Hydrogen", "Carbondioxide and Nitrogen", "Hydrogen and Oxygen", "Oxygen and Nitrogen"], ["one of the major bad effects of polluted air is ________", "global warming becomes a major concern", "people can live a healthy life", "people can make a quick buck out of it", "a downspike in disease cases"], ["25% of methane gas comes from ________", "enteric fermentation", "landfills", "manure management", "coal mining"], ["humans will experience ________ when breathing in small amounts of carbondioxide.", "little to no toxicological effect", "increased/decreased respiratory rate", "impaired conciousness", "convulsions"], ["photosynthesis is where carbondioxide will experience ________ and release the oxygen gas.", "reduction", "morphology", "oxidation", "photosynthesis"], ["one of the effort to reduce air pollution is by ________", "reduce wildfire", "use plastic bags", "using an air conditioner instead of a fan", "using a private vehicle"], ["the glass house effect is mainly caused by ________", "water vapour, carbondioxide, nitrous oxide", "water vapour, nitrogen, oxygen", "carbondioxide, nitrous oxide, oxygen", "oxygen, nitrogen, carbondioxide"], ["the greenhouse effect says that ________ due to greenhouse gasses such as carbondioxide and methane gas.", "some of the heat is reflected back to earth", "all of the heat is reflected to space", "all of the heat is reflected back to earth", "all of the heat is trapped in earth", "there are so many positives in breathing in clean air, but the exact opposite effect if you breathe in polluted air is ________", "decrease in sleep quality, less productivity at work, shorter life", "less productivity at work, shorter life, stable environment", "weaker immune system", "productivity at work, unstable environment", "longer life, improving sleep quality, reduction of sick and leave, and greater comfort in general"], ["carbondioxide's mass production comes from ________", "fossil fuels", "land use", "industrial processes", "other raw materials"]] #all the correct answers will be placed at index one (to ease the coding process), though it'll be randomized when printed out to the user.
  Kexo_Sustainable = [["To sustain a stable lifestyle we'll need to ________", "reduce meat-eating", "not throw plastics to our ocean", "waste food", "eat unhealthy"], ["approximately ________ million plastics are produced every year.", "380", "300", "460", "600"], ["________ percent of all produced plastic every year are single use.", "50", "30", "20", "40"], ["when we throw out old electronics, they can kill wildlife because ________", "they contain toxins that can leak", "the animals think that it's food and they'll eat it", "they don't really harm or kill wildlife so it's none of them", "they produce carbondioxide which can ruin the surrounding environment"], ["There are many ways to stop food wasting but not like ________", "throwing your newly fresh mcdonalds out the trash", "start your own garden", "start donating food to other people", "recycle old electronics"], ["let's say you love meat, but you heard that the meat industry is very destructive. So you in this situation will need to ________", "reduce eating it", "TURN VEGAN!!", "eat it artificially", "stop eating it fully"], ["so you don't have to keep renewing your product, you'll need to check it's durability by ________", "checking what brand made that product", "smashing it as hard as you can to the ground", "ask the store's clerk on when it was made", "check the price tag of the item, the more expensive the more durable"], ["There are a lot of eco-friendly products, such as ________", "coffee cups", "plastic cups", "helium balloons", "all plastic-related items basically"], ["starting our own garden reduces food waste beecause ________", "we tend to not throw away food that is grown by ourselves", "they don't really reduce food waste because we're only making more food", "we know how we process the food", "we know whether they're clean or not because we'll be the one growing them"], ["brands that prioritize on producing energy-saving appliances are called ________", "Energy Star appliances", "Samsung", "ASKO", "Bosch"], ["Sustainable Lifestyle is ________", "a way to get reduce of one's carbon footprint", "a way to keep yourself healthy", "a way to adapt to your surroundings", "a way to stay unhealthy"]]
  Used_Numbers = [] #Indexes that are used will go here to prevent doubles.
  Correct = 0 #how many questions have been answered correctly.
  Points = 0 #how many points have been awarded.
  Answered_Questions = 0 #how many questions have been answered.
  
  print("Kexo: So here's the rules! you'll need to answer about 5 questions before the round ends! Each questions are worth 20 points, your final grade is the sum of all the correct answers! (press enter to continue)") 
  input()
  print("""Kexo: Go ahead! pick a category (1 or 2)
1. Clean air (Hard)
2. Sustainable lifestyle (Easy)""")
  ChosenCategory = input("> ")

  Kexo_Question = Kexo_Air if ChosenCategory == "1" else Kexo_Sustainable

  while True:
    Amount = len(Kexo_Question) - 1
    Rotation = 0 #count how many questions has been printed out to the user (see how it works below.)
    
    Random_Question = random.randint(0, Amount)
    Chosen = Kexo_Question[Random_Question]
    
    print(f"Kexo: {Chosen[0]}")
    
    while True: #Randomising the 4 options
      index = random.randint(1,4)
  
      if index not in Used_Numbers:
        Rotation += 1
        Used_Numbers.append(index)
        print(f"{Rotation}. {Chosen[index]}")

        if index == 1:
          Chosen.append(Rotation)
  
      if Rotation == 4:
        Used_Numbers.clear()
        break
        
    KexoAnswer = input("> ")
    Answered_Questions += 1
        
    if KexoAnswer == str(Chosen[len(Chosen) - 1]):
      Correct += 1
      Points += 20

    if Answered_Questions == 5:
      print(f"Kexo: You got {Correct} out of 5 correct answers! That's a {Points}/100!")

      TrophyHandOut("GameShow Trophy", "The GameShow Trophy, 'Regardless on your performance, you'll get this shiny trophy!'. Achieved by completing a PopQuiz session.\n")
      
      input("Press enter to quit")
      break
      
    Kexo_Question.pop(Random_Question)
    print()

def KexoRPG(name):
  Enemy = ["Random smoke particle", "Carbon dioxide", "Fossil Fuel", "Nicotine", "Carbon monoxide", "Methane"]
  RandomEnemy = f"{red}{random.choice(Enemy)}{white}"
  Enemy_Health = random.randint(30,50)
  UserHealth = 100

  print(f"Kexo: Alright, this one's pretty simple. You either defend or attack. It is luck based though so beware {red}(press enter to continue){white}")
  input()

  print(f"Kexo: Alright, you're going up against a {RandomEnemy}?? \n")

  while True:
    print(f"> {name}'s' HP: {UserHealth}    |    > {RandomEnemy}'s HP: {Enemy_Health}")
    print(f"""____________________________________
| > What are you gonna do??        |
| 1. {red}FIGHT IT!!!{white}                   |
| 2. {cyan}DEFEND (IT GOT A WEAPON!!){white}    |
|__________________________________|""")
    KexoInput = input("> ").strip().lower()
    print()

    if KexoInput == "attack" or KexoInput == "1":
      attack = random.randint(1,20)
      print(f"Kexo: Looks like {name} attacked {RandomEnemy} and dealt {attack} damage!")

      Enemy_Health -= attack

      if Enemy_Health <= 0:
        print(f"Kexo: looks like {name} has won the battle!\n")

        TrophyHandOut("The Winner's Trophy", "The Winner's Trophy, 'You won, agains't a particle?'. Achieved by defeating an enemy in RPG.\n")

        input("Press enter to quit")
        break
        
    elif KexoInput == "defend" or KexoInput == "2":
      defend = random.randint(1,20)
      print(f"Kexo: Looks like {name} defended and gained {defend} HP!")
      UserHealth += defend #not gonna cap the user's health at 200 unlike the enemy since they're in a disadvantage

    else:
      continue

    EnemyChoice = random.choice(["defend", "attack"])
    
    if EnemyChoice == "attack":
      attack = random.randint(10,30)
      print(f"Kexo: Looks like {RandomEnemy} attacked {name} and dealt {attack} damage!")
      UserHealth -= attack

      if UserHealth <= 0:
        print(f"Kexo: looks like {RandomEnemy} has won the battle!\n")
        input("(Press enter to quit)")
        break

    elif EnemyChoice == "defend":
      defend = random.randint(10,30)
      print(f"Kexo: Looks like {RandomEnemy} defended and gained {defend} HP!")

      if Enemy_Health < 200:
        Enemy_Health += defend
      else:
        Enemy_Health = 200

    print()

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

def KexoStickFigure():
  print("Kexo: Here's the rule: you'll need to guess your way to victory. Each round the word is different and it's related to sustainable lifestyle. Don't worry! you have infinite lives for the purpose of learning new words!")
  KexoListWord = [["recycle", "Ah yes, the process to repurpose your old junk and use it to make newly produce materials."], ["garden", "Building your own garden may take time, but it can be worth the wait!"], ["reforestration", "Come on people stop killing the earth's resources for your own greedy need, is it that hard?"], ["ecofriendly", "Environmentally friendly, nothing to say about this one really pretty self explanatory."], ["reuse", "Essentially like recycling, there's not much of a difference."], ["protect", "Protect as in protect the flaura and fauna of the earth."], ["sustainable", "Sebastian was really thinking hard about putting this one in, alas he was forced to. Atleast it has some kind of connection with sustainable lifestyle, eh.. word-wise."]]
  
  KexoIndex = random.randint(0, len(KexoListWord) - 1)
  KexoChosenWord = KexoListWord[KexoIndex][0]
  KexoWordDialogue = KexoListWord[KexoIndex][1]

  GuessWord = []
  BlatantlyWrong = []

  for char in KexoChosenWord:
    GuessWord.append(char)
  
  KexoAnonymousChar = GuessWord.copy()
  for i in range(len(KexoAnonymousChar)):
    KexoAnonymousChar[i] = "_"
  
  while True:
    for characters in KexoAnonymousChar:
      print(characters, end=" ")

    print("\n")
    KexoWordGuessing = input("> ")

    for i in range(len(GuessWord)):
      for char in KexoWordGuessing:
        if char == GuessWord[i]:
          KexoAnonymousChar[i] =  char

        if char not in GuessWord:
          if char not in BlatantlyWrong:
            BlatantlyWrong.append(char)
    
    print("Used wrong alphabets: ", end="")
    for char in BlatantlyWrong:
      print(char, end=", ")
    print()

    if KexoAnonymousChar == GuessWord:
      print(f"Kexo: {KexoWordDialogue}")
      print(f"Kexo: Good job! you've won the game! You've entered {len(BlatantlyWrong)} wrong characters in total!\n")

      TrophyHandOut("The Stick Trophy", "The Stick Trophy, 'Quite literally made out of sticks'. Achieved by correctly guessing the word in stickman.\n")
      break