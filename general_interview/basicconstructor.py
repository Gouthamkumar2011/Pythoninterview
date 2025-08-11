class Hotel:
    def __init__(self, name, room):
        self.name = name
        self.room = room
    
    def welcome(self):
        print(f"Welcome {self.name}, your room is {self.room}.")
    
    def order_food(self, item):
        print(f"{self.name} in room {self.room} ordered {item}.")


Hotel1 = Hotel("Alice", 101)
Hotel2 = Hotel("Bob", 102)

Hotel1.welcome()
Hotel1.order_food("pasta")

Hotel2.welcome()
Hotel2.order_food("noodles")

        