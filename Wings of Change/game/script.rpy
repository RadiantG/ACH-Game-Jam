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
default no = 0

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

    "Welcome to Wings of Change."
    "Note: This game does not have sound, but self-voicing assist can be toggled with the V button."
    "The volume of it can be changed with SHIFT+A."

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
    
    n "We will need all three gems: amethyst, emerald, and ruby, to unlock the secret power of the forest."

menu:
    n "Please! Will you help me?"
    "Yes! I will help you.":
        n "Thank you!"
        "There seems to be three riddles engraved in the trees. Which riddle would you like to solve first?"
        "A beginner should start with the amethyst puzzle."
        jump puzzles
    "No. I'm just going to leave.":
        call screen about
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
    n "Yeah, that was right!"
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
    $ mood = 1
    n "I think because an amethyst would shine in the sun, it had to be the puzzles."
    n "Because the only reason we're doing this is to unlock the forest's secrets."
    $ gem_color = 1
    show gem
    $ mood = 2
    n "Wow! There it is!"
    n "Awesome job with that!"
    $ amethyst = True
    "You earned an amethyst!"
    $ mood = 1
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
    "Try a different puzzle":
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
    $ mood = 2
    n "Right. Because everyone's afraid of something!"
    $ mood = 1
    n "Now for the last Emerald question."
menu:
    n "What is your biggest obstacle right now?."
    "The puzzles." if emerald_wrong_puzzle == False:
        $ emerald_wrong_puzzle = True
        jump emerald_incorrect
    "My fear." if emerald_wrong_fear == False:
        $ emerald_wrong_fear = True
        jump emerald_incorrect
    "The fact this question is playing games with me." if emerald_wrong_puzzle == True and emerald_wrong_fear == True:
        jump emerald_correct2


label emerald_incorrect:
if emerald_wrong_puzzle != False or emerald_wrong_fear != False:
    $ mood = 3
    if emerald_wrong_puzzle != True or emerald_wrong_fear != True:
        n "No.. The puzzle didn't like that."
        $ mood = 1
        n "I think we need to try again..."
if emerald_wrong_puzzle == True and emerald_wrong_fear == True:
    $ mood = 3
    n "No.. The puzzle still didn't like that."
    $ mood = 1
    
menu:
    "The puzzle reset."
    "Try again":
        $ mood = 1
        jump emerald_puzzle
    "Try a different puzzle":
        $ mood = 1
        jump puzzles

label emerald_correct2:
    n "So that's what it is..."
    $ mood = 2  
    n "Awesome!"
    n "I think here what we really needed was to show the courage to speak out against the puzzle!"
    $ mood = 1
    n "We found a pretty green gem."
    $ gem_color = 2
    show gem
    $ emerald = True
    $ mood = 2
    "You earned an emerald!"
    $ mood = 1 
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
    n "No, I said it was- wait."
    n "Huh...?"
    n "Are they all correct?"
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
    "If I have no fear." if emerald == True:
        jump ruby_incorrect_alt
    "If all favorite desserts are valid." if emerald == True:
        n "I guess that's true. Every dessert is delicious."
        $ mood = 3
        n "But wait... if the last answer was wrong..."
        $ mood = 1
        n "That means... that wasn't the last question?"
        $ mood = 3
        n "Oh, c'mon..."
        $ mood = 1
        jump ruby_correct3
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
        call screen about
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
    "Try a different puzzle":
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
    "Suddenly, a locked door appears to you."
    "It has three holes in the shapes of your three gems."
    jump puzzles
    # This ends the game.

