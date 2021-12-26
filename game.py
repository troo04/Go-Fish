import random
import sys

def find(array, choice):
  for i in array:
    if i == choice:
      return True
  return False

def winner(player, computer):
  bookCountPlayer = {}
  bookCountComputer = {}
  playerBookCount = 0
  computerBookCount = 0

  for i in player:
    if i not in bookCountPlayer:
      bookCountPlayer[i] = 1
    else:
      bookCountPlayer[i] += 1

  for i in bookCountPlayer:
    if bookCountPlayer[i] == 4:
      playerBookCount += 1

  for i in computer:
    if i not in bookCountComputer:
      bookCountComputer[i] = 1
    else:
      bookCountComputer[i] += 1

  for i in bookCountComputer:
    if bookCountComputer[i] == 4:
      computerBookCount += 1

  if playerBookCount > computerBookCount:
    return 'Player wins!'
  elif playerBookCount < computerBookCount:
    return 'Computer wins!'
  else:
    return 'Tie!'

arrOfCards = []

for x in range(4):
  arrOfCards.append("A")
  arrOfCards.append("K")
  arrOfCards.append("Q")
  arrOfCards.append("J")
  arrOfCards.append("10")
  arrOfCards.append("9")
  arrOfCards.append("8")
  arrOfCards.append("7")
  arrOfCards.append("6")
  arrOfCards.append("5")
  arrOfCards.append("4")
  arrOfCards.append("3")
  arrOfCards.append("2")

random.shuffle(arrOfCards)

player = arrOfCards[:5]
computer = arrOfCards[5:10]

playerCount = {}

for x in player:
  if x not in playerCount:
    playerCount[x] = 1
  else:
    playerCount[x] += 1

computerCount = {}

for x in computer:
  if x not in computerCount:
    computerCount[x] = 1
  else:
    computerCount[x] += 1

for i in range(len(arrOfCards)):
  if i < 10:
    arrOfCards.pop(0)

deck = {}

for a in arrOfCards:
  if a not in deck:
    deck[a] = 1
  else:
    deck[a] += 1

def playerTurn():
  if len(arrOfCards) > 0:
    if len(player) == 0:
      print("You take one from the deck")
      player.append(arrOfCards[0])
      return
    else:
      print("Here is your hand: ", str(player))
      choice = input(">>> Your turn\n")
      if find(computer, choice.upper()) == True:
        print("Computer says: \"Here you go\"")

        for i in range(len(computer)):
          if computer[i] == choice.upper():
            player.append(computer[i])

        try:
          while True:
            computer.remove(choice)
        except ValueError:
          pass

      else:
        print("Computer says: \"Go Fish!\"")
        player.append(arrOfCards[0])
        arrOfCards.pop(0)
      print("Here is your hand: ", str(player))
  elif len(arrOfCards) == 0 and len(player) == 0:
    sys.exit("Game Over")

userLog = {}
for b in computer:
  userLog[b] = ""

def computerTurn(userLog):
  occurences = {}
  for i in computer:
    if i not in occurences:
      occurences[i] = 1
    else:
      occurences[i] += 1

  temp = 0

  for x in occurences:
    #something most likely wrong with userLog[str(x)] == "":
    if occurences[x] > 1 and userLog[str(x)] == "":
      temp = 1
      answer = input(">>> Computer\n\"Do you have any {}'s\"".format(x))
      userLog[str(x)] = answer
      anotherTemp = x
      break

  if temp == 0:
    randomNum = random.randrange(0, len(computer))
    answer = input(">>> Computer\n\"Do you have any {}'s\"".format(computer[randomNum]))
    if answer.strip().lower() == "yes":
      for i in range(len(player)):
        if player[i] == computer[randomNum]:
          computer.append(player[i])

      try:
        while True:
          player.remove(computer[randomNum])
      except ValueError:
        pass
    elif answer.strip().lower() == "go fish!":
      if len(arrOfCards) != 0:
        computer.append(arrOfCards[0])
        arrOfCards.pop(0)
        userLog[arrOfCards[0]] = ""


  elif temp == 1:
    if answer.strip().lower() == "yes":
      for i in range(len(player)):
        if player[i] == anotherTemp:
          computer.append(player[i])
          userLog[player[i]] = ""

      try:
        while True:
          player.remove(anotherTemp)
      except ValueError:
        pass
    elif answer.strip().lower() == "go fish!":
      if len(arrOfCards) != 0:
        computer.append(arrOfCards[0])
        arrOfCards.pop(0)
        userLog[arrOfCards[0]] = ""

while len(arrOfCards) != 0:
  playerTurn()
  if len(arrOfCards) == 0:
    break
  else:
    computerTurn(userLog)

winner(player, computer)
