from gameData import allItems, allCharacters, worldRooms, CHARACTERS, FRIEND, HEALTH, STRENGTH, WEAPON, DAMAGEAMPLIFIER, CHARDESC, CHARDIALOGUE, DESC, NORTH, SOUTH, EAST, WEST, UP, DOWN, GROUND, GROUNDDESC, SHORTDESC, LONGDESC, TAKEABLE, DESCWORDS, SCREEN_WIDTH
import cmd, textwrap, random, sys, time

location = 'Outside the Hut' #Start outside The Hut
inventory = [] #Start with blank inventory
charInfoDict = {} #Start with no creatures discovered
showFullExits = True
ALIVE = "alive"
playerHealth = 30
HIT = 'hit'
STAND = 'stand'
battleOptions = [HIT, STAND]
weaponCount = 0
killedEnemyCount = 0
enemyCounter = 0

#Counting how many enemies are on the map
for eachCharacter in allCharacters:
        if allCharacters[eachCharacter].get(FRIEND, True) == False:
            enemyCounter += 1

#Shown display when game is finished
def finishedGame(killedEnemyCount):
    print("""\n                                   .''.       
       .''.      .        *''*    :_\/_:     . 
      :_\/_:   _\(/_  .:.*_\/_*   : /\ :  .'.:.'.
  .''.: /\ :   ./)\   ':'* /\ * :  '..'.  -=:o:=-
 :_\/_:'.:::.    ' *''*    * '.\'/.' _\(/_'.':'.'
 : /\ : :::::     *_\/_*     -= o =-  /)\    '  *
  '..'  ':::'     * /\ *     .'/.\'.   '
      *            *..*         :
        *
        *\n""")
    print("\nA noble and brave hero,")
    print("You have saved the lands from grief and despair!")
    print(f"Slaughtering all {killedEnemyCount} enemies, you have forever saved the lands from turmoil.")
    print("The creatures of the land are eternally grateful.\n")
    print("To quit the game, simply type 'quit'. If you would like to explore more, the option is open.")

