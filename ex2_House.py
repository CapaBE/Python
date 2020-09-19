class House:
    "The house that can contain many rooms"
    def __init__(self):
        self.rooms = []
        
    def add_rooms(self, *room):
        self.rooms += room

    def size(self):
        return sum([room.size for room in self.rooms])
    
    def housesize(self):
        return len(self.rooms)
    
    #string representation of the house
    def __str__(self):
        return "House:\n" + "\n".join([str(room) for room in self.rooms])
  
    
class Room:
    "The room class with it's attributes name and size."
    def __init__(self, name, size):
        self.name = name
        self.size = size
    #string representation of the class
    def __str__(self):
        #includes 2 placeholders
        return "{}, {}m".format(self.name, self.size)  
    


h = House()
bedroom = Room('bedroom', 10)
kitchen = Room('kitchen', 9)
bathroom = Room('bathroom', 3)
h.add_rooms(bedroom, kitchen, bathroom)
print(f'Size of the house : {h.size()} m')
print(f'No. of rooms in the house : {h.housesize()}')
print(str(h))
p = House()
for i in range(10):
    p.add_rooms(Room(f'bedroom {i}', 15))



