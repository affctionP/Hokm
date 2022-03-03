class Player :
    #hand=[]
    def __init__(self,name):
        self.name=name
        self.hand=[]
        
    def show_hand(self):
        #return self.hand
        print("*****Hands of "+self.name+"*****")
        for i in self.hand:
            print(i.__str__())
    def set_hakem(self):
        self.is_hakem=True
        
    def __str__(self):
        return self.name