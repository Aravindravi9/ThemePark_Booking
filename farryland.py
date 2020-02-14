'''Class Description:
Customer class:

play_game():

Calculates total points based on the list of games played by the customer
ThemePark allows a free ride on Game 2 if the customer has opted for Game 3. If this is satisfied, add "Game2" to list_of_games and include its points to total points

update_food_coupon():
 They provide food coupon to a customer who has opted Game 4 and has earned more than 15 points.
Updates attribute, food_coupon status to "Yes" if the above rule is satisfied

book_ticket():
Calculates ticket amount, generates ticket id, plays game, updates food coupon and returns true
Else, returns false'''

#This class represents ThemePark
class ThemePark:
    #dict_of_games contains the game name as key, price/ride and points that can be earned by customer in a list as value
    dict_of_games={"Game1":[35.5,5], "Game2":[40.0,6],"Game3":[120.0,10], "Game4":[60.0,7],"Game5":[25.0,4]}
    @staticmethod
    def validate_game(game_input):
        f=0
        for key, values in ThemePark.dict_of_games.items():
            if(game_input in key):
                f=1
                break
        if(f==1):
            return True 
        else:
            return False
         
    @staticmethod
    def get_points(game_input):
        for key, values in ThemePark.dict_of_games.items():
            if(game_input == key):
                return values[1]
                break

    @staticmethod
    def get_amount(game_input):
        for key, values in ThemePark.dict_of_games.items():
            if(game_input == key):
                return values[0]
                break
      

#This class represents ticket
class Ticket:
    __ticket_count=200
    def __init__(self):
        self.__ticket_id=0
        self.__ticket_amount=0
    def generate_ticket_id(self):
        self.__ticket_id =Ticket.__ticket_count
        Ticket.__ticket_count +=1
        
        #Auto-generate ticket_id starting from 201
        
    def calculate_amount(self,list_of_games):
        f=0
        for i in range(0 , len(list_of_games)):
            if(ThemePark.validate_game(list_of_games[i])):
                f=1 
            else:
                f=0 
                break
        if (f==1):
            self.__ticket_amount=0
            for i in range(0 , len(list_of_games)):
                self.__ticket_amount +=ThemePark.get_amount(list_of_games[i])
            
            return True
            
        else:
            return False
                
        
        '''Validate the games in the list_of_games.
        If all games are valid, calculate total ticket amount and assign it to attribute, ticket_amount and return true. Else, return false'''
    def get_ticket_id(self):
        return self.__ticket_id
    def get_ticket_amount(self):
        return self.__ticket_amount

class Customer(Ticket):
    
    def __init__(self,name,list_of_games):
        self.__name=name
        self.__list_of_games=list_of_games
        self.__ticket=0
        self.__points_earned=0
        self.__food_coupon='No'
	    
	    
    def get_name(self):
        return self.__name
        
    def get_list_of_games(self):
        return self.__list_of_games
        
    def get_ticket(self):
        return self.__ticket
        
    def get_points_earned(self):
        return self.__points_earned
        
    def get_food_coupon(self):
        return self.__food_coupon
        
    def play_game(self):
        for i in range(0 , len(self.__list_of_games)):
                self.__points_earned +=ThemePark.get_points(self.__list_of_games[i])
        for i in range(0 , len(self.__list_of_games)):
            if(self.__list_of_games[i]=='Game3'):
                self.__list_of_games.append('Game2')
                self.__points_earned +=ThemePark.get_points('Game2')
                break
                
                
        
    def book_ticket(self):
        if(self.calculate_amount(self.__list_of_games)):
            self.generate_ticket_id()
            self.play_game()
            self.update_food_coupon()
            #print("Success")
            return True
            
            
        else:
            return False
        
                
        
    def update_food_coupon(self):
        for i in range(0 , len(self.__list_of_games)):
            if(self.__list_of_games[i]=='Game4' and self.__points_earned >15):
                self.__food_coupon='Yes'
                
    
c=Customer('Raghul',['Game1','Game5','Game2'])
if(c.book_ticket()):
    print("Booking Succesfull!!")
    print("Ticket Details")
    print("Name :", c.get_name() )
    print("Ticket-Id:",c.get_ticket_id())
    print("Food-Coupon:",c.get_food_coupon())
    print("Points-Earned",c.get_points_earned())
    print("Games Played:",c.get_list_of_games())
    print("Total amount to be paid :",c.get_ticket_amount())
else:
    print("Booking failed - Invalid Game selected")
    
print("-----------------------------------------------------------------------------")  


c2=Customer('Varma',['Game1','Game5','Game3'])
if(c2.book_ticket()):
    print("Booking Succesfull!!")
    print("Ticket Details")
    print("Name :", c2.get_name() )
    print("Ticket-Id:",c2.get_ticket_id())
    print("Food-Coupon:",c2.get_food_coupon())
    print("Points-Earned",c2.get_points_earned())
    print("Games Played:",c2.get_list_of_games())
    print("Total amount to be paid :",c2.get_ticket_amount())
else:
    print("Booking failed - Invalid Game selected")






