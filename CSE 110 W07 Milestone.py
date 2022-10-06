from random import randint

INTL_arch = ["Nova Lake", "Panther Cove", "Darkmont", "Lunar Lake", "Arrow Lake", "Lion Cove", "Skymont",
             "Sierra Forest", "Granite Rapids", "Meteor Lake", "Redwood Cove", "Crestmont", "Emerald Rapids",
             "Raptor Lake", "Raptor Cove", "Gracemont", "Sapphire Rapids", "Golden Cove", "Rocket Lake", "Cypress Cove",
             "Tiger Lake", "Willow Cove", "Cooper Lake", "Comet Lake", "Sky Lake", "Ice Lake", "Sunny Cove",
             "Coffee Lake", "Cannon Lake", "Palm Cove", "Amber Lake", "Kaby Lake", "Whisky Lake", "Apollo Lake",
             "Broadwell", "Haswell", "Devil's Canyon", "Ivy Bridge", "Sandy Bridge", "Westmere", "Nehalem", "Penryn",
             "Core", "Merom", "Yonah", "Doathan", "Banias", "Tualatin", "Copermine", "Katmai", "Deshutes", "Klamath"]
NVDA_arch = ["Lovelace", "Hopper", "Grace", "Ampere", "Turing", "Volta", "Titan", "Pascal", "Maxwell", "Kepler",
             "Fermi", "Telsa", "Quadro", "Tegra", "Kalel", "Wayne", "Grey", "Logan", "Erista", "Parker", "Xavier",
             "Orin", "Atlan", "Curie", "Rankine", "Kelvin", "Celsius", "Fahrenheit"]
AMD_arch = ["Granite Ridge", "Strix Point", "Turin", "Raphael", "Dragon Range", "Phoenix", "Genoa", "Bergamo",
            "mendocino", "Vermeer", "Cezanne ", "Rembrandt", "Milan", "Milan-X", "Chagall", "Matisse", "Rome",
            "Castle Peak", "Renoir", "Lucienne", "Pinnacle Ridge", "Colfax", "Picasso", "Summit Ridge", "Whitehaven",
            "Raven Ridge", "Naples", "Snowy Owl"]
list_all = INTL_arch + NVDA_arch + AMD_arch
INTL_len = len(INTL_arch) - 1
NVDA_len = len(NVDA_arch) - 1
AMD_len = len(AMD_arch) - 1
list_all_len = len(list_all) - 1
# INTL_arch[randint(0, INTL_len)]
# NVDA_arch[0, NVDA_len]
# AMD_arch[0, AMD_len]


def start_up():
    string = ""
    y = 0
    word = ""
    for x in string:
        if x.isalpha():
            word += "_"
        else:
            word += x
        y += 1

    game(string, word)
    print(f"The answer was {string}.")


def choose_answer_pool():
    print(f"What do answer pool do you want to guess from?\n"
          "1. Intel Architectures\n"
          "2. Nvidia Architectures\n"
          "3. AMD Architectures\n"
          "4. All of the above")
    answer = int(input(""))

    if answer == 1:
        word = INTL_arch[randint(0, INTL_len)]
        print(word)
        return word
    if answer == 2:
        word = NVDA_arch[randint(0, NVDA_len)]
        print(word)
        return word
    if answer == 3:
        word = AMD_arch[randint(0, AMD_len)]
        print(word)
        return word
    if answer == 4:
        word = list_all[randint(0, list_all_len)]
        print(word)
        return word


def game(original, current_word):
    letter = str("o")
    new_word = list(current_word)
    guess_count = 5
    guessed = ""
    while guess_count > 0:
        y = 0
        print("".join(new_word))
        print(f"You have {guess_count} number of guesses left")
        letter = input(str("What is your one letter guess? "))
        if letter in guessed:
            print(f"You already guessed {letter}")
            guess_count -= 1

        elif letter or letter.upper() in original:
            print(f"Yes, {letter} is in the answer.")
            for x in original:
                if x == letter:
                    new_word[y] = letter
                elif x == letter.upper():
                    new_word[y] = letter.upper()
                y += 1

        else:
            print(f"No, {letter} is in the answer.")
            guess_count -= 1

        print("")
        guessed += letter.lower()
        if "_" not in new_word:
            print("You won!")
            if guess_count == 5:
                print("You made no mistakes!")
            else:
                print(f"You only made a mistake {-1 * (guess_count -5)} times!")
            guess_count = 0
        elif guess_count == 0:
            print("Game over")


start_up()
