class Player :
    #hand=[]
    def __init__(self,name,id):
        self.name=name
        self.id=id
        self.hand=[]
        
    def show_hand(self):
        #return self.hand
        print("*****Hands of "+self.name+"*****")
        for i in self.hand:
            print(i.__str__())
    def set_hakem(self):
        self.is_hakem=True
    
        
        
    def play(self,index):
        self.hand.remove(index)
        return index
        
    def __str__(self):
        return self.name
    