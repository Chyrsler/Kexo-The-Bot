#Other frequently commands used throughout the files will be placed in this file

import os

def TrophyHandOut(TypeTrophy, Description):
   with open("SaveFile/KexoTrophy.text", "r") as f:
    trophies = f.readlines()

    boolean_check = []

    for content in trophies:
      boolean_check.append(TypeTrophy not in content)
      
    if False not in boolean_check:
      with open("SaveFile/KexoTrophy.text", "a") as f:
          f.write(Description)