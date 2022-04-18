#Defining constants
DESC = 'desc'
NORTH = 'north'
SOUTH = 'south'
EAST = 'east'
WEST = 'west'
UP = 'up'
DOWN = 'down'
GROUND = 'ground'
GROUNDDESC = 'grounddesc'
SHORTDESC = 'shortdesc'
LONGDESC = 'longdesc'
TAKEABLE = 'takeable'
DESCWORDS = 'descwords'
CHARACTERS = 'characters'
SCREEN_WIDTH = 100
HEALTH = 'health'
STRENGTH = 'strength'
FRIEND = 'friend'
CHARDESC = 'chardesc'
WEAPON = 'weapon'
DAMAGEAMPLIFIER = 'damageamplifier'
CHARDIALOGUE = 'chardialogue'

#Characteristics of each character, including enemies, in the game
allCharacters = {
    "Bull": {
        FRIEND: False,
        HEALTH: 100,
        CHARDESC: "Suddenly, an angry bull intimidates you with its horns!"
    },
    "Pirate": {
        FRIEND: False,
        HEALTH: 90,
        CHARDESC: "A pirate is threatened by your presence!"
    },
    "Witch": {
        FRIEND: False,
        HEALTH: 80,
        CHARDESC: "Suddenly, a witch curses at you!"
    },
    "Zombie": {
        FRIEND: False,
        HEALTH: 70,
        CHARDESC: "A zombie approaches you and tries to eat your brains!"
    },
    "Goat": {
        FRIEND: False,
        HEALTH: 45,
        CHARDESC: "Suddenly, a goat chases you to battle her!"
    },
    "Creature": {
        HEALTH: 20,
        CHARDESC: "A mysterious creature slyly smiles at you.",
        CHARDIALOGUE: ["The weather seems cold today.", "I don't think I've seen you before.", "I wonder how you got here!", "Wish I got to meet you before."]
    },
    "Neighbour": {
        HEALTH: 20,
        CHARDESC: "The neighbour appears friendly and inviting.",
        CHARDIALOGUE: ["Seems like you've been on a journey.", "Welcome, I haven't seen you around before!", "I hope you're enjoying your time here!", "Where have you been all this time?"]
    },
    "Wizard": {
        HEALTH: 20,
        CHARDESC: "A magical wizard stands still and appears to have noticed you.",
        CHARDIALOGUE: ["I really need to rehearse my spells more.", "Wish it was a bit warmer today.", "You don't appear to be a wizard.", "Haven't seen you around."]
    },
    "Nomad": {
        HEALTH: 20,
        CHARDESC: "A wandering nomad with no apparent destination passes by you.",
        CHARDIALOGUE: ["I wonder where you're going!", "I wish I was new to this place like you.", "How did I get here?", "You seem lost."]
    },
    "Robot": {
        HEALTH: 20,
        CHARDESC: "A robot seems to have some of his wires exposed but still continues walking on.",
        CHARDIALOGUE: ["Beep bop beep beep bop.", "01001000 01100101 01101100 01101100 01101111", "Beep beep beep!", "Beep bop beep bop?"]
    }
}

#Characteristics of all rooms in the game
worldRooms = {
    'Outside the Hut': {
        DESC: 'There is an unknown creature gazing at you from behind the forest leaves. An uneasy aura surrounds the outside of the hut.',
        NORTH: 'The Hut',
        SOUTH: 'Empty Field',
        GROUND: ['Glowing Leaf', 'Axe'],
        CHARACTERS: ['Creature']},

    'The Hut': {
        DESC: 'The hut is a compact and discreet place to be. You rub your nose from the scent of dust in the air.',
        EAST: "Neighbouring House",
        SOUTH: 'Outside the Hut',
        WEST: 'Left Town Road',
        GROUND: ['Table', 'Dying Flowers']},

    'Left Town Road': {
        DESC: 'From being abandoned for so long, you would expect the left town road to wear down. Somehow, it stands in place.',
        WEST: 'Viewing Tower',
        EAST: 'The Hut',
        GROUND: ['Wooden Bench'],
        CHARACTERS: ['Zombie']},

    'Viewing Tower': {
        DESC: 'A sturdy yet magical tower overshadows the horizon.',
        EAST: 'Left Town Road',
        WEST: "Wizard's Stone Path",
        UP: 'Top of the Viewing Tower',
        GROUND: ['Locket']},

    'Top of the Viewing Tower': {
        DESC: 'You can almost view the remnants of the gone civilisation at the top of the Viewing Tower.',
        DOWN: 'Viewing Tower',
        GROUND: ['Cannon'],
        CHARACTERS: ['Witch']},

    "Wizard's Stone Path": {
        DESC: "It was said that all of society once wandered along this path collecting spells. Now, it's almost desolate.",
        EAST: 'Viewing Tower',
        SOUTH: 'Forest',
        GROUND: ['Wand'],
        CHARACTERS: ['Wizard']},

    'Forest': {
        DESC: 'The howls of wolves become louder within the trees.',
        NORTH: "Wizard's Stone Path",
        SOUTH: 'Overgrown Path',
        CHARACTERS: ['Goat']},

    'Overgrown Path': {
        DESC: 'Moss covers the ground with a beautiful painting of green. The sun dries out the previously vivid murals on the path.',
        NORTH: 'Forest',
        EAST: 'Empty Field',
        GROUND: ['Sapling'],
        CHARACTERS: ['Robot']},

    'Empty Field': {
        DESC: 'You feel free running around in the empty field. Your paranoia almost goes away.',
        NORTH: 'Outside the Hut',
        WEST: 'Overgrown Path',
        EAST: 'Nature View Road',
        GROUND: ['Poppy'],
        CHARACTERS: ['Bull']
        },

    'Nature View Road': {
        DESC: 'The winding road goes along a steep hill. You wonder how much longer you have to walk.',
        NORTH: 'Waterfall',
        WEST: 'Empty Field',
        GROUND: ['Sword'],
        CHARACTERS: ['Nomad']},

    'Waterfall': {
        DESC: 'The rushing water of the waterfall overwhelms your ears. It appears to be never-ending.',
        NORTH: "Explorer's Path",
        SOUTH: 'Nature View Road',
        GROUND: ['Bottle of Water'],
        CHARACTERS: ['Pirate']},

    "Explorer's Path": {
        DESC: 'The never-ending view brings you excitement as you begin to understand explorers from the past.',
        WEST: 'Neighbouring House',
        SOUTH: 'Waterfall',
        GROUND: ['Compass']},

    'Neighbouring House': {
        DESC: 'The red brick stands out against the forest and captures your attention.',
        WEST: 'The Hut',
        EAST: "Explorer's Path",
        GROUND: ['Letter'],
        CHARACTERS: ['Neighbour']
        },
    }

#Characteristics of all items in the game
allItems = {
    'Glowing Leaf': {
        GROUNDDESC: 'A leaf glows brightly against the ground.',
        SHORTDESC: 'glowing leaf',
        LONGDESC: 'The leaf appears to be magical and really light to the touch.',
        DESCWORDS: ['leaf', "glowing leaf"]},

    'Creature': {
        GROUNDDESC: 'A creature hides behind the overgrowth.',
        SHORTDESC: 'a creature',
        TAKEABLE: False,
        LONGDESC: 'The creature mutters at your presence.',
        DESCWORDS: ['creature']},

    'Table': {
        GROUNDDESC: 'A table is placed on the ground.',
        SHORTDESC: 'a table',
        LONGDESC: 'The table seems to have sword marks on it. Who stabbed the table?',
        TAKEABLE: False,
        DESCWORDS: ['table']},

    'Dying Flowers': {
        GROUNDDESC: 'Dying flowers lie on the ground.',
        SHORTDESC: 'dying flowers',
        LONGDESC: 'A bouquet tied with string rests in your inventory, the flowers wilted and dry.',
        DESCWORDS: ['dying', 'dying flowers', 'flowers', 'dry']},

    'Wooden Bench': {
        GROUNDDESC: 'A wooden bench stands on the ground.',
        SHORTDESC: 'a wooden bench',
        LONGDESC: 'The wooden bench has stood up straight all these years despite the harsh weather conditions.',
        TAKEABLE: False,
        DESCWORDS: ['wooden', 'bench', 'wooden bench']},

    'Locket': {
        GROUNDDESC: 'A shattered locket lies on the ground.',
        SHORTDESC: 'a locket',
        LONGDESC: 'It appears there is no picture within the locket.',
        DESCWORDS: ['locket', 'shattered locket', 'chain', 'shattered']},

    'Cannon': {
        GROUNDDESC: 'The cannon stands strong on the ground.',
        SHORTDESC: 'a cannon',
        LONGDESC: 'You wonder how many enemies have been killed with this cannon.',
        TAKEABLE: False,
        DESCWORDS: ['cannon']},


    'Wand': {
        GROUNDDESC: 'A wand lies on the ground.',
        SHORTDESC: 'a wand',
        LONGDESC: 'The wand echoes the spells it has cast in the years before.',
        DESCWORDS: ['wand', 'long'],
        WEAPON: True,
        DAMAGEAMPLIFIER: 1.3
        },

    'Axe': {
        GROUNDDESC: 'An axe gently rests on the ground.',
        SHORTDESC: 'an axe',
        LONGDESC: 'It appears to have signs of wear and tear.',
        DESCWORDS: ['axe', 'weapon'],
        WEAPON: True,
        DAMAGEAMPLIFIER: 1.1
        },

    'Sapling': {
        GROUNDDESC: 'A sapling rests on the ground.',
        SHORTDESC: 'a sapling',
        LONGDESC: 'The plant is urging for you to take it home and plant it.',
        DESCWORDS: ['sapling', 'plant']},

    'Poppy': {
        GROUNDDESC: 'A poppy lies on the cold, hard ground.',
        SHORTDESC: 'a poppy',
        LONGDESC: 'The poppy smells like home. You wonder where home even is.',
        DESCWORDS: ['poppy', 'flower']},

    'Sword': {
        GROUNDDESC: 'A magical sword rests abandoned on the ground.',
        SHORTDESC: 'a sword',
        LONGDESC: 'The handle of the sword seems to be heavily scratched.',
        DESCWORDS: ['sword', 'magical', 'magical sword'],
        WEAPON: True,
        DAMAGEAMPLIFIER: 1.2
        },

    'Bottle of Water': {
        GROUNDDESC: 'A bottle of water rests on the ground.',
        SHORTDESC: 'a bottle of water',
        LONGDESC: 'The fresh water from the waterfall swirls within the glass.',
        DESCWORDS: ['bottle of water', 'water', 'bottle']},

    'Compass': {
        GROUNDDESC: 'A shattered compass lies on the ground.',
        SHORTDESC: 'a broken compass',
        LONGDESC: 'The broken compass continually faces west, not moving an inch.',
        DESCWORDS: ['compass', 'broken']},

    'Letter': {
        GROUNDDESC: 'A letter appears to have been lost on the ground.',
        SHORTDESC: 'a letter',
        LONGDESC: 'You squint your eyes but you still can\'t decipher the foreign language.',
        DESCWORDS: ['letter', 'note']},
    }