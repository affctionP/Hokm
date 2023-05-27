from math import floor
import card
import random
import player
from math import floor
class Game :
    SIGNS = ['heart','club','diamond','spade']
    VALUES = ['King','Queen','jack','Ace','2','3','4','5','6','7','8','9','10']
    def __init__(self):
        self.cards=[]
        self.players=[]


        for i in range (len(self.SIGNS)):
            for j in range (len(self.VALUES)):
                self.cards.append(card.Card(self.VALUES[j],self.SIGNS[i]))
                
    def join_player(self,player):
        self.players.append(player)
 
        
    def show_players (self):
        for k in (self.players):
            print(k.__str__())
                
                
    def __str__(self):
        for obj in  self.cards:
            print( obj, sep =' ' )
    
    def shuffle(self,count,replace=True):
        if replace :
            cards=self.cards
        else :
            cards=self.cards.copy()
        sh_hand=[]
        for i in range(0,count):
            k=random.randint(1,len(cards))
            q=cards.pop(k-1)
            sh_hand.append(q)
        return sh_hand
        
    
    def get_hand(self,card_list,player):
        for card in card_list:
            player.hand.append(card) 
            
        #player.hand=card_list 
                   
    """def update_wieght(self):
        for index in self.cards :
            if index.sign == self.sign :
                for k in self.VALUES:
                    index."""
                
        
            
    def remove_card(self,card):
        self.cards.remove(card)
        
    def set_hokm(self,sign):
        self.hokm=sign

                
    def get_hokm(self):
        return self.hokm
    #for first round
    def set_king(self):
        """rule : give every player a card  until one of them recive a 'ace'
        sign if both of them recive 'ace' at same time do this again between that palyers
        """
        #print(f"lens before shuffle {len(self.cards)}")
        king_id=[]
        for card in range (int(len(self.cards)/len(self.players))) :
            sh_cards=self.shuffle(len(self.players),replace=False)
            print(f"round  shuffle {card}")
            for index ,sh_card in enumerate(sh_cards ):
                #print(f"round  shuffle {sh_card.sign}")
                if sh_card.value == 'Ace' :
                    king_id.append(index)
                    
            if len(king_id) == 1 :
                hakem=[ person  for person in self.players if  person.id == king_id[0]]
                hakem[0].set_hakem()
                print (f" hakem is {hakem[0].name }")
                break
                    
                      
                 
                    
           
     
        
            
        
               
    
    
if __name__ == '__main__':
    
    game= Game()
    player1=player.Player("atefeh",0)
    print (player1.id)
    player2=player.Player("saeed",1)
    #game.cardss()
    #cards_list=game.shuffle(3)
    #cards_list1=game.shuffle(5)
    
    game.join_player(player1)
    game.join_player(player2)
    
    game.set_king()
    
    #game.get_hand(cards_list,player1)
    #game.get_hand(cards_list1,player2)
    #player1.show_hand()
    #player2.show_hand()
    
    