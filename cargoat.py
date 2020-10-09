import random

class carOrGoat():
    def __init__(self, numtimes):
        self.numtimes = numtimes
        self.correctM1 = 0 # sticking w/ first choice
        self.correctM2 = 0 # switching doors
        self.rv = 0 # psuedo random value from 1-3
        self.car_loc = 0 # car location
        self.doors = [0,0,0]

    def grv(self): #generate random value
        self.rv = random.randrange(3)

    def method_1(self):
        self.grv()
        if self.doors[self.rv] == 2:
            self.correctM1 += 1

    def method_2(self):
        first_choice = random.randrange(3)
        other_spots = []

        for i in range(3):
            if i != first_choice and i != self.car_loc:
                other_spots.append(i)

        self.doors[random.choice(other_spots)] = -1

        second_choice = None
        for i in range(3):
            if i != first_choice and self.doors[i] != -1:
                second_choice = i

        if self.doors[second_choice] == 2:
            self.correctM2 += 1

    def gen_doors_m1(self):
        #0 = goat, 1 = car
        for i in range(self.numtimes):
            self.grv()
            self.doors[self.rv] = 2
            self.car_loc = self.rv
            self.method_1()
            self.doors = [0,0,0]

    def gen_doors_m2(self):
        #0 = goat, 1 = car
        for i in range(self.numtimes):
            self.grv()
            self.doors[self.rv] = 2
            self.car_loc = self.rv
            self.method_2()
            self.doors = [0,0,0]



print("\n-----The Monty Hall Problem-----\n")
print(">You are in a game show.")
print(">There are three doors. Behind one is a car, the other two have goats.")
print(">First you pick a door at random.")
print(">Then the game show host reveals a goat at random that was not behind your door.")
print(">You then have the choice of sticking with your door, or choosing the other available door.")
print("(This program only uses a psuedo random number generator)")
get = input("\nTimes to simulate this problem: ")

while not isinstance(get, int):
    try:
        get = int(get)
    except ValueError:
        get = input("Please input an integer: ")


cg = carOrGoat(get)


cg.gen_doors_m1()
cg.gen_doors_m2()

print("Always sticking with your first choice yielded you: {}% accuracy.".format(cg.correctM1/get))
print("While always switching to a second choice yielded you {}% accuracy.".format(cg.correctM2/get))
