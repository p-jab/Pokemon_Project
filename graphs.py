import matplotlib.pyplot as plt
def pie_chart(pokedex = []):
    dicto = {}
    for pokemon in pokedex:
        dicto[pokemon[11]] = dicto.get(pokemon[11],0) + 1
    x = dicto.values()
    l = [f"Generation {x}" for x in dicto.keys()]
    plt.pie(x, labels=l, autopct="%1.0f%%")
    plt.title("My Pokemon sorted by generation")
    plt.show(block = False)
    plt.pause(0.01)
    input()
    plt.close()
    """3
    Task 27: Create a Pie Chart showing pokemon from pokedex sorted by their generation

    Access the pokedex, sort out pokemon by generation and plot this data in a
    pie chart format. Add labels to clearly identify each generation.

    :param pokedex: list of pokemon
    :return: None
    """

def bar_chart(pokedex = []):
    dicto = {}
    for pokemon in pokedex:
        dicto[pokemon[2]] = dicto.get(pokemon[2],0) + 1
    y = dicto.values()
    x = dicto.keys()
    plt.bar(x, y)
    plt.title("My Pokemon sorted by type")
    plt.xlabel("Type of Pokemon")
    plt.ylabel("Number of Pokemon")
    plt.show(block = False)
    plt.pause(0.001)
    input()
    plt.close()
    """
    Task 28: Create a Bar Chart showing pokemon from pokedex sorted by their type

    Access the pokedex, sort out pokemon by type and plot this data in a
    bar chart format. Add axis labels and main title.

    :param pokedex: list of pokemon
    :return: None
    """