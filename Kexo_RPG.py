import random

white = "\033[0;37m"
red = "\033[0;31m"
blue = "\033[0;34m"
cyan = "\033[0;94m"

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