def get_starting_number():
    response = input("How many bottles of beer on the wall? ")

    while not response.isnumeric() or int(response) < 1:
        response = input("How many bottles of beer on the wall? ")

    return int(response)


def sing(num_bottles):
    for bottles in range(num_bottles, 0, -1):
        if bottles == 1:
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall!")
        elif bottles == 2:
            print("2 bottles of beer on the wall, 2 bottles of beer.")
            print("Take one down, pass it around, 1 bottle of beer on the wall.")
            print()
        else:
            print("{} bottles of beer on the wall, {} bottles of beer.".format(bottles, bottles))
            print("Take one down, pass it around, {} bottles of beer on the wall.".format(bottles - 1))
            print()