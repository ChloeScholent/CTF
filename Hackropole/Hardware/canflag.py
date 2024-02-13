import csv

ID = 6
Text = 7
Extended_Flag = 8

csv_file = "canflag.csv"

dico_ID_Text = {}

with open(csv_file) as csvfile:
    canflagreader = csv.reader(csvfile, quotechar='"')
    print(type(canflagreader))
    for ligne_sur_laquelle_je_travaille_actuellement in canflagreader:
        #print(row)
        ID_str = ligne_sur_laquelle_je_travaille_actuellement[ID]
        EXT_str = ligne_sur_laquelle_je_travaille_actuellement[Extended_Flag]
        Text_str = ligne_sur_laquelle_je_travaille_actuellement[Text]
        Index = int(ID_str[:2]) - eval(EXT_str)
    
        # Dans une liste [:2] pour sélectionner les éléments 0 et 1 de la liste (l'élément 2 est exclu).
        # Si rien avant : on part du début de la liste. Sous-liste = Liste[inclu:exclu]
        #fonction eval() pour exécuter un string comme expression python. eval("True") = True = 1
        
        dico_ID_Text[Index] = Text_str

flag = ""

#On commence à 1 car on travaille l'index d'un dico (1 à 67) et pas une liste. La dernière valeur (68) est exclue avec la fonction range()
for i in range(1,68):
    flag += dico_ID_Text[i]

print(flag)