#When player enters a battle
def battleMode(enemyName, enemyHealth):
    global weaponCount
    global playerHealth
    global killedEnemyCount
    global enemyCounter
    damageIncrease = 1.0

    print("\nYou approach an enemy!")

    fightOrFlight = input("Do you fight or flight? ").lower().strip()

    while fightOrFlight != "fight" and fightOrFlight != "flight":
        fightOrFlight = input("Sorry, I didn't get that. Do you fight or flight? ").lower().strip()
    
    if fightOrFlight == "flight":
        print("\nYou try to outrun the enemy!")
        time.sleep(1)
        print("You're running...\n")
        time.sleep(3)
        if random.randint(0,3) > 2:
            print("Haha! You have outrun the enemy!")
            return
        else:
            print("Despite your olympic sprinting abilities, the enemy has caught up to you.")

    print(f"\nPlayer Health: {playerHealth}")
    print(f"Enemy Health: {enemyHealth}")
    weaponList = []
    
    #Apply damage increase if the player has a weapon
    if weaponCount == 1:
        for potentialWeapon in inventory:
            if allItems[potentialWeapon].get(WEAPON) != None:
                print(f"\nYou draw out your {potentialWeapon} and brace yourself for an attack.")
                damageIncrease = allItems[potentialWeapon][DAMAGEAMPLIFIER]

    #Ask the user which weapon they want to use if they have multiple
    if weaponCount > 1:
        for potentialWeapon in inventory:
            if allItems[potentialWeapon].get(WEAPON) != None:
                weaponList.append(potentialWeapon)
        
        print("\nYou have the following weapons:")
        for item in weaponList:
            print(item)

        lowerWeaponList = [weapon.lower() for weapon in weaponList]

        userWeapon = input("\nWhich weapon would you like to use? ")
        while userWeapon.lower().strip() not in lowerWeaponList:
            print("Please list a weapon which you have in your inventory.\n")
            userWeapon = input("Which weapon would you like to use? ")
        userWeapon = weaponList[lowerWeaponList.index(userWeapon)]

        damageIncrease = allItems[userWeapon][DAMAGEAMPLIFIER]

    #Check if the fight can continue
    while playerHealth > 0 and enemyHealth > 0:

        playerTactic = input("\nDo you stand or hit? ")
        while playerTactic.strip().lower() != "hit" and playerTactic.strip().lower() != "stand":
            playerTactic = input("Sorry, I didn't get that. Do you stand or hit? ")

        enemyTactic = [battleOptions[random.randint(0, 1)]][0]
        
        if playerTactic == "stand":
            if enemyTactic == "stand":
                if playerHealth <= 25:
                    playerHealth += 5
                    print("\nYour magical powers reinvigorate you as you regain 5 health.")

                print("\nYou and the enemy brace yourselves for another attack.")

            if enemyTactic == "hit":
                print("\nSeeing that you have not hit, the enemy reacts quickly!")
                print("You lose 5 health.")
                playerHealth -= 5

        #Player tactic: "hit"
        else:
            if enemyTactic == "stand":
                currentDamage = int(str(damageIncrease * 10).rstrip('0').rstrip('.'))
                enemyHealth -= currentDamage
                print("\nThe enemy is distracted!")
                print(f"You go in for a hit and deal {currentDamage} damage!")
            
            if enemyTactic == "hit":
                currentDamage = int(str(damageIncrease * 10).rstrip('0').rstrip('.'))
                enemyHealth -= currentDamage
                playerHealth -= 5
                print("\nYou and the enemy both go in for the kill!\n")
                print(f"The enemy is wounded and loses {currentDamage} health.")
                print("You are wounded and lose 5 health.")

        if playerHealth < 0:
            playerHealth = 0

        if enemyHealth < 0:
            enemyHealth = 0
        print(f"\nPlayer Health: {playerHealth}")
        print(f"Enemy Health: {enemyHealth}\n")

    #Player wins
    if enemyHealth <= 0:
        charInfoDict[enemyName][HEALTH] = 0
        print(f"The ground shakes as the {enemyName} falls to the ground in defeat.")
    
    #Enemy wins
    if playerHealth <= 0:
        print("You scream your last words as your soul escapes your body!")
        print("""
        ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
        ███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
        ██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
        ██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
        ██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
        ███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
        ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
        ███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
        ██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
        ██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
        ██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
        ███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄
        ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
        ┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼
        ┼┼┼┼┼┼████▄┼┼┼▄▄▄▄▄▄▄┼┼┼▄████┼┼┼┼┼┼┼
        ┼┼┼┼┼┼┼┼┼▀▀█▄█████████▄█▀▀┼┼┼┼┼┼┼┼┼┼
        ┼┼┼┼┼┼┼┼┼┼┼█████████████┼┼┼┼┼┼┼┼┼┼┼┼
        ┼┼┼┼┼┼┼┼┼┼┼██▀▀▀███▀▀▀██┼┼┼┼┼┼┼┼┼┼┼┼
        ┼┼┼┼┼┼┼┼┼┼┼██┼┼┼███┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼
        ┼┼┼┼┼┼┼┼┼┼┼█████▀▄▀█████┼┼┼┼┼┼┼┼┼┼┼┼
        ┼┼┼┼┼┼┼┼┼┼┼┼███████████┼┼┼┼┼┼┼┼┼┼┼┼┼
        ┼┼┼┼┼┼┼┼▄▄▄██┼┼█▀█▀█┼┼██▄▄▄┼┼┼┼┼┼┼┼┼
        ┼┼┼┼┼┼┼┼▀▀██┼┼┼┼┼┼┼┼┼┼┼██▀▀┼┼┼┼┼┼┼┼┼
        ┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼
        ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼\n""")
        sys.exit()
    
    playerHealth = 30
    print("\nCongratulations! You have won this fight!\n")
    print("You feel your body shiver as your health restores.")
    print("It is time to undergo more adventures.")
    killedEnemyCount += 1

    #Checking if the game is beaten
    if killedEnemyCount == enemyCounter:
        finishedGame(killedEnemyCount)


def displayLocation(loc):
    
    print(f"\n{loc}")
    print('=' * len(loc) + "\n")

    #Room's description
    print('\n'.join(textwrap.wrap(worldRooms[loc][DESC], SCREEN_WIDTH)))

    #Items on the ground
    if worldRooms[loc].get(GROUND) != None:
        if len(worldRooms[loc][GROUND]) > 0:

            for item in worldRooms[loc][GROUND]:
                print("\n" + allItems[item][GROUNDDESC])

    #Showing which characters are in the room, recording undiscovered ones
    if worldRooms[loc].get(CHARACTERS) != None:

        for eachCharacter in worldRooms[loc][CHARACTERS]:
            
            if eachCharacter not in charInfoDict:
                discoveredChar = {}
                for item in allCharacters[eachCharacter]:
                    discoveredChar[item] = allCharacters[eachCharacter][item]
                    charInfoDict[eachCharacter] = discoveredChar
            
            if charInfoDict[eachCharacter][HEALTH] != 0:

                print("\n" + allCharacters[eachCharacter][CHARDESC])

                #Instantly going into battle mode if creature is not friendly
                if allCharacters[eachCharacter].get(FRIEND, True) == False:
                    currentEnemyHealth = allCharacters[eachCharacter][HEALTH]
                    battleMode(eachCharacter, currentEnemyHealth)
            else:
                print(f"\nThe bones of a slain {eachCharacter.lower()} lie abandoned.")

    #Seeing exits
    exits = []
    for direction in (NORTH, SOUTH, EAST, WEST, UP, DOWN):
        if direction in worldRooms[loc].keys():
            exits.append(direction.title())
    print()
    for direction in (NORTH, SOUTH, EAST, WEST, UP, DOWN):
        if direction in worldRooms[location]:
            print('%s: %s' % (direction.title(), worldRooms[location][direction]))


def moveDirection(direction):
    #Changing location
    global location

    if direction in worldRooms[location]:
        print('You move to the %s.' % direction)
        location = worldRooms[location][direction]
        displayLocation(location)
    else:
        print('You cannot move in that direction')

#Getting descriptions of items
def getAllDescWords(itemList):
    itemList = list(set(itemList))
    descWords = []
    for item in itemList:
        descWords.extend(allItems[item][DESCWORDS])
    return list(set(descWords))

def getAllFirstDescWords(itemList):
    itemList = list(set(itemList))
    descWords = []
    for item in itemList:
        descWords.append(allItems
        [item][DESCWORDS][0])
    return list(set(descWords))

def getFirstItemMatchingDesc(desc, itemList):
    itemList = list(set(itemList))
    for item in itemList:
        if desc in allItems[item][DESCWORDS]:
            return item
    return None

def getAllItemsMatchingDesc(desc, itemList):
    itemList = list(set(itemList))
    matchingItems = []
    for item in itemList:
        if desc in allItems[item][DESCWORDS]:
            matchingItems.append(item)
    return matchingItems

