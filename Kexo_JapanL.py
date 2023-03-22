import random

def Word_Gen(Mode, name, Word_Type="clean"): #Romaji/Definition, clean is set as default. 
  #list of words
  Words_sustainable = [["リサイクル (るさいくる)", "rusaikuru", "recycle"], ["しょくひん はいき もの", "shokuhin haiki mono", "food waste"], ["じぞく かのうな ライフスタイル (らいふすたいる)", "Jizoku kanouna raifusutairu", "sustainable lifestyle"], ["しょうえね", "shoune", "energy saving"], ["プラスチック (ぷらしちっく)", "purasuchikku", "plastic"], ["えんげい", "engei", "gardening"], ["けんこう たべる", "kenkou taberu", "eat healthy"], ["かんきょう に やさしい", "kankyou ni yasashii", "enviromentally friendly"], ["はいき もの ぜろ", "haiki mono zero", "zero waste"], ["ペットボトル (ぺっとぼとる)", "pettobotoru", "plastic bottle"], ["やさい", "yasai", "vegetables"], ["さい りよう かのう", "sai riyou kanou", "reusable"]]
  Words_air = [["くうき", "kuuki", "air"], ["きれいな くうき", "kireina kuuki", "clean air"], ["たんそ", "tanso", "carbon"], ["ほうしゅつ", "houshutsu", "emission"], ["メタン (めたん)", "metan", "methane"], ["おんしつ こうか がす", "onshitsu kouka gasu", "greenhouse gas"], ["ガス (がす)", "gasu", "gas"], ["たいき おせん", "taiki osen", "air pollution"], ["にさんかたんそ", "nisankatanso", "carbondioxide"], ["すいそ", "suiso", "hydrogen"], ["ちきゅう おんだんか", "chikyuu ondanka", "global warming"], ["かせき ねんりょう", "kaseki nenryou", "fossil fuel"], ["ソーラーパネル (そおらあぱねる)", "sooraapaneru", "solar panel"], ["てんねん がす", "tennen gasu", "natural gas"], ["やま かじ", "yama kaji", "forest fire"], ["ちっそ", "chisso", "nitrogen"]]
  Correct = 0

  #chosen word category
  Words = Words_air

  if Word_Type == "sustainable":
    Words = Words_sustainable
  
  #program starts
  for i in range(10):
    Random_Word = random.randint(0, len(Words) - 1)
    Chosen_Word = Words[Random_Word][0] 
    Romaji = Words[Random_Word][1]
    Definition = Words[Random_Word][2]

    if Mode == "definition":
      print("LIST OF WORDS: | ", end="")
      
      for i in range(len(Words)):
        print(Words[i][2], end=" | ")
      print()
    
    print(f"Kexo: Alright, what is the {Mode} of {Chosen_Word}?")
    User_Word = input("> ").lower().strip()

    if Mode == "romaji":
      if User_Word == Romaji:
        print(f"Kexo: Good job {name}, the definition of it is {Definition}!")
        Correct += 1
      else:
        print(f"Kexo: Sorry {name}, the answer is actually {Romaji}.")

    elif Mode == "definition":     
      if User_Word == Definition:
        print(f"Kexo: Nicely done {name}, of course it is {Romaji} if written in romaji.")
        Correct += 1
      else:
        print(f"Kexo: The answer is actually {Definition}, sorry {name}.")
      
    Words.pop(Random_Word)
    print()

  print(f"Kexo: Congratulations on beating with {Correct}/10 corrects, {name}!")

