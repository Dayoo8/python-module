class hair:
    

    def __init__(self, length, color):
        self.length = length
        self.color = color

hair1 = hair("long", "black")
hair2 = hair("short", "red")

print(hair1.length)
print(hair2.color)
       
class hair:
    

    def __init__(self, length, color):
        self.length = length
        self.color = color

    def describe(self):
        print(f"This hair has grown {self.length} and is {self.color} in color.")

hair1 = hair("long", "black")
hair2 = hair("short", "red")

print(hair1.length)
print(hair2.color)
hair1.describe()
hair2.describe()

class weaves:
    def __init__(self, style, texture):
        self.style = style
        self.texture = texture

    def describe(self):
        print(f"This weave has a {self.style} style with a {self.texture} texture.")

weaves1 = weaves("curly", "soft")
print(weaves1.style)
weaves1.describe()


class LuxuryWeave(weaves):
    def __init__(self, style, texture, color, price):
        super().__init__(style, texture)
        self.color = color
        self.price = price  # additional attribute

    def describe(self):
        print(f"A luxury {self.color} weave, {self.style} style, {self.texture} texture, priced at ${self.price}.")



        # Base Class
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method.")

# Subclass 1
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Subclass 2
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Subclass 3
class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

# Using Polymorphism
def start_journey(vehicles):
    for v in vehicles:
        v.move()  # Each object calls its own version of move()

# Create Objects
car = Car()
plane = Plane()
boat = Boat()

# List of vehicles
fleet = [car, plane, boat]

# Start journey
start_journey(fleet)






    


