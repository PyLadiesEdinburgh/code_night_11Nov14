


   

class Game():
    
    def __init__(self, name):
        self.name = name
        self.end = False
        
     
    def start(self):
        print("""You run into the building, and spot a body in the middle of the room.
                Out of the corner of your eye, you spot a figure scrambling out the window
                
                Do you:
                - Stay and check the body, or
                - Chase the figure!""")
        print()


        choice = input("Enter 1 to stay; enter 2 to chase") 

        if choice == "1":
            self.check_house()
        elif choice == "2":
            self.end_game()

            
    def check_house(self):
        print("""The body is a man, who is not responsive. You think to yourself that you should probably check the rest of the house.
        The house has two floors.
        
        Do you:
        - Stay downstairs and check the other rooms, or
        - Go upstairs and take a look there?""")
        
        choice = input("Enter 1 to go downstairs; enter 2 to check upstairs") 

        if choice == "1":
            self.end_game()
        elif choice == "2":
            self.go_upstairs()
        
    def go_upstairs(self):
        print("""You hear commotion coming from a room at the end of the corridor. 
        
        Do you:
        - Investigate, or
        - Call for help?""")
        
        choice = input("Enter 1 to go investigate; enter 2 to call for help") 

        if choice == "1":
            self.investigate()
        elif choice == "2":
            self.end_game()
    
    def investigate(self):
      
        print("""You find a woman lying on the floor in a pool of blood.

        Do you:
        - Phone an ambulance or
        - Question her?""")

        choice = input("Enter 1 to phone an ambulance; enter 2 to question her") 

        if choice == "2":
            self.question()
        elif choice == "1":
            self.end_game()
    
    def question(self):
        
        print("""You question the woman who tells you that she has been stabbed by the vicious killer Kate. Well done Detective {}""".format(self.name))
        self.end_game()
    def end_game(self):
        self.end = True

def start_game():
    name = input("What is your name?") 
    new_game = Game(name)
    while new_game.end == False:
        new_game.start()
    
    print("Game over")
    restart = input("Would you like to play again? Y/N")

    if restart == "Y":
        start_game()

start_game()
    