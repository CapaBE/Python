class Room:
    "The room class with it's attributes name and size."
    def __init__(self, name, size):
        self.name = name
        self.size = size
    #string representation of the class
    def __str__(self):
        #includes 2 placeholders
        return "{}, {}m".format(self.name, self.size)

# instantiation of my room 
myroom = Room("My own room",125)

# printing out info about the created room 
print("I have created the room '" + myroom.name + "' with it's size '" + str(myroom.size) +"'.")

# printing out documentation of the class  
print(myroom.__doc__)

