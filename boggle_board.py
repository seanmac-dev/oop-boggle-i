import random
import string


class BoggleBoard:
    grid = []

    def __init__(self, name):
        # self._random = random
        self._name = name

    def shake(self):
        length = 4
        # random_string1 = "".join(
        #     random.choice(string.ascii_letters) for _ in range(length)
        # )
        # random_string2 = "".join(
        #     random.choice(string.ascii_letters) for _ in range(length)
        # )
        # random_string3 = "".join(
        #     random.choice(string.ascii_letters) for _ in range(length)
        # )
        # random_string4 = "".join(
        #     random.choice(string.ascii_letters) for _ in range(length)
        # )
        # random_string1, random_string2, random_string3, random_string4 = "".join(
        #     random.choice(string.ascii_letters) for _ in range(length)
        # )

        # while len(BoggleBoard.grid) < 4:
        #     BoggleBoard.grid.append(random_string1.upper())
        #     BoggleBoard.grid.append(random_string2.upper())
        #     BoggleBoard.grid.append(random_string3.upper())
        #     BoggleBoard.grid.append(random_string4.upper())

        for i in range(length):
            obj = "  ".join(random.choice(string.ascii_letters) for _ in range(length))
            BoggleBoard.grid.append(obj.upper())

        for obj in BoggleBoard.grid:
            q = "Q"
            obj = obj.replace(q, "Qu")
            print(obj)

            # for i in obj:
            #     if i == "Q":
            #         i += "u"
            # print(obj)


player1 = BoggleBoard("Bob")

player1.shake()


# Goal: 4x4 grid, randomly generated letters
# Create BoggleBoard class
# shake!() (A-Z random)


# import string

# Set the length of the random string
# length = 5  # Change this to the desired length

# Generate a random string of letters
