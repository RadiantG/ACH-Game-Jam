# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

default mood = 1
default gem_color = 1
default amethyst = False
default emerald = False
default ruby = False
default emerald_wrong_puzzle = False
default emerald_wrong_fear = False
default fuck = False
default how = False
default need = False
default dont = False
default done = False
default give = False

define n = Character("Nico")

image nico_character:
    LiveComposite(
        (1700, 1100),
    (0, 2), ConditionSwitch(
                    #mood
                            "mood == 1", "nico_standard",
                            "mood == 2", "nico_happy",
                            "mood == 3", "nico_sad",
                        ),)

image gem:
    LiveComposite(
        (1100, 800),
    (0, 2), ConditionSwitch(
                    #mood
                            "gem_color == 1", "gem_amethyst",
                            "gem_color == 2", "gem_emerald",
                            "gem_color == 3", "gem_ruby",
                        ),)                        

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene forest

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show nico_character

    # These display lines of dialogue.

    n "My name is Nico."

    $ mood = 2

    n "I'll try to be open!"

    $ mood = 3

    n "But it's tough for me..."

    $ mood = 1

    n "Anyway... Let's begin!" 

    show gem

    n "This, is a gem. To get them, we must answer the riddles of the forest."

    hide gem

    $ mood = 3

    n "I read all of the riddles, but I can't really figure them out."

    $ mood = 1
    
    n "We will need all three gems: amethyst, emerald, and ruby, to unlock the secret power of the woods."

menu:
    n "Please! Will you help me?"
    "Yes! I will help you.":
        n "Thank you!"
        "There seems to be three riddles engraved in the trees. Which riddle would you like to solve first?"
        jump puzzles
    "No. I'm just going to leave.":
        jump end_game

label puzzles:
    $ mood = 1
menu:
    "Make a choice."
    "Amethyst puzzle" if amethyst == False:
        jump amethyst_puzzle
    "Emerald puzzle" if emerald == False:
        jump emerald_puzzle
    "Ruby puzzle" if ruby == False:
        jump ruby_puzzle
    "Open the secret forest door with the gems." if ruby == True and emerald == True and amethyst == True:
        jump ending1
    "Walk away from everything. You don't want it anymore." if ruby == True and emerald == True and amethyst == True:
        jump ending2
    "Give the gems to Nico and let him decide what to do." if ruby == True and emerald == True and amethyst == True:
        jump ending3

label amethyst_puzzle:
    "Welcome to the Amethyst puzzle"
menu:
    n "What has a bark sharper than its bite?"
    "An angry dog.":
        jump amethyst_incorrect
    "A tree trunk.":
        jump amethyst_correct1
    "Peppermint bark candy.":
        jump amethyst_incorrect

label amethyst_correct1:
    $ mood = 2
    n "Yeah, that was right."
    $ mood = 3
    n "I think I understand now. Because an angry dog bite would hurt a lot..."
    $ mood = 2
    n "But a tree doesn't bite at all!"
    $ mood = 1
    n "One more question for this puzzle."
menu:
    n "I have a point, but only one. I never shine in the sun."
    "The puzzles of the forest.":
        jump amethyst_correct2
    "The amethyst gemstone.":
        jump amethyst_incorrect
    "A pebble in the forest depths.":
        jump amethyst_incorrect 

label amethyst_correct2: 
    $ mood = 2
    n "Correct, nice job!"
    n "I think because an amethyst would shine in the sun, it had to be the puzzles."
    n "Because the only reason we are doing this is to unlock the forest's secrets."
    $ gem_color = 1
    show gem
    n "Wow! There it is!"
    $ mood = 1
    n "Awesome job with that."
    $ amethyst = True
    "You earned an amethyst!"
    hide gem
    jump puzzles

label amethyst_incorrect:
$ mood = 3  
n "Sorry, that's wrong..."
$ mood = 1
menu:
    "The puzzle reset."
    "Try again":
        $ mood = 1
        jump amethyst_puzzle
    "Try different puzzle":
        $ mood = 1
        jump puzzles

label emerald_puzzle:
    "Welcome to the Emerald puzzle"
menu:
    n "What is your biggest fear?"
    "Being alone.":
        jump emerald_correct1
    "Being incompetent.":
        jump emerald_correct1
    "Something that I won't say.":
        jump emerald_correct1
    "I have no fears.":
        jump emerald_incorrect

label emerald_correct1:
    $ mood = 3
    n "Opening up can be scary."
    $ mood = 2
    n "But this time I think it helped us!"
    $ mood = 1
    n "Let's try doing that again with this last Emerald question."
menu:
    n "What is your biggest obstacle right now?"
    "The puzzles." if emerald_wrong_puzzle == False:
        $ emerald_wrong_puzzle = True
        jump emerald_incorrect
    "My fear." if emerald_wrong_fear == False:
        $ emerald_wrong_fear = True
        jump emerald_incorrect
    "The fact this question is playing games with me." if emerald_wrong_puzzle == True and emerald_wrong_fear == True:
        jump emerald_correct2


