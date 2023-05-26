import random
intro = ('''     _                                             
    | |                                            
    | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
    | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | | | | (_| | | | | (_| | | | | | | (_| | | | |
    |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |                      
                       |___/    
    ''')
hang_1 = '''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
hang_2 = '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
'''
hang_3 = '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
'''
hang_4 = '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
'''
hang_5 = '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
'''
hang_6 = '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
'''
hang_7 = '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
'''
hang = [hang_1,hang_2,hang_3,hang_4,hang_5,hang_6,hang_7]
words = ['apple', 'handsome', 'blueberry', 'mountain', 'water', 'kitchen', 'tiger', 'elephant', 'pappaya', 'coconut', 'honeybee', 'abruptly', 'absurd','abyss','affix','askew', 
'avenue', 'awkward', 'axiom', 'azure', 'bagpipes', 'bandwagon', 'banjo', 'bayou', 'beekeeper', 'bikini', 'blitz', 'blizzard', 'boggle', 'bookworm', 'boxcar', 'boxful', 'buckaroo', 'buffalo', 'buffoon', 'buxom', 'buzzard', 'buzzing', 'buzzwords', 'caliph', 
'cobweb', 'cockiness', 'croquet', 'crypt', 'curacao', 'cycle', 'daiquiri', 'dirndl', 'disavow', 'dizzying', 'duplex', 'dwarves', 'embezzle', 'equip', 'espionage', 'euouae', 'exodus', 'faking', 'fishhook', 'fixable', 'fjord', 'flapjack', 'flopping', 'fluffiness', 
'flyby', 'foxglove', 'frazzled', 'frizzled', 'fuchsia', 'funny','gabby', 'galaxy', 'galvanize', 'gazebo', 'giaour', 'gizmo', 'glowworm', 'glyph', 'gnarly', 'gnostic', 'gossip', 'grogginess', 'haiku', 'haphazard', 'hyphen', 'iatrogenic', 'icebox', 'injury', 
'ivory', 'ivy', 'jackpot', 'jaundice', 'jawbreaker', 'jaywalk', 'jazziest', 'jazzy', 'jelly', 'jigsaw', 'jinx', 'jiujitsu', 'jockey', 'jogging', 'joking', 'jovial', 'joyful', 
'juicy', 'jukebox', 'jumbo', 'kayak', 'kazoo', 'keyhole', 'khaki', 'kilobyte', 'kiosk', 
'kitsch', 'kiwifruit', 'klutz', 'knapsack', 'larynx', 'lengths','lucky', 'luxury', 'lymph', 
'marquis', 'matrix', 'megahertz','microwave', 'mnemonic', 'mystify', 'naphtha', 'nightclub', 'nowadays', 'numbskull', 'nymph', 'onyx', 'ovary', 'oxidize', 'oxygen', 'pajama', 'peekaboo','phlegm', 'pixel', 'pizazz', 'pneumonia', 'polka', 'pshaw', 'psyche', 
'puppy', 'puzzling', 'quartz', 'queue', 'quips', 'quixotic', 'quiz', 'quizzes', 'quorum', 
'razzmatazz', 'rhubarb', 'rhythm', 'rickshaw','schnapps', 'scratch', 'shiv', 'snazzy', 'sphinx', 'spritz', 'squawk', 'staff', 'strength', 'strengths', 'stretch', 'stronghold', 'stymied', 'subway', 'swivel','syndrome', 'thriftless', 'thumbscrew', 'topaz', 'transcript', 'transgress', 'transplant', 'triphthong', 'twelfth', 'twelfths', 'unknown', 
'unworthy', 'unzip', 'uptown', 'vaporize', 'vixen', 'vodka', 'voodoo', 'vortex', 'voyeurism', 'walkway', 'waltz', 'wave', 'wavy', 'waxy', 'wellspring', 'wheezy', 'whiskey', 
'whizzing', 'whomever', 'wimpy', 'witchcraft', 'wizard', 'woozy', 'wristwatch', 'wyvern', 
'xylophone', 'yachtsman', 'yippee', 'yoked','youthful', 'yummy', 'zephyr', 'zigzag', 'zigzagging', 'zilch', 'zipper', 'zodiac', 'zombie']
choice_word = list(random.choice(words))
guess_word = ""
all_guess = []
chance = 0
end_of_game = False
print(intro)
from replit import clear
from string import ascii_lowercase
for dash in range(len(choice_word)):
    guess_word += "_"
while not end_of_game:
    guess = input("Guess a letter: ")
    all_guess.append(guess)
    clear()
    print(f"You have tried: {all_guess}\n")
    new = ""
    if guess in guess_word and guess in list(ascii_lowercase):
        print(guess_word)
        print(f"You have already guessed {guess}, try another letter")
    else:
        for char in range(len(choice_word)):
            if choice_word[char] == guess:
                new = list(guess_word)
                new[char] = guess
                guess_word = ''.join(new)
        print(guess_word)
    if guess not in choice_word and guess in list(ascii_lowercase):
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        chance += 1
    if guess not in list(ascii_lowercase):
        print("Please input an Alphabet")
    if chance > 5:
        end_of_game = True
        print(f"\u001b[31mYou lose\nThe word was {''.join(choice_word)}")
    if "_" not in guess_word:
        end_of_game = True
        print("\u001b[32mYou won")
    print(hang[chance])