label ending1:
    "You walk up to the door and put in the gems one by one."
    "Amethyst."
    "Emerald."
    "Ruby."
    "The door glows and shakes, opening up."
    "Tn front of you, all that is inside is a mirror."
    "..."
    "The answer was you all along."

    menu:
        "The answer was you all along."
        "The answer is... me?":
            menu:
                "The answer was you all along."
                "Isn't that a little cliché?":
                    label ending1_0:
                    menu:
                        "The answer was you all along."
                        "Accept the ending as is." if no != 5:
                            jump ending1_1
                        "Do not accept it." if no != 5:
                            $ no += 1
                            jump ending1_0
                        "Try something else." if no == 5:                        
                            menu:
                                "The answer was you all along."
                                "Break the mirror.":
                                    label mirror:
                                    "You charge forward and break the mirror."                                    
                                    scene black
                                    "Everything goes dark."
                                    n "What's going on?!"
                                    n "Why did you do that?!"
                                    n "I can't see!"
                                    "You try to find Nico, but you can't feel anything."
                                    $ no -= 1
                                    "A voice booms that belongs to neither of you."
                                    label final:
                                    menu:
                                        "{b}WHAT IS YOUR BIGGEST FEAR?{/b}"
                                        "Being alone.":
                                            scene forest
                                            hide nico_character
                                            show nico_character
                                            jump puzzles
                                        "Being incompetent.":
                                            scene forest
                                            hide nico_character
                                            show nico_character
                                            jump puzzles
                                        "The dark.":
                                            scene forest
                                            hide nico_character
                                            show nico_character
                                            jump mirror
                                        "Dying.":
                                            scene forest
                                            hide nico_character
                                            show nico_character
                                            jump ending1_0
                                        "Losing a friend.":
                                            scene forest
                                            hide nico_character
                                            show nico_character
                                            jump puzzles
                                        "Something that I won't say.":
                                            jump final
                                        "This.":
                                            scene forest
                                            hide nico_character
                                            show nico_character
                                            "Light refills the area, and Nico gets up dizzily after having fallen."
                                            $ mood = 3
                                            n "I am not sure what happened."
                                            n "Are you okay?"
                                            $ mood = 1
                                            menu:
                                                n "Are you okay?"
                                                "I think so.":
                                                    n "Okay, good."
                                                    $ mood = 3
                                                    n "But that was scary."
                                                    $ mood = 1
                                                    n "We should get out of here."
                                                    n "Why did you break the mirror?"
                                                    menu:
                                                        n "Why did you break the mirror?"
                                                        "I wanted to.":
                                                            n "You wanted to?"
                                                            $ mood = 3
                                                            n "This is ancient magic."
                                                            n "You put both of us in danger..."
                                                            menu:
                                                                n "You put both of us in danger..."
                                                                "I'm sorry.":
                                                                    n "I... need a little time to forgive you."
                                                                    $ mood = 1
                                                                    n "But I haven't forgot all of the good things either."
                                                                    n "Let's stick together for now, and get out of here."
                                                                "I'm not sorry.":
                                                                    n "Then suit yourself."
                                                                    hide nico_character
                                                                    "You leave without Nico, walking out of the forest alone."
                                                                    call screen about
                                                                    jump end_game
                                                        "I was frustrated.":
                                                            $ mood = 3
                                                            n "I am sorry that there wasn't more behind the door."
                                                            n "I wonder how I would've reacted."
                                                            $ mood = 1
                                                            n "Either way, we should get going."
                                                        "I wanted to see if there was something behind it.":
                                                            n "Was there?"
                                                            label barkwall:
                                                            "You look over at the shattered mirror and a thick tree trunk behind it."                                                          
                                                            menu:
                                                                "You look over at the shattered mirror and a thick tree trunk behind it."
                                                                "No.":
                                                                    n "Well, I guess it was worth a shot."
                                                                    n "But we should go."
                                                                    jump ending_secret
                                                                "I don't know.":
                                                                    jump barkwall
                                                        "Impulsive thought, and I acted on it.":
                                                            $ mood = 3
                                                            n "I know what you mean."
                                                            $ mood = 1
                                                            n "You helped me, I would be willing to help you too."
                                                            n "Y'now... learn to control that."
                                                            $ mood = 2
                                                            n "All things aside, I am glad I met you."
                                                            $ mood = 1
                                                            n "Let's get out of here."
                                                        "I don't know.":
                                                            $ mood = 3
                                                            n "I don't either..."
                                                            $ mood = 1
                                                            n "But either way, the magic here doesn't seem safe."
                                                            n "We should go."
                                                    jump ending_secret
                                                        
                                        "I have no fears.":
                                            "Then you will not fear this."
                                            jump end_game
                                        

label ending1_1:
    "You have learened the true power is from within."
    "Learned that even when it's hard, you can stand up for yourself."
    "And most imprtantly, learned that all favorite desserts are valid."
    "You did it!"
    "Thank you for playing Wings of Change."
    
    call screen about
    jump end_game

label ending_secret:
    "You and Nico run out of the forest together."
    "You unlocked the secret ending."

    "Thank you for playing Wings of Change."
    
    call screen about
    jump end_game


label ending2:
    "You think back on everything that has happened."
    "And you decide that don't need the secrets of the forest after all."
    "Not after all of those trials and tricks."
    menu:
        "I can't do this. I just want to leave.":
            n "Okay. You don't have to."
        "Change your mind.":
            jump puzzles

    hide nico_character
    "You decide to walk away from everything, and leave with your head held high."

    "Thank you for playing Wings of Change."

    call screen about
    jump end_game

label ending3:
    "You give the gems to Nico and let him decide what to do."

    $ mood = 2
    n "Oh!"
    n "Me?!"
    $ mood = 3
    n "Oh, wow..."
    $ mood = 1
    n "I can't thank you enough for all of the help you've given me."
    n "I..."

    "Nico walks up to the door and puts in the gems one by one."
    "Amethyst."
    "Emerald."
    "Ruby."

    "The door glows and shakes, opening up. Nico is looking in disbelief."
    "There is no tunnel, or cave, or anything of the sort."
    "Instead, Nico is looking face to face with... himself."
    "It's a mirror."

    "Nico reaches out and touches it gently with a talon."
    n "That's me, huh?"
    n "It's been awhile since I really looked at myself."
    n "I..."
    n "Is that it? The secret was inside us all along?"
    n "Isn't that a little cliché?"

    menu:
        n "Isn't that a little cliché?"
        "Sure. But the writers only had a few days to write this.":
            n "That's fair. But also kind of nice."
            n "Thank you, writers."
            n "And thank you, player."
            n "Both of you made choices that helped me take a step towards loving myself fully."

    "Thank you for playing Wings of Change."
    
    call screen about
    jump end_game

label end_game:
    return
