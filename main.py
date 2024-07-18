import numpy as np

rng = np.random.default_rng()

def pair_up(given_names):
    """
    Return list of tuples: pairs of shuffled names
    """

    name_list = given_names.copy()

    #Shuffle the name lisst copy
    rng.shuffle(name_list)

    #Zip every other name into tuples, cast into a list of tuples
    pair_list = list(zip(name_list[::2], name_list[1::2]))
    return pair_list

    if __name__ == "__main__":
        names= [
            "Jasmine",
            "Jacob",
            "Jyiar",
            "Ahmed",
            "Justice",
            "Amora",
            "Ahmad",
            "Jalena",
            "Julien",
            "Marqus"
        ]

        print(pair_up(names))