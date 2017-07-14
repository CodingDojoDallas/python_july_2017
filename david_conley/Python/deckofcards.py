#52 cards
#shuffle and deal
# create player with name and hand
# player should be able to draw a card from deck and discard their hand.

import random
suite = ('c', 'd', 'h', 's')
ranks = ('2', '3', '4', '5', '6', '7', '8', '9','T', 'J', 'Q', 'K', 'A')

Deck = ()

class Poker(object):
	#initialze
	def __init__(self, card, num_players):
		self.card = card
		self.suite =  suite
		self.num_players = num_players

	def displayinfo(self):
	  return "ID: {} card: {} suite: {} num_players: {}".format(
        self.ID,	    
	      self.card,
	      self.suite,
	      self.num_players
	      
	  )
	  
class	Deck(object):
  def __init__(self, card_num, suite, rank):
    for rank in ranks:
      for suite in suites:
        card = card(rank, suite)
        deck.cards.append(card)
   
        return self
        
class Player(object):
  def __init__(self, ID):
    self.ID = ID
    
    
# print Poker(52, 5)
# print deck
player1 = Player(1)
player2 = Player(2)
print Deck