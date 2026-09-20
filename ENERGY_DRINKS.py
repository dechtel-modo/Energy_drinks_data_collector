
import json as js
import os

# reading drinks list
d ={}
with open("ENERGY_DRINKS.json",'r') as file :
  try:
    d = js.load(file)
  except js.JSONDecodeError :
    print("List is Empty")
# reading text words that are separated by a space
def words(TXT) :
  word = ""
  list_words= []
  TEXT = TXT.strip()
  TEXT += " "

  for i in  TEXT :
    if i == " " and word != "":
      list_words.append(word)
      word = ""
    else :
      word += i
  return list_words


while True :
  # data analyzing main variables
  command = str(input("–@– "))
  commands= words(command)
  length = len(commands)

  #print(command,"::",commands,"::",length) # test

  if length > 2 :
    print("A lot of Words")

  elif length == 2 and commands[0] == "list" :
    name_drink = commands[1].capitalize()
    if name_drink in d :
      name = d[name_drink]
      
      print(f"Taurine : {name["Taurine"]}")
      print(f"Inositol : {name["Inositol"]}")
      print(f"Caffeine : {name["Caffeine"]}")
      print(f"Total  Taurine : {name["Total Taurine"]}")
      print(f"Total  Inositol : {name["Total Inositol"]}")
      print(f"Total  Caffeine : {name["Total Caffeine"]}")
      print(f"Total Can Size : {name["Total Size"]}")
    else:
      print(f"{commands[1].capitalize()} is not in the list")

  elif length == 1 and commands[0] == "new":
    NAME = str(input("drink name : ")).capitalize()
    try :
      if NAME in d :
        print(f"{NAME} drink in the list")
        print("by continueing you're updating the drink ")
        if str(input("q to quit enter to resume : ")) == "q" :
          exit()  # noqa: PLR1722



      taurine = float(input("Taurine Per 100mL : "))
      inositol = float(input("Inositol Per 100mL : "))
      caffeine = float(input("Caffeine Per 100mL : "))
      total_size = int(input("Total Can Size : "))

    except KeyboardInterrupt :
      exit()  # noqa: PLR1722

    except ValueError :
      print("Enter Valid Values")

  elif length == 1 and commands[0] in ["q","Q","Quit","quit","QUIT"] :
    print("We are QUITTING")
    exit()  # noqa: PLR1722

  elif length == 1 and commands[0] == "save" :
    with open("ENERGY_DRINKS.json","w") as file :
      try:
        factor = total_size / 100
        d[NAME]={"Taurine":taurine,
        "Inositol":inositol,
        "Caffeine" : caffeine,
        "Total Size":total_size,
        "Total Taurine":taurine*factor,
        "Total Inositol":inositol*factor,
        "Total Caffeine":caffeine*factor}
      except NameError :
        pass
      print("saving")
      js.dump(d,file,indent=2)

  elif length == 2 and commands[0] in ["del","delete","remove","rm"] :
    if commands[1].capitalize() in d :

      d.pop(commands[1].capitalize())
    else :
      print(f"{commands[1].capitalize()} Is NOT In The List")
  elif length == 1 and commands[0] == "backup":
    with open("BACKUP.json","w") as BACKUP:
        js.dump(d,BACKUP,indent=2)
  elif length == 1 and commands[0] == "clear" :
    os.system("clear"if os.name == "posix" else "cls")
  else :
    print("wrong command")
