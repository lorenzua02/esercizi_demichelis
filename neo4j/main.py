from stagemodel import Neo4jModel as n4j
import os
import menu

db = n4j("bolt://localhost:7687", "", "")
print(f"Cancellati {db.empty_database()} nodi.")

while True:
    os.system("cls")
    print('[Menu]\n\n|[1]| Crea nodo\n|[2]| Crea relazione\n|[3]| Cancella nodo\n|[4]| Cancella relazione\n|[5]| Cerca il miglior prof\n|[6]| Cancella il database\n|[9]| Esci\n')
    option = input("Inserisci scelta: ")

    try:
        option = int(option)
    except:
        # Scelta non presente
        option = -1

    if option == 9:
        input("adios")
        os.system("cls")
        break

    elif option not in [x for x in range(0, 6)]:
        print("Scelta non presente")
        input("Premi un tasto per continuare")
        continue

    elif option == 1:
        os.system("cls")
        print('[Menu -> Crea nodo]\n\n|[1]| Crea Alunno\n|[2]| Crea Professore\n|[3]| Crea Azienda\n|[9]| Torna indietro\n')
        option_create_node = input("Inserisci scelta: ")
        try:
            option_create_node = int(option_create_node)
        except:
            # Scelta non presente
            option_create_node = -1
        if option_create_node == 9:
            option = 0
            option_create_node = 0

        elif option_create_node == 1:
            print("Alunno")
            # Funzione Create Alunno
            input("Continua...")

        elif option_create_node == 2:
            print("Professore")
            # Funzione Create Professore
            input("Continua...")

        elif option_create_node == 3:
            print("Azienda")
            # Funzione Create Azineda
            input("Continua...")

    elif option == 2:
        continue
    elif option == 3:
        continue
    elif option == 4:
        continue
    elif option == 5:
        continue
    elif option == 6:
        n4j.empty_database()
    else:
        continue

menu.main_menu()
db.close()