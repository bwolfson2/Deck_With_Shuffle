import itertools as it
import random
from operator import itemgetter
import timeit

#ENUM's
SUITS = ['♠', '♦', '♥', '♣']#["Clubs","Diamonds","Hearts","Spades"]
RANKS = list(range(2,11,1)) + ["Jack","Queen","King","Ace"]
CARDS = ["{rank} of {suit}".format(rank=i[0],suit=i[1]) for i in it.product(RANKS,SUITS)]

#Implements a deck class with Fischer Yates Shuffle
class Deck:
	def __init__(self):
		self.__deck = CARDS.copy()
	
	def shuffle(self):
		#Implements Fischer Yates Shuffle, runs in O(N) time
		#Implemented for completeness, the python's random.shuffle module uses the same algorithm, but runs quicker
		for i in range(len(self.__deck)):
			rand_idx = random.randrange(start=i,stop=len(self.__deck),step=1)
			self.__deck[i],self.__deck[rand_idx] = self.__deck[rand_idx],self.__deck[i]
	
	#Returns a copy of the deck in it's current state
	def get_deck(self):
		return self.__deck.copy()
	
	#Deals cards from the top of the deck to the desired number of players
	def deal_cards(self,num_players,num_cards = 52):
		try:
			assert(num_cards < 53)
		except:
			ValueError("Please deal more than -1 and less than 53 cards")
		return [self.__deck[i:num_cards:num_players] for i in range(0, num_players)]
	
def shuffle_time_test():
	deck = Deck()
	num_trials = 10000
	print("Deck.shuffle implementation (n={num_trials}): ".format(num_trials=num_trials))
	deck_implemenation_time = timeit.timeit("deck.shuffle()",globals={"deck":deck},number=10000)
	print(deck_implemenation_time)
	deck_array = deck.get_deck()
	random_shuffle_implementation = timeit.timeit("random.shuffle(deck_array)",globals={"deck_array":deck_array,"random":random},number=10000)
	print("random.shuffle implementation (n={num_trials}): ".format(num_trials=num_trials))
	print(random_shuffle_implementation)
	print("Ratio of Deck.shuffle time to random.shuffle\n {:.2}".format(deck_implemenation_time/random_shuffle_implementation))
	
def main():
	deck = Deck()
	for num_cards in range(53):
		for num_players in range(1,14):
			deck.shuffle()
			hands = deck.deal_cards(num_players,num_cards)
			#Expected hand length, assuming the whole deck is dealt out
			expected_hand_length = [int(num_cards/num_players) + 1 if i <= num_cards % num_players else int(num_cards/num_players) for i in range(1,num_players+1)]
			actual_hand_length = [len(hand) for hand in hands]
			try:
				assert(expected_hand_length == actual_hand_length)
			except:
				raise ValueError("Expected hand size and actual hand size do not match")
	
if __name__ == "__main__":
	main()