import colorama
from colorama import Fore

print("\n")
#Vraag om de pin code
pin = input("Geef hier de pin code: ")
print("\n")

#Zet de pin code los van elkaar
pin_list = [int(i) for i in str(pin)]

#geef de beginwaarde van de loop aan
list_item = 0

#De totale lengte van het pad
lengte = 0

# Ga door de list totdat alle items in de list zijn  geweest
while list_item + 1 < len(pin_list):

    #Dit is het nummer waar de stap vandaan wordt gezet
    begin = pin_list[list_item]

    #Dit is het nummer waar de stap eindigd
    eind = pin_list[list_item + 1]

    # Check of het begin en  eind cijfer even of oneven is en geef vervolgens de lengte van de stap
    if (begin % 2) == 0:
        if (eind % 2) == 0:
            lengte += 1.41213562
            richting = "schuin"

        else:
            lengte += 1.0
            richting = "recht"
    else:
        if(eind % 2) == 0:
            lengte += 1.0
            richting = "recht"

        else:
            lengte += 1.41213562
            richting = "schuin"


    print("De stap wordt gezet van: " + str(begin) + " naar " + str(eind) + ", deze stap gaat " + richting + "\n")


    #ga door naar de volgende item in de list
    list_item = list_item + 1

#Rond de lengte van het cijfer af
res = str(round(lengte, 2))
# print het eindresultaat
print(Fore.GREEN + "De lengte van de pin is: " + res + "\n")
print(Fore.WHITE)