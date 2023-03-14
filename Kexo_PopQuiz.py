import random

def KexoPOP():
  Kexo_Question = [["the 2 particle that fills up most of the atmosphere is ________", "Nitrogen and Hydrogen", "Carbondioxide and Nitrogen", "Hydrogen and Oxygen", "Oxygen and Nitrogen"], ["one of the major bad effects of polluted air is ________", "global warming becomes a major concern", "people can live a healthy life", "people can make a quick buck out of it", "a downspike in disease cases"], ["25% of methane gas comes from ________", "enteric fermentation", "landfills", "manure management", "coal mining"], ["humans will experience ________ when breathing in small amounts of carbondioxide.", "little to no toxicological effect", "increased/decreased respiratory rate", "impaired conciousness", "convulsions"], ["photosynthesis is where carbondioxide will experience ________ and release the oxygen gas.", "reduction", "morphology", "oxidation", "photosynthesis"], ["one of the effort to reduce air pollution is by ________", "reduce wildfire", "use plastic bags", "using an air conditioner instead of a fan", "using a private vehicle"], ["the glass house effect is mainly caused by ________", "water vapour, carbondioxide, nitrous oxide", "water vapour, nitrogen, oxygen", "carbondioxide, nitrous oxide, oxygen", "oxygen, nitrogen, carbondioxide"], ["the greenhouse effect says that ________ due to greenhouse gasses such as carbondioxide and methane gas.", "some of the heat is reflected back to earth", "all of the heat is reflected to space", "all of the heat is reflected back to earth", "all of the heat is trapped in earth", "there are so many positives in breathing in clean air, but the exact opposite effect if you breathe in polluted air is ________", "decrease in sleep quality, less productivity at work, shorter life", "less productivity at work, shorter life, stable environment", "weaker immune system", "productivity at work, unstable environment", "longer life, improving sleep quality, reduction of sick and leave, and greater comfort in general"], ["carbondioxide's mass production comes from ________", "fossil fuels", "land use", "industrial processes", "other raw materials"]] #all the correct answers will be placed at index one (to ease the coding process), though it'll be randomized when printed out to the user.
  Used_Numbers = [] #Indexes that are used will go here to prevent doubles.
  Correct = 0 #how many questions have been answered correctly.
  Points = 0 #how many points have been awarded.
  Answered_Questions = 0 #how many questions have been answered.
  
  print("Kexo: So here's the rules! you'll need to answer about 5 questions before the round ends! Each questions are worth 20 points, your final grade is the sum of all the correct answers! goodluck! (press enter to continue)")
  input()

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
      input("Press enter to quit")
      break
      
    Kexo_Question.pop(Random_Question)
    print()