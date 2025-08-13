class guest():
    def __init__(self, name, room,size) -> None:
        self.name = name
        self.room = room
        self.size = size
    
    def Welcome(self):
        print(f'Welcome {self.name}, your room number is {self.room}')
    
    def food(self,food):
        print(f'The guest in {self.room} has ordered {food}')
        print(f'the room is a {self.size}')

    def

guest1 = guest("Alice", 101, "2BHK")
guest2 = guest("Bob",102, "1 BHK")

guest1.Welcome()
guest1.food("Noodles")
guest2.Welcome()
guest2.food("Bacon")