#Command line prompts
class TextAdventureCmd(cmd.Cmd):
    prompt = '\n>> '

    #If an invalid input is given
    def default(self, arg):
        print('Sorry, what did you say? Type "help" for a list of commands.')

    def do_quit(self, arg):
        return True

    def help_combat(self):
        print('This game implements a "hit" or "stand" system. Use this to your advantage (and try to win). There are also weapons for you to pick up and use.')

    def help_talking(self):
        print("To talk to a non-enemy character, simply type 'talk <character>'.")
    
    def help_moving(self):
        print("To move, type in north, east, south, west, up or down.")
    
    def help_looking(self):
        print("""You can look at the room overview with 'look'.
You can also look at objects on the ground with 'look' and then the name of the object.
You can look at items within your inventory with 'look' and the item.
Looking to see what directions lie ahead can be done with 'look' and then the direction.""")


    #Movement Directions
    def do_north(self, arg):
        moveDirection('north')

    def do_south(self, arg):
        moveDirection('south')

    def do_east(self, arg):
        moveDirection('east')

    def do_west(self, arg):
        moveDirection('west')

    def do_up(self, arg):
        moveDirection('up')

    def do_down(self, arg):
        moveDirection('down')


    def do_inventory(self, arg):
        if len(inventory) == 0:
            print('Inventory:\n  (nothing)')
            return

        #Counting each distinct item in the inventory
        itemCount = {}
        for item in inventory:
            if item in itemCount.keys():
                itemCount[item] += 1
            else:
                itemCount[item] = 1

        #Deleting duplicates in the inventory
        print('Inventory:')
        for item in set(inventory):
            if itemCount[item] > 1:
                print('  %s (%s)' % (item, itemCount[item]))
            else:
                print('  ' + item)


    def do_take(self, arg):
        global weaponCount

        itemToTake = arg.lower()
        if itemToTake == '':
            print('Sorry, what would you like to take? Enter "look" to see the items on the ground here.')
            return

        cantTake = False

        #Get the item name that the player's command describes
        for item in getAllItemsMatchingDesc(itemToTake, worldRooms[location][GROUND]):
            if allItems[item].get(TAKEABLE, True) == False:
                cantTake = True
                continue

            print('You take %s.' % (allItems
            [item][SHORTDESC]))
            worldRooms[location][GROUND].remove(item) #Remove from the ground
            inventory.append(item) #Add to inventory

            if allItems[item].get(WEAPON) != None:
                weaponCount += 1

            return

        if cantTake:
            print('You cannot take "%s".' % (itemToTake))
        else:
            print('That is not on the ground.')

    def complete_take(self, text):
        possibleItems = []
        text = text.lower()

        #If the user has only typed "take" but no item name
        if not text:
            return getAllFirstDescWords(worldRooms[location][GROUND])

        #Description words for ground items matching command text 
        for item in list(set(worldRooms[location][GROUND])):
            for descWord in allItems[item][DESCWORDS]:
                if descWord.startswith(text) and allItems[item].get(TAKEABLE, True):
                    possibleItems.append(descWord)

        return list(set(possibleItems))
    

    def do_talk(self, arg):
        #Random generator for simple character speech
        talkSynonyms = ["says", "tells you", "declares", "utters", "affirms", "expresses"]

        targetChar = arg.lower().strip()
        availableChar = []
        creatureExists = False

        if CHARACTERS in worldRooms[location]:
            if targetChar.title() in worldRooms[location][CHARACTERS]:

                for discoveredChar in charInfoDict:
                    if charInfoDict[discoveredChar][HEALTH] != 0:

                        if discoveredChar not in availableChar:
                            availableChar.append(discoveredChar.lower().strip())

        #If character can be found
        if targetChar in availableChar:
            randomDialogue = random.choice(allCharacters[targetChar.title()][CHARDIALOGUE])
            print(f'The {targetChar.title()} {random.choice(talkSynonyms)}: "{randomDialogue}"')
            creatureExists = True

        if creatureExists == False:
            print("Sorry, the character you entered does not exist here. Please try again.")

    #Drop an item onto the ground
    def do_drop(self, arg):
        global weaponCount
        itemToDrop = arg.lower()
        invDescWords = getAllDescWords(inventory)

        if itemToDrop not in invDescWords:
            print('You do not have "%s" in your inventory.' % (itemToDrop))
            return

        #Get the item name that the player's command describes
        item = getFirstItemMatchingDesc(itemToDrop, inventory)
        if item != None:
            print('You drop %s.' % (allItems
            [item][SHORTDESC]))
            inventory.remove(item) #Remove from inventory
            worldRooms[location][GROUND].append(item) #Add to the ground

            if allItems[item].get(WEAPON) != None:
                weaponCount -= 1

    def complete_drop(self, text, line):
        possibleItems = []
        itemToDrop = text.lower()

        #Get a list of all "description words" for each item in the inventory
        invDescWords = getAllDescWords(inventory)
        print(invDescWords)

        for descWord in invDescWords:
            if line.startswith('drop %s' % (descWord)):
                return []

        if itemToDrop == '':
            return getAllFirstDescWords(inventory)

        #Description words for ground items matching command text
        for descWord in invDescWords:
            if descWord.startswith(text):
                possibleItems.append(descWord)

        return list(set(possibleItems))
        

    def do_look(self, arg):

        #Reprinting an area description for the "look" command
        lookingAt = arg.lower()
        if lookingAt == '':
            displayLocation(location)
            return

        if lookingAt == 'exits':
            for direction in (NORTH, SOUTH, EAST, WEST, UP, DOWN):
                if direction in worldRooms[location]:
                    print('%s: %s' % (direction.title(), worldRooms[location][direction]))
            return

        if lookingAt in ('north', 'west', 'east', 'south', 'up', 'down'):
            if lookingAt.startswith('n') and NORTH in worldRooms[location]:
                print(worldRooms[location][NORTH])
            elif lookingAt.startswith('w') and WEST in worldRooms[location]:
                print(worldRooms[location][WEST])
            elif lookingAt.startswith('e') and EAST in worldRooms[location]:
                print(worldRooms[location][EAST])
            elif lookingAt.startswith('s') and SOUTH in worldRooms[location]:
                print(worldRooms[location][SOUTH])
            elif lookingAt.startswith('u') and UP in worldRooms[location]:
                print(worldRooms[location][UP])
            elif lookingAt.startswith('d') and DOWN in worldRooms[location]:
                print(worldRooms[location][DOWN])
            else:
                print('There is nothing in that direction.')
            return

        #See if the item being looked at is on the ground at this location
        item = getFirstItemMatchingDesc(lookingAt, worldRooms[location][GROUND])
        if item != None:
            print('\n'.join(textwrap.wrap(allItems
            [item][LONGDESC], SCREEN_WIDTH)))
            return

        #See if the item being looked at is in the inventory
        item = getFirstItemMatchingDesc(lookingAt, inventory)
        if item != None:
            print('\n'.join(textwrap.wrap(allItems
            [item][LONGDESC], SCREEN_WIDTH)))
            return

        print('You do not see that nearby.')


    def complete_look(self, text, line):
        possibleItems = []
        lookingAt = text.lower()

        #Get describing words for inventory items
        invDescWords = getAllDescWords(inventory)
        groundDescWords = getAllDescWords(worldRooms[location][GROUND])

        for descWord in invDescWords + groundDescWords  + [NORTH, SOUTH, EAST, WEST, UP, DOWN]:
            if line.startswith('look %s' % (descWord)):
                return []

        if lookingAt == '':
            possibleItems.extend(getAllFirstDescWords(worldRooms[location][GROUND]))
            for direction in (NORTH, SOUTH, EAST, WEST, UP, DOWN):
                if direction in worldRooms[location]:
                    possibleItems.append(direction)
            return list(set(possibleItems))

        #Get a list of all "description words" for ground items matching the command text so far
        for descWord in groundDescWords:
            if descWord.startswith(lookingAt):
                possibleItems.append(descWord)


        #Check matching directions
        for direction in (NORTH, SOUTH, EAST, WEST, UP, DOWN):
            if direction.startswith(lookingAt):
                possibleItems.append(direction)

        #Get "description words" list for inventory items matching the command text so far
        for descWord in invDescWords:
            if descWord.startswith(lookingAt):
                possibleItems.append(descWord)

        return list(set(possibleItems))

#What the program will run while starting up
if __name__ == '__main__':
    print('\nExploring the Unknown:')
    print('A Simple Text-Based RPG Game\n')
    print('====================')
    print("To move around, simply type in 'north', 'south', 'east' and 'west'.")
    print("To pick items up, type in 'take' and the name of the item. If you would like to drop an item, print 'drop' and the name of the item.")
    print("To talk to characters in the game, type 'talk' and the character you would like to talk to.\n")
    print("In this game, you can look at the room overview with 'look'.")
    print("You can also look at objects on the ground with 'look' and then the name of the object.")
    print("You can look at items within your inventory with 'look' and the item.")
    print("Looking to see what directions lie ahead can be done with 'look' and then the direction.")
    print('(Type "help" for commands.)')
    print()
    displayLocation(location)
    TextAdventureCmd().cmdloop()
    print('\nThanks for playing\n')