'''Task 0: Import the modules csv and random'''
import csv,random

def startup():    
    """
    Task 1: Display an entry message.

    The message should consist of the name of your application centered in the middle of the console.

    :return: Does not return anything.
    """
    print("\t\t\t\t\tWelcome to Pokemon App")


def options():
    """
    Task 2: Display a menu of options and read the user's response.

    A menu consisting of the following options should be displayed:
    'Check your Pokemon', 'Add a new Pokemon', 'Show all Pokemon', 'Visualise' ,'Save your Pokedex' and 'Exit'

    :return: None if invalid selection otherwise an integer corresponding to a valid selection
    """
    print("Choose one option from menu by typing a number:\n1-Check your Pokemon\n2-Add a new Pokemon\n3-Show all Pokemon\n4-Visualise\n5-save your Pokedex\n6-Exit")
    response = int(input())
    if response in [1,2,3,4,5,6]:
        return response


def check_poke():
    """
    Task 3: Display a menu of options for how a Pokemon should be searched. Read in the user's response.

    A menu should be displayed that contains the following options:
        'By name', 'By type'

    :return: None if an invalid selection made otherwise an integer corresponding to a valid option
    """
    print("Choose one option from menu by typing a number:\n1-By name\n2-By type\n")
    response = int(input())
    if response in [1,2]:
        return response


def add_poke():
    """
    Task 4: Display a menu of options for how a Pokemon should be added. Read in the user's response.

    A menu should be displayed that contains the following options:
        'Add specific', 'Add at random'

    :return: None if an invalid selection made otherwise an integer corresponding to a valid option

    """
    print("Choose one option from menu by typing a number:\n1-Add Specific\n2-Add at random\n")
    response = int(input())
    if response in [1,2]:
        return response


def visualise():
    """
    Task 5: Display a menu of options for how a graph should be produced. Read in the user's response.

    A menu should be displayed that contains the following options:
        'By Generation (Pie Chart)', 'By Type (Bar Chart)'

    :return: None if an invalid selection made otherwise an integer corresponding to a valid option
    """
    print("Choose one option from menu by typing a number:\n1-Generation(Pie Chart)\n2-By type (Bar Chart)\n")
    response = int(input())
    if response in [1,2]:
        return response

def by_name(p_list = []):
    
    """
    Task 6: Display a pokemon from the list, searching by name.

    The p_list is a list of pokemon.
    Prompt the user to enter name of the pokemon they are searching for.
    The function should display all the details related only to that single pokemon, if it's on the p_list.
    If pokemon of such name does not exist on the p_list, then display appropriate message.

    :param p_list: A list of pokemon
    :return: does not return anything
    """
    name = input("Enter name of the Pokemon: ")
    for pokemon in p_list:
        if pokemon[1] == name:
            print(pokemon)
            return
    print("No such Pokemon could be found!")



def by_type(p_list = []):
    
    """
    Task 7: Display pokemon from the list, searching by type.

    The p_list is a list of pokemon.
    Prompt the user to enter type of the pokemon they are searching for.
    The function should display all the details related only to pokemon of that type,
    if it's on the p_list.
    If no such pokemon of that type exists on the p_list, then display appropriate message.

    :param p_list: A list of pokemon
    :return: does not return anything
    """
    type = input("Enter the type of Pokemon: ")
    for pokemon in p_list:
        if pokemon[2] == type or pokemon[3] == type:
            print(pokemon)
            return
    print("No Pokemon of that type exists")



def add_specific_poke():
    
    """
    Task 8: Search for pokemon in the database, and return it if it's found.

    Access pokemon_database.csv using appropriate module.
    Search through this database, looking for a pokemon by it's name.
    If no such pokemon exists, then display appropriate message and return None.

    :param: None
    :return: A list representing a pokemon or None
    """
    with open("pokemon_database.csv") as database:
        csv_reader = csv.reader(database)
        name = input("Enter a name: ")
        for line in csv_reader:
            if line[1] == name:
                return line
        print("Pokemon not found")



def add_random_poke():
    
    """
    Task 9: Search for a random pokemon in the database, and return it.

    Access pokemon_database.csv using appropriate module.
    Pick out a random pokemon and return it.

    :param:  None
    :return: A list representing a pokemon
    """
    with open("pokemon_database.csv") as database:
        csv_reader = csv.reader(database)
        x = random.randint(1, 721)
        lista =[]
        for line in csv_reader:
            lista.append(line)
        return lista[x]


def show_all(pokedex = []):
    """
    Task 10: Print all pokemon from pokedex.

    Print key information about all the pokemon in the pokedex. Include their
    name, type, hp and generation.

    :param p_list: None
    :return: None
    """
    for pokemon in pokedex:
        print(f"Name: {pokemon[1]}\tType: {pokemon[2]}\tHP: {pokemon[5]}\tGeneration: {pokemon[11]}")



def save_pokes(pokedex = []):
    """
    Task 11: Save content of the pokedex to a suitable file format
    Print "Saving complete" at the end.

    :param p_list: pokedex: a list of pokemon
    :return: None
    """
    with open("pokedex.csv", "a", newline= "") as p_dex:
        csv_writer = csv.writer(p_dex)
        for item in pokedex:
            csv_writer.writerow(item)


def load_pokes(path):
    lista = []
    with open(path) as f:
        csv_reader = csv.reader(f)
        for line in csv_reader:
            lista.append(line)
    return lista