def KexoJP(name):
  #list of kana
  Hiragana = [[["あ", "a"], ["い", "i"], ["う", "u"], ["え", "e"], ["お", "o"]], [["か", "ka"], ["き", "ki"], ["く", "ku"], ["け", "ke"], ["こ", "ko"]], [["さ", "sa"], ["し", "shi"], ["す", "su"], ["せ","se"], ["そ", "so"]], [["た", "ta"], ["ち", "chi"], ["つ", "tsu"], ["て", "te"], ["と", "to"]], [["な", "na"], ["に", "ni"], ["ぬ", "nu"], ["ね", "ne"], ["の", "no"]], [["は", "ha"], ["ひ", "hi"], ["ふ", "fu"], ["へ", "he"], ["ほ", "ho"]], [["ま", "ma"], ["み", "mi"], ["む", "mu"], ["め", "me"], ["も", "mo"]],  [["ら", "ra"], ["り", "ri"], ["る", "ru"],["れ", "re"], ["ろ", "ro"]], [["や", "ya"], ["ゆ", "yu"], ["よ", "yo"], ["わ", "wa"], ["を", "wo"], ["ん", "n"]]] #these characters are grouped in 3d arrays. For example, 'か' is grouped with 'ka' (which is the romaji) which is grouped with the 'k' family. This is done so that the user can study hiragana in order.
  Hiragana_small = [[["き", "k"], ["に", "n"], ["ひ", "h"], ["み", "m"], ["り", "r"]], [["ゃ", "ya"], ["ゅ", "yu"], ["ょ", "yo"]]] #i only placed them in their initials because they will be combined with the second group (the smaller versions of ya yu yo), for example 'きゅ' is read as 'kyu'
  
  KanaToHiragana = f"A word in japanese hiragana will be shown and you will be asked to translate it to romaji. I'll tell you the definition of it after you answer! Are you ready {name}? (press enter to continue)"
  KanaDefinition = f"A word in japanese hiragana will be shown and you will be asked to translate it in english. Are you ready {name}? (press enter to continue)"

  print(f"Kexo: There isn't much going on here, i'll teach you some vocabularies that are associated with clean air in japanese. However {name}, have you ever learnt hiragana? We're not gonna use katakana nor kanji for now. If you haven't learned hiragana before i can teach you!")
  print("""
1. No i have never learnt hiragana.
2. Yes i have learnt hiragana before.""")
  
  user = input("> ").strip()
  
  if user == "1":
    print()
    print("""Kexo: There are multiple lessons in this part, you can pick where you want to start from:
1. Hiragana introduction
2. Small Kana""")
    user_lesson = input("> ").lower().strip()

    if user_lesson not in ["1", "2"]:
      user_lesson = "1" #auto picks if the user chooses none.

    print()
    
    if user_lesson == "1":
      print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")
      print("Kexo: Alright! i'll teach you from a-i-u-e-o and ending in wa-wo. After each lesson i'll ask you which is which and you'll need to answer them correctly! Goodluck!!")
      part = -1
      
      while True:
        print()
        part += 1
  
        if part == len(Hiragana): #this means the user has completed the exercise, running the rest of the code will break because there are no more than 9 groups in the list.
          break
  
        for i in range(len(Hiragana[part])):
          print(f"{Hiragana[part][i][0]} is {Hiragana[part][i][1]}")
    
        print("(enter if you're ready..)")
        input()
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    
        for i in range(len(Hiragana[part])):
          Hiragana_int = random.randint(0, len(Hiragana[part]) - 1)
          Random_Hiragana = Hiragana[part][Hiragana_int][0]
          Hiragana_answer = Hiragana[part][Hiragana_int][1]
  
          print(f"Kexo: What is {Random_Hiragana}?")
          user_answer = input("> ").lower().strip()
  
          if user_answer == Hiragana_answer:
            print(f"Kexo: That is correct, good job {name}!")
          else:
            print(f"Kexo: Ehh the answer is '{Hiragana_answer}', sorry {name}..")
            
          Hiragana[part].pop(Hiragana_int)

        user_lesson = "2" #moves the user into the next lesson.
          
    if user_lesson == "2": #had to use 'if' instead of 'elif' so if the user came from lesson 1 they can head straight into the next lesson.
      print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")
      print("Kexo: Moving on to the next lesson.")
      print("Kexo: So there are these things called 'small kana'. Remember the 'ya', 'yu', and 'yo'? Well they can be decreased in size and then matched with another kana that ends with an 'i' so for example ひ (hi) + ゃ(ya) -> ひゃ is read as 'hya'. Notice the size difference to the normal ya 'や'. (press enter to continue)")
      input()

      print("Kexo: However, 'し' and 'ち' is different, since they're 3 characters in romaji (shi and chi), when combined with a small kana the only thing that gets replaced is the end character. Example: しょ is read as 'cho' NOT 'chyo'")
  
      for i in range(len(Hiragana_small[0])):
        Kana_int = random.randint(0, len(Hiragana_small[0]) - 1)
        Random_Kana = Hiragana_small[0][Kana_int][0] #the first is group 0 (which is the groups of Kana), the second one is randomized between the 5 existing kana that is in the group and the 3rd one is the kana itself
        Kana_Answer = Hiragana_small[0][Kana_int][1]
  
        Small_int = random.randint(0,2) #picking the index of the small kana, it is guaranteed to be 0-2 because none of them are gonna be deleted/removed.
        Random_SmallKana = Hiragana_small[1][Small_int][0]
        SmallKana_Answer = Hiragana_small[1][Small_int][1]
  
        print(f"Kexo: What is {Random_Kana}{Random_SmallKana} in romaji?")
        user_answer = input("> ").lower().strip()
  
        if f"{Kana_Answer}{SmallKana_Answer}" in user_answer:
          print(f"Kexo: Great job {name}! you got that one correct!")
        else:
          print(f"Kexo: Sorry {name} the answer is {Kana_Answer}{SmallKana_Answer}")
  
        Hiragana_small[0].pop(Kana_int)
        print()
        
    print(f"Kexo: Congratulations {name}, on completing the Hiragana tutorial! \n")
            
  elif user == "2":    
    print("Kexo: Alright! looks like we're jumping straight to the material. There's currently 4 modes, each one has 10 questions you'll need to answer, goodluck!")
    print("""
1. Define a hiragana to romaji - Clean Air
2. Define a hiragana into it's actual meaning in english - Clean Air

3. Define a hiragana to romaji - Sustainable Lifestyle
4. Define a hiragana into it's actual meaning in english - Sustainable Lifestyle""")
    Japan_Mode = input("> ").strip()

    print()

    if Japan_Mode == "1":
      print(KanaToHiragana)
      input()
      
      Word_Gen("romaji", name)

    elif Japan_Mode == "2":
      print(KanaDefinition)

      Word_Gen("definition", name)

    elif Japan_Mode == "3":
      print(KanaToHiragana)
      input()

      Word_Gen("romaji", name, "sustainable")

    elif Japan_Mode == "4":
      print(KanaDefinition)
      input()
      
      Word_Gen("definition", name, "sustainable")

    with open("SaveFile/KexoTrophy.text", "r") as f:
      trophies = f.readlines()

      boolean_check = []

      for content in trophies:
        boolean_check.append("The Origami Trophy" not in content)
        
      if False not in boolean_check:
        with open("SaveFile/KexoTrophy.text", "a") as f:
            f.write("The Origami Trophy, 'It's folded like an origami but shaped like a trophy!'. Achieved by doing any exercise in Japanese.\n")
            
  else:
    print("Kexo: Come again later! \n")