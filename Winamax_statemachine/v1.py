# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 17:17:50 2023

@author: grab
"""

""" From CodingGame : "winamax-battle"
The Goal
Let's go back to basics with this simple card game: war!

Your goal is to write a program which finds out which player is the winner for a given card distribution of the "war" game.
 	Rules
War is a card game played between two players. Each player gets a variable number of cards of the beginning of the game: that's the player's deck. Cards are placed face down on top of each deck.
 
Step 1 : the fight
At each game round, in unison, each player reveals the top card of their deck – this is a "battle" – and the player with the higher card takes both the cards played and moves them to the bottom of their stack. The cards are ordered by value as follows, from weakest to strongest:
2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A.
 
Step 2 : war
If the two cards played are of equal value, then there is a "war". First, both players place the three next cards of their pile face down. Then they go back to step 1 to decide who is going to win the war (several "wars" can be chained). As soon as a player wins a "war", the winner adds all the cards from the "war" to their deck.
 
Special cases:
If a player runs out of cards during a "war" (when giving up the three cards or when doing the battle), then the game ends and both players are placed equally first.
The test cases provided in this puzzle are built in such a way that a game always ends (you do not have to deal with infinite games)
Each card is represented by its value followed by its suit: D, H, C, S. For example: 4H, 8C, AS.

When a player wins a battle, they put back the cards at the bottom of their deck in a precise order. First the cards from the first player, then the one from the second player (for a "war", all the cards from the first player then all the cards from the second player).

For example, if the card distribution is the following:
Player 1 : 10D 9S 8D KH 7D 5H 6S
Player 2 : 10H 7H 5C QC 2C 4H 6D
Then after one game turn, it will be:
Player 1 : 5H 6S 10D 9S 8D KH 7D 10H 7H 5C QC 2C
Player 2 : 4H 6D

"""
##### init #####
# input examples

class player_state():
    
    def __init__(self, cards_deck_1, cards_deck_2):
        # create card decks
        n = len(cards_deck_1)
        m = len(cards_deck_2)

        # map parsing to numeric values
        card_map = {str(ii): ii for ii in range(2, 11)}
        card_map["J"] = 11
        card_map["Q"] = 12
        card_map["K"] = 13
        card_map["A"] = 14

        # create card decks
        self.deck_1 = []
        for ii in range(n):
            card_1 = card_map[in_1[ii][:-1]]
            self.deck_1.append(card_1)
            
        self.deck_2 = []  
        for ii in range(m):
            card_2 = card_map[in_2[ii][:-1]]
            self.deck_2.append(card_2)

        # create the game stack
        self.war_stack_1 = []
        self.war_stack_2 = []

        # output init
        self.rounds = 0
        
        # winner:
        self.winner = -1 #1 or 2, PAT
        
        return

    ##### functions #####
    def make_battle(self): 
        """
        Each player puts a card on his stack
        Update decks and stacks
        """
        # each player puts a card on his stack
        card_1 = self.deck_1.pop(0)
        card_2 = self.deck_2.pop(0)
        self.war_stack_1.append(card_1)
        self.war_stack_2.append(card_2)
        
        return

    def declare_winner(self):    
        """
        Find winner of battle
        """
        # evaluating battle winner
        if self.war_stack_1[-1] > self.war_stack_2[-1]: outcome = 1
        elif self.war_stack_1[-1] < self.war_stack_2[-1]: outcome = 2  
        else: outcome = 0   
        
        return outcome

    def make_war(self):
        """
        Each players puts 3 cards on his stack
        Update decks and stacks
        /!\ will return an error if len(deck) <3 ! Error is used later on
        """
        # try to draw 3 cards from each players and puts on their stacks
        for _ in range(3):
                self.war_stack_1.append(self.deck_1.pop(0))
        for _ in range(3):
                self.war_stack_2.append(self.deck_2.pop(0))
    
        return

    def resolve_stack(self, outcome):
        """
        Resolve phase: clean stack and updates deck if a battle winner exists
        """
        if outcome == 1:
            self.deck_1 += self.war_stack_1
            self.deck_1 += self.war_stack_2
            self.war_stack_1 = []
            self.war_stack_2 = []         
        
        elif outcome == 2:
            self. deck_2 += self.war_stack_1
            self.deck_2 += self.war_stack_2
            self.war_stack_1 = []
            self.war_stack_2 = []
            
        return
    
    def play_one_round(self):
        """
        Play a single round of the game
        """
        # increment number of rounds
        self.rounds += 1    

        # 1. battle phase
        self.make_battle()   
        # 2. find outcome
        outcome = self.declare_winner()  
        # 3. entering war phase   
        if outcome == 0:
            while outcome == 0:
                
                try: 
                    # i. make war
                    self.make_war()
                    # ii. make battle
                    self.make_battle()
                    # iii. find winner
                    outcome = self.declare_winner()
                    
                # If a player has no cards during war: PAT
                except:
                    self.deck_1 = []
                    self.deck_2 = []
                    self.war_stack_1 = []
                    self.war_stack_2 = []
                    break
            
        # 4. end of round : clean stack/decks 
        self.resolve_stack(outcome)
        return
        
    
    def play(self):
        """
        Play game until a player looses or PAT during war
        """
        #####  Game loop ##### 
        # game loop: play rounds until PAT or winner is declared
        while self.deck_1 != [] and self.deck_2 != []:
            
            #single round
            self.play_one_round()
          
        # finding the winner
        if self.deck_1 != [] and self.deck_2 == []:
            print(1, self.rounds)
        elif self.deck_1 == [] and self.deck_2 != []:
            print(2, self.rounds)
        else:
            print('PAT')
        
            
        return 
      
#####  Instanticate game #####
in_1 = ["10D", "9S", "8D", "KH", "7D", "5H", "6S"]
in_2 = ["10H", "2H", "2C", "2C", "2C", "2H", "2D"]

game = player_state(in_1,in_2)
game.play()