label emerald_incorrect:
$ mood = 3  
n "No.. The puzzle didn't like that."
$ mood = 1
n "I think we might need to open up to get this one right..."
menu:
    "The puzzle reset."
    "Try again":
        $ mood = 1
        jump emerald_puzzle
    "Try different puzzle":
        $ mood = 1
        jump puzzles

label emerald_correct2:
    $ mood = 2  
    n "Awesome!"
    n "I think here what we really needed was to show the courage to speak out against the puzzle!"
    $ mood = 1
    n "We found a pretty green gem."
    $ gem_color = 2
    show gem
    $ emerald = True
    "You earned an emerald!"
    hide gem
    jump puzzles

label ruby_puzzle:
    "Welcome to the Ruby puzzle"
    $ mood = 2
    n "Oh, this is the only one I got right the first time!"
    n "The answer is cake."
    $ mood = 1
menu:
    n "Which of these desserts is your favorite?"
    "Cake.":
        jump ruby_correct1_alt
    "Ice Cream.":
        jump ruby_correct1
    "Something else.":
        jump ruby_correct1

label ruby_correct1:
    n "Huh... are they all right?"
    $ mood = 3
    n "I feel cheated..."
    $ mood = 1
    n "Ok... last question."
    jump ruby_q2

label ruby_correct1_alt:
    $ mood = 2
    n "See??? Cake!"
    n "I got some skills at least."
    $ mood = 1
    n "Ok... last question."
    jump ruby_q2

label ruby_q2:
menu:
    n "Do you have the Amethyst gem?"
    "Yes." if amethyst == False:
        jump ruby_incorrect_alt
    "Yes." if amethyst == True:
        $ mood = 2
        n "We did it!"
        $ mood = 1
        n "Wait..."
        n "Huh?! Another question?!"
        jump ruby_correct2
    "No." if amethyst == False:
        jump ruby_incorrect
    "No." if amethyst == True:
        jump ruby_incorrect_alt

label ruby_correct2:
menu:
    n "Do you have the Emerald gem?"
    "If the trees have a vicious bite." if emerald == True:
        jump ruby_incorrect_alt
    "If all favorite desserts are valid." if emerald == True:
        n "I guess that's true. Every dessert is delicious."
        n "But wait... if the last answer was wrong..."
        n "That means... that wasn't the last question?"
        n "Oh, c'mon..."
        n "Another??"
        jump ruby_correct3
    "If I have no fear." if emerald == True:
        jump ruby_incorrect_alt
    "If this is the last question." if emerald == True:
        jump ruby_incorrect_alt
    "If the trees have a vicious bite." if emerald == False:
        jump ruby_incorrect 
    "If all favorite deserts are valid." if emerald == False:
        jump ruby_incorrect_alt
    "If I have no fear." if emerald == False:
        jump ruby_incorrect
    "If this is the last question." if emerald == False:
        jump ruby_incorrect

label ruby_correct3:
menu:
    n "Do you have the Ruby gem?"
    "Oh, fuck this shit!" if fuck == False:
        $ fuck = True
        jump ruby_correct3
    "How can you ask that? This is the Ruby gem puzzle!" if how == False:
        $ how = True
        jump ruby_correct3
    "Do I even really need it?" if need == False:
        $ need = True
        jump ruby_correct3
    "You already know I don't have it." if dont == False:
        $ dont = True
        jump ruby_correct3
    "I thought we were all done with these questions." if done == False:
        $ done = True
        jump ruby_correct3
    "Just give me the ruby." if give == False:
        $ give = True
        jump ruby_correct3
    "I am standing up for myself!" if fuck == True and how == True and need == True and dont == True and done == True and give == True:
        jump ruby_correct4
    "Yes?" if fuck != True or how != True or need != True or dont != True or done != True or give != True:
        jump ruby_incorrect_alt
    "I'm just going to leave." if fuck != True or how != True or need != True or dont != True or done != True or give != True:
        jump end_game

label ruby_incorrect:
$ mood = 3  
n "We need the gem."
jump ruby_reset

label ruby_incorrect_alt:
$ mood = 3  
n "The puzzle doesn't like liars."
jump ruby_reset

label ruby_reset:
menu:
    "The puzzle reset."
    "Try again":
        $ mood = 1
        jump ruby_puzzle
    "Try different puzzle":
        $ mood = 1
        jump puzzles

label ruby_correct4:
    $ mood = 2  
    n "You did it!"
    n "You solved the final riddle!"
    n "You stood up for yourself!"
    $ mood = 3
    n "That is what I needed to learn to do."
    $ mood = 2
    n "And I think you helped me get there too."
    $ mood = 1
    $ gem_color = 3
    show gem
    $ ruby = True
    "You earned a ruby!"
    hide gem
    "Suddenly a locked door appears to you."
    "It has three holes in the shapes of your three gems."
    jump puzzles
    # This ends the game.

label ending1:
    "You open the door and it is a mirror."
    "The answer was you all along."

    "Thank you for playing Wings of Change."
    "The end."
    jump end_game

label ending2:
    "You walk away from everything and leave."
    jump end_game

label ending3:
    "You give the gems to Nico and let him decide what to do."
    jump end_game

label end_game:
    return
