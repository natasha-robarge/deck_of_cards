def deck_o_cards():
  values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace'];
  suits = ['hearts', 'diamonds', 'clubs', 'spades'];

  cards = [] # deck
  shuffledCards = [] # deck shuffled

  topCard = 0
  card = {}

  for i in enumerate(suits):
    for j in enumerate(values):
      card = {
        suit: suits[i],
        value: values[j]
      }
    cards.push(card)
  shuffledCards = shuffle(cards)
  
  topCard = shuffledCards[0]

  print("The deck has {} cards".format(len(cards)))
  print("The top card is the {} of {}".format(topCard.value, topCard.suit))

def shuffle(arr):
  counter = len(arr), temp, idx

  while counter > 0:
    idx = math.floor(math.random * counter)

    counter -= 1

    temp = arr[counter]
    arr[counter] = arr[idx]
    arr[idx] = temp

  print(arr)

deck_o_cards()