import card
import random
import player
class Game :
    def __init__(self):
        self.cards=[]
        self.palyers=[]
        SIGNS = ['heart','club','diamond','spade']
        VALUES = ['King','Queen','jack','Ace','2','3','4','5','6','7','8','9','10']
        for i in range (len(SIGNS)):
            for j in range (len(VALUES)):
                self.cards.append(card.Card(VALUES[j],SIGNS[i]))
                
    def join_player(self,player):
        self.palyers.append(player)
        
    def show_players (self):
        for k in (self.players):
            print(k.__str__())
                
                
    def __str__(self):
        for obj in  self.cards:
            print( obj, sep =' ' )
    
    def shuffle(self,count):
        sh_hand=[]
        for i in range(count):
            k=random.randint(1,len(self.cards)-1)
            q=self.cards.pop(k)
            sh_hand.append(q)
        return sh_hand
        
    
    def get_hand(self,card_list,player):
        for card in card_list:
            player.hand.append(card)  
                   

            
    def remove_card(self,card):
        self.cards.remove(card)
        
    def set_hokm(self,sign):
        self.hokm=sign
    def get_hokm(self):
        return self.hokm
    #for first round
    def find_hakem(self):
        while True:
            for i in self.players:
                k=self.shuffle(1)
                if k[0].__str__().split('__')[0] == 'Ace':
                    print (i.__str__()+" is hakem")
                    break
            
        
               
    
    
if __name__ == '__main__':
    
    game= Game()
    player1=player.Player("atefeh")
    player2=player.Player("saeed")
    cards_list=game.shuffle(3)
    cards_list1=game.shuffle(5)
    game.get_hand(cards_list,player1)
    game.get_hand(cards_list1,player2)
    player1.show_hand()
    player2.show_hand()
    
    