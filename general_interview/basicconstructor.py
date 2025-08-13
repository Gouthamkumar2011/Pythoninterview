class Guest():
    def __init__(self, name, room) -> None:
        self.name = name
        self.room = room
    
    def Welcome(self):
        print(f"Welcome {self.name}, your room is {self.room}")
    
    def food_item(self,item):
        print(f"{self.name} in {self.room} ordered {item}")


guest1 = Guest("alice",101)
guest2 = Guest("Biob",102)

guest1.Welcome()
guest1.food_item("Bacon")

guest2.Welcome()
guest2.food_item("Noodles")


        