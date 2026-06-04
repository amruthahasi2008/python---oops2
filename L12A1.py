class cricket:
    def __init__(self,player,score):
        self.__score = score       # private attribute
        self.__player = player     # private attribute
    def info (self) :
        print(f"cricket player - {self.__player} , score -{self.__score}") # same method name as football
    def play(self) :
        print(f"{self.__player} hits a six!") # same method name different output
    def get_score (self) :  # getter method
        return self.__score
    def set_score(self, new_score) : # setter method

        if new_score >= 0 :
            self.__score = new_score
            print(f"score updated to {self.__score}")
        else :
            print("score cannot be negative")
    
class football :
    def __init__(self,player,score):
        self.__score = score       # private attribute
        self.__player = player     # private attribute
    def info (self) :
        print(f"football player - {self.__player} , score -{self.__score}")
    def play(self) :
        print(f"{self.__player} scores a goal!") # same method name different output
    def get_score (self) :  # getter method
        return self.__score 
    def set_score(self, new_score) : # setter method

        if new_score >= 0 :
            self.__score = new_score
            print(f"score updated to {self.__score}")
        else :
            print("score cannot be negative")

# create objects
Cricket = cricket("rohit",85)
Football = football("arjun",2)

# polymorphism
print("---------- score board -----------")
for sport in (Cricket,Football) :
    sport.info
    sport.play
    print()

# encapsulation
print("--- direct change attemp ---")
cricket.__score = 999
print("get score still shows",Cricket.get_score())

print("---- updated scores ----")
Cricket.set_score(999)
Football.set_score(4)


    

    

    


