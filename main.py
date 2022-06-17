# This is a sample Python script.

#salle = [[1]*places]*row
salle=[]

def init_salle(row=8, places=9):    #default paramater: row=8, place=9
    for i in range(row):
        list=[]
        for j in range(places):
            list.append(1)
        salle.append(list)


def print_salle(salle):
    print("\n")
    print("------------------------------------------------------------\n")
    for index, row in enumerate(salle):
        print(index, "|", end=" ")
        for place in row:
            if place == 0 : print('[ x ]', end=" ")
            else : print('[ _ ]', end=" ")
        print('\n')
    places= len(salle[0])  #get places number
    for n in range(places) :
        space = 5 if n==0 else 4
        print(" "*space, n, end="")
    print("\n")


def check(number_place, range_number):
    if salle[range_number].count(1) == 0:
        return -1
    elif salle[range_number].count(1) < number_place :
        return 0
    else:
        return 1


def reservation(number_place, range_number):
    index = salle[range_number].index(1)
    for n in range(number_place):
        salle[range_number][index+n] = 0


if __name__ == '__main__':
    init_salle()
    while(True):
        try :
            number_place = int(input("Combien de place voulez-vous acheter ? \n"))
            range_number = int(input("A quelle rangé voulez-vous aller ? \n"))
        except ValueError:
            print("Veuillez entrer un nombre entier.")
            continue
        status = check(number_place, range_number)
        if status == -1 :
            print("Il n'y a plus de place dans la rangé veuillez choisir une autre rangé")
        elif status == 0:
                print("Il n'y pas assez de place dans la rangé veuillez choisir une autre rangé")
        else:
            reservation(number_place, range_number)
            print_salle(salle)
