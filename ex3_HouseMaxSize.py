class House:
    "The house that can contain many rooms"
    def __init__(self, available_space=100):
        self.rooms = []
        self.available_space = available_space
        self.totalsize=0
        
    def add_rooms(self, *room):
            for item in room:
                if sum([room.size for room in self.rooms]) + item.size > self.available_space:
                    raise NotEnoughSpaceError(f'There is not enough space in the house for the {item.name},  Available space: {self.available_space - self.totalsize} -- Space needed: {item.size} ')
                else:
                    self.rooms.append(item)
                    self.totalsize += item.size
                

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

class NotEnoughSpaceError(Exception):
    pass
    
h = House(20)
bedroom = Room('bedroom', 10)
kitchen = Room('kitchen', 9)
bathroom = Room('bathroom', 3)
h.add_rooms(bedroom, kitchen, bathroom)
print(h.size())
print(str(h))


# h = House(100)
# bedroom = Room('bedroom', 80)
# kitchen = Room('kitchen', 15)
# bathroom = Room('bathroom', 30)
# cellar = Room('cellar', 10)
# h.add_rooms(bedroom)
# h.add_rooms(kitchen)
# h.add_rooms(bathroom, cellar)
# # h.add_rooms(bathroom, cellar)
# print(f'Size of the house : {h.size()} m')
# print(f'No. of rooms in the house : {h.housesize()}')
# print(f'max space : {h.available_space}')
# print(str(h))
