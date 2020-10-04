class Neighborhood:
    "a number of houses that belong together"
    total_size=0
    def __init__(self, name=""):
        self.name = name
        self.houses = []
    
    def add_houses(self,*house):
        for item in house:
            self.houses.append(item)
            Neighborhood.total_size += item.size()
        
    def size(self):
        #the size of 1 neighborhood
        return sum(house.size() for house in self.houses)
    
    def __str__(self):
        #string representation of the neighborhood
        return "Neighborhood '"+ self.name +"' houses:\n" + "\n".join([str(house) for house in self.houses])
    
class House:
    "The house that can contain many rooms"
    def __init__(self, available_space=100):
        self.rooms = []
        self.available_space = available_space
        self.totalsize=0
        
    def add_rooms(self, *room):
            for item in room:
                if self.size() + item.size > self.available_space:
                    raise NotEnoughSpaceError(f'There is not enough space in the house for the {item.name},  Available space: {self.available_space - self.totalsize} -- Space needed: {item.size} ')
                else:
                    self.rooms.append(item)
                    self.totalsize += item.size
                
    def size(self):
        return sum(room.size for room in self.rooms)
    
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

Neighborhood.total_size = 0
n1 = Neighborhood('Oak Valley')
n2 = Neighborhood('Mountain River')

houses = []
for i in range(3):
  h = House()
  bedroom = Room('bedroom', 10)
  kitchen = Room('kitchen', 9)
  bathroom = Room('bathroom', 3)
  h.add_rooms(bedroom, kitchen, bathroom)
  houses.append(h)

n1.add_houses(*houses)
n2.add_houses(*houses)

print(n1.name+" size= "+str(n1.size()))
print(n1.total_size)

print(n2.name+" size= "+str(n2.size()))
print(n2.total_size)

print("n total size= "+str(Neighborhood.total_size))
print("n1 total size= "+str(n1.total_size))
print("n2 total size= "+str(n2.total_size))

Neighborhood.total_size = 5

print("n total size= "+str(Neighborhood.total_size))
print("n1 total size= "+str(n1.total_size))
print("n2 total size= "+str(n2.total_size))

# print(str(n1))
# print(str(n2))


