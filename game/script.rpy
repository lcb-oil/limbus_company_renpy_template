

init python:
    # Handle different character sprite heights
    # Adjust these numbers if the heights seem wrong to you.
    character_offsets = {
        "don": -150, # Don's spear is so tall, her sprite is special
        "faust": 280,
        "test": 0,
        "greg": 330,
        "heath": 230,
        "dad": 220,
        "sancho": 430,
        "yi": 230,
        "ishmael": 350,
        "outis": 230
    }
    # How high characters will jump for their special animations
    jump_height = 50
    # How far from the side of the screen character sprites should be placed 
    x_axis_offset = 0.2
    # Predefined waits to create timing for character lines
    shortWait = 0.3 
    longWait = 0.5 
    # "Characters per second" shown when typing out text
    # You can change this per character or line for various effects
    default_cps = 25 
    # How long the final credits roll lasts
    credits_duration = 25.0

# Define a background image
image bg pcorplot = Transform("images/p-corp-lot.png", fit="contain")

# Define default location
default current_location = "Backstreets of P Corp."

# When a character is done speaking, apply this transform to darken the sprite as in-game
transform darken:
    matrixcolor TintMatrix("#444444")

# If a character starts speaking again, apply this transform to remove the darker tint. 
transform light_tint:
    matrixcolor TintMatrix("#ffffff")

# Define custom transforms for character positioning
# There's probably a better way to do this, but here it is.
transform left_top_don:
    xalign x_axis_offset
    yalign 0.0
    yoffset character_offsets["don"]

transform right_top_don:
    xalign 1.0 - x_axis_offset
    yalign 1.0
    yoffset character_offsets["don"]

transform left_top_dad:
    xalign x_axis_offset
    yalign 0.0
    yoffset character_offsets["dad"]

transform right_top_dad:
    xalign 1.0 - x_axis_offset
    yalign 0.0
    yoffset character_offsets["dad"]

transform left_top_sancho:
    xalign x_axis_offset
    yalign 0.0
    yoffset character_offsets["sancho"]
    
transform right_top_sancho:
    xalign 1.0 - x_axis_offset
    yalign 0.0
    yoffset character_offsets["sancho"]

transform right_top_heath:
    # a little more offset for Heathcliff's wide bat
    xalign 1.0 - x_axis_offset + .1
    yalign 0.0
    yoffset character_offsets["heath"]

transform left_top_yi:
    xalign x_axis_offset
    yalign 0.0
    yoffset character_offsets["yi"]

transform right_top_yi:
    xalign 1.0 - x_axis_offset
    yalign 0.0
    yoffset character_offsets["yi"]

transform left_top_ishmael:
    xalign x_axis_offset
    yalign 0.0
    yoffset character_offsets["ishmael"]

transform right_top_ishmael:
    xalign 1.0 - x_axis_offset
    yalign 0.0
    yoffset character_offsets["ishmael"]

transform left_top_outis:
    xalign x_axis_offset
    yalign 0.0
    yoffset character_offsets["outis"]

transform right_top_outis:
    xalign 1.0 - x_axis_offset
    yalign 0.0
    yoffset character_offsets["outis"]

transform left_top_heath:
    xalign x_axis_offset
    yalign 0.0
    yoffset character_offsets["heath"]

transform left_top_faust:
    xalign x_axis_offset + 0.1
    yalign 0.0
    yoffset character_offsets["faust"]

transform left_top_greg:
    xalign x_axis_offset
    yalign 0.0
    yoffset character_offsets["greg"]

# Define a jumping animation for the two Quixotes
transform dad_jump:
    xalign x_axis_offset
    yalign 0.0
    yoffset character_offsets["dad"]
    ease 0.2 yoffset (character_offsets["dad"] - jump_height)  
    ease 0.2 yoffset character_offsets["dad"]
    ease 0.2 yoffset (character_offsets["dad"] - jump_height)  
    ease 0.2 yoffset character_offsets["dad"]

transform sancho_jump:
    xalign 1.0 - x_axis_offset
    yalign 0.0
    yoffset character_offsets["sancho"]
    ease 0.2 yoffset (character_offsets["sancho"] - jump_height)  
    ease 0.2 yoffset character_offsets["sancho"]
    ease 0.2 yoffset (character_offsets["sancho"] - jump_height)  
    ease 0.2 yoffset character_offsets["sancho"]

# Sancho vibrates with excitement talking about Fixers...
transform sancho_vibrate:
    xalign 1.0 - x_axis_offset
    yalign 0.0
    yoffset character_offsets["sancho"]
    linear 0.05 xoffset 3
    linear 0.05 xoffset -3
    linear 0.05 xoffset 3
    linear 0.05 xoffset -3
    linear 0.05 xoffset 3
    linear 0.05 xoffset -3
    linear 0.05 xoffset 3
    linear 0.05 xoffset -3
    linear 0.05 xoffset 0

transform sancho_vibrate_more:
    xalign 1.0 - x_axis_offset
    yalign 0.0
    yoffset character_offsets["sancho"]
    linear 0.05 xoffset 6
    linear 0.05 xoffset -6
    linear 0.05 xoffset 6
    linear 0.05 xoffset -6
    linear 0.05 xoffset 6
    linear 0.05 xoffset -6
    linear 0.05 xoffset 6
    linear 0.05 xoffset -5
    linear 0.05 xoffset 0

# This function plays the click sound each time the player
# clicks to advance to the next line, just like in-game. 
init python:
    def callbackcontinue(ctc, **kwargs):
        if ctc == "end":
            renpy.music.play("audio/next-click-sfx.wav", channel="sound")

style character_name_shadow:
    is say_label
    outlines [(0, "#000000", 2,2)]

# By applying this style, text without a speaker defined will be
# centered, just like Dante's thoughts in-game. 
style narrator:
    xalign 0.5
    textalign 0.5
    yalign 0.6

# -- CHARACTER DEFINITIONS --

# The Narrator (text with no speaker)
define narrator = Character(None, 
    what_style="narrator",
    what_prefix="{cps=[default_cps]}",
    ctc="check_selected_foreground",
    ctc_position="nestled",
    callback=callbackcontinue)

# Proper characters
# --------------------------------------------------------
# When you add a new character here, be sure to add a title
# to the top of dialogue_screens.rpy in the company_affiliations list
# so that it will be displayed automatically! 
# --------------------------------------------------------
define don = Character("Don Quixote",   # Name, as displayed in the game
    color="#fddbb3",                  # Color that the character's name is written in
    nameboxbg_background="#a39a1bff", # Color of the text box behind the character name
    who_style="character_name_shadow",  # Style applied to the character's name
    what_prefix="{cps=[default_cps]}",  # Set the characters per second the character speaks in
    ctc="check_selected_foreground",    # Icon that will be shown when the player can click to continue
    ctc_position="nestled",             # Where the click to continue icon is shown (nestled next to text)
    callback=callbackcontinue)          # functions called when the player clicks to continue
define faust = Character("Faust", 
    color="#fddbb3", 
    nameboxbg_background="#a97b7ac2", 
    who_style="character_name_shadow",
    what_prefix="{cps=[default_cps]}",
    ctc="check_selected_foreground",
    ctc_position="nestled",
    callback=callbackcontinue)
define dad = Character("Don Quixote (Sr.)",
    color="#fddbb3",
    nameboxbg_background="#6d1515",
    who_style="character_name_shadow",
    what_prefix="{cps=[default_cps]}",
    who_size=gui.dad_name_text_size,
    ctc="check_selected_foreground",
    ctc_position="nestled",
    callback=callbackcontinue)
define heath = Character("Heathcliff",
    color="#fddbb3",
    nameboxbg_background="#4e3076da",
    who_style="character_name_shadow",
    what_prefix="{cps=[default_cps]}",
    ctc="check_selected_foreground",
    ctc_position="nestled",
    callback=callbackcontinue)
define yi = Character("Yi Sang",
    color="#fddbb3",
    nameboxbg_background="#a3afb3c9",
    who_style="character_name_shadow",
    what_prefix="{cps=[default_cps]}",
    ctc="check_selected_foreground",
    ctc_position="nestled",
    callback=callbackcontinue)
define greg = Character("Gregor",
    color="#fddbb3",
    nameboxbg_background="#44270ca6",
    who_style="character_name_shadow",
    what_prefix="{cps=[default_cps]}",
    ctc="check_selected_foreground",
    ctc_position="nestled",
    callback=callbackcontinue)
define hermann = Character("Hermann",
    color="#d5001e",
    nameboxbg_background="#2a274269",
    who_style="character_name_shadow",
    what_prefix="{cps=[default_cps]}",
    ctc="check_selected_foreground",
    ctc_position="nestled",
    callback=callbackcontinue)
define ishmael = Character("Ishmael",
    color="#fddbb3",
    nameboxbg_background="#dd8407d8",
    who_style="character_name_shadow",
    what_prefix="{cps=[default_cps]}",
    ctc="check_selected_foreground",
    ctc_position="nestled",
    callback=callbackcontinue)
define dosquixotes = Character("Dos Quixotes",
    color="#fddbb3",
    nameboxbg_background="#a39a1bff",
    who_style="character_name_shadow",
    what_prefix="{cps=[default_cps]}",
    ctc="check_selected_foreground",
    ctc_position="nestled",
    callback=callbackcontinue)
define outis = Character("Outis",
    color="#fddbb3",
    nameboxbg_background="#325339c9",
    who_style="character_name_shadow",
    what_prefix="{cps=[default_cps]}",
    ctc="check_selected_foreground",
    ctc_position="nestled",
    callback=callbackcontinue)

label start:
    don "."

label scenario_begin:
    play music "audio/Welcome Back.wav" fadein 1.0
    $ current_location = "Backstreets of P Corp." # Use a line like this to change the location text
    scene bg pcorplot with dissolve
    show don normal at left_top_don

    # This example shows a way to change character sprites in the middle of a line being shown.
    don "At long last... After such a complex battle,{nw}"
    show don puzzled at left_top_don
    don "At long last... After such a complex battle,{fast} requiring much reading and extensive comprehension of enemy passives,{nw}"
    show don normal at left_top_don
    don "At long last... After such a complex battle, requiring much reading and extensive comprehension of enemy passives,{fast} we have arrived at our most well-fought victory!"

    show outis mad at right_top_outis
    # Darken - makes the character's sprite darker when not speaking
    # zorder 0 - moves the character to the back, so that speaking characters appear on top 
    show don normal at darken, left_top_don zorder 0
    outis "To think that we would have to ask the Manager to authorize the use of our Color Fixer identities, just to take down some bookworm Feathers with fancy toys!"

    hide outis
    show ishmael question at right_top_ishmael
    ishmael "I have {i}never{/i} seen swords used that way before."
    show ishmael question at darken, right_top_ishmael zorder 0
    show don sad at left_top_don
    don "..."
    show don contemplate at left_top_don
    don "Father hath finally been avenged, his body recovered unto me."

    hide ishmael
    show don contemplate at darken, left_top_don zorder 0
    show heath normal at right_top_heath zorder 1
    heath "Lass..."

    show heath normal at darken, right_top_heath zorder 0
    show don contemplate at light_tint, left_top_don zorder 1
    don "Having thus come to the conclusion of my quest, I shall now return Rocinante to its rightful bearer... after these many years."

    hide don
    hide heath

    "After Don Quixote dismounted Rocinante, she reverently placed them down where her father's body lay."
    stop music fadeout 1.0
    "Then, suddenly, there was an explosion of golden light!"

    "SHWOOM!"
    "VOOSH!"

    show dad gah at light_tint, left_top_dad zorder 1 with dissolve
    dad "Oh goodness, does that sting!"

    show dad gah at darken, left_top_dad zorder 0
    show sancho happy at right_top_sancho
    don "Father?!"

    show sancho happy at darken, right_top_sancho zorder 0
    show dad normal at light_tint, left_top_dad zorder 1
    dad "Sancho! Thank you for taking Rocinante with you on your adventure, just as I had asked."
    show dad happy at light_tint, left_top_dad zorder 1
    dad "With my recharged EGO returned to me, I have regained the strength to make a full recovery!"

label the_explanation:
    play music "audio/Team Energy.wav" fadein 1.0
    hide sancho
    show dad normal at darken, left_top_dad zorder 0
    show heath normal at right_top_heath
    heath "Uhh... explain to me how that works?"

    show heath normal at darken, right_top_heath zorder 0
    hide dad
    show sancho sincerehappy at left_top_sancho
    don "Hundreds and hundreds of years of accumulated blood and power, all channeled into Rocinante —"
    
    hide sancho
    show faust normal at left_top_faust
    faust "Faust attributes it to the living will of the inherited blood within Don Quixote, combined with the highly preserved state of the body —"

    hide heath
    show yi softsmile at right_top_yi
    show faust normal at darken, left_top_faust zorder 0
    yi "Her heart's true and enduring wish to be reunited with her father has brought them together once more!"
    
    show yi normal at darken, right_top_yi zorder 0
    show faust normal at light_tint, left_top_faust zorder 1
    faust "..."
    
    hide faust
    show heath normal at left_top_heath
    show yi normalright at darken, right_top_yi zorder 0
    heath "..."
    
    show heath normal at darken, left_top_heath zorder 0
    show yi smile at light_tint, right_top_yi zorder 1
    yi "T-though upon reflection, my fellow's other conjectures do seem quite plausible as well..."
    
    show yi normal at darken, right_top_yi zorder 0
    show heath normal at light_tint, left_top_heath zorder 1
    heath "Wow, bang-up explanation, guys."
    show heath huh at light_tint, left_top_heath zorder 1
    heath "What I meant was... Didn't the White Nights and Dark Days happen not that long ago? How would this guy have manifested EGO if he was locked away for hundreds of years...?"
    show heath question at light_tint, left_top_heath zorder 1
    heath "Does that explanation even fit in with the canon at all?"

    hide yi

    show heath question at darken, left_top_heath zorder 0
    show dad normal at right_top_dad
    dad "If you don't manage to manifest an EGO after multiple hundreds of years of personal torment,"
    show dad smile at right_top_dad
    dad "If you don't manage to manifest an EGO after multiple hundreds of years of personal torment,{fast} I'm going to have to declare that a skill issue."

    hide dad
    show heath normal at darken, left_top_heath zorder 0
    show ishmael smile at right_top_ishmael zorder 1
    ishmael "This is the most fortunate thing to happen to us since Hermann took Ahab and Nelly to get proper therapy!"

    hide heath
    show greg sweat at left_top_greg
    show ishmael smile at darken, right_top_ishmael zorder 0
    greg "Thanks again for that, Mom..."

    hide ishmael
    show greg sweat at darken, left_top_greg zorder 0
    show hermann smile at right_top_heath
    hermann "Anything for my wonderful son!"

    hide greg
    hide hermann
    show dad normal at left_top_dad
    dad "Well, with that out of the way... Do make a space for me on your transport, won't you?"

    show ishmael question at right_top_ishmael
    show dad normal at darken, left_top_dad zorder 0
    ishmael "... What? You're coming with us?"

    show dad normal at light_tint, left_top_dad zorder 1
    show ishmael question at darken, right_top_ishmael zorder 0
    dad "Why wouldn't I?"
    show dad sadeyes
    dad "I think it would be wise for me to... leave this place. Urgently."

    show ishmael smile at right_top_ishmael
    show dad sadeyes at darken, left_top_dad zorder 0
    ishmael "This is incredible! With a First Kindred joining us, we'll be able to put an end to this Wing War once and for all!"
    show dad normal at left_top_dad zorder 1
    show ishmael smile at darken, right_top_ishmael zorder 0
    dad "A war you say? How nostalgic."
    show dad happy at left_top_dad zorder 1
    dad "Of course I'd be happy to assist my Daughter..."
    show dad happy at darken, left_top_dad zorder 0
    hide ishmael
    show sancho lookdown at right_top_sancho
    "For some reason, Don Quixote tenses up."
    show dad happy at left_top_dad zorder 1
    show sancho lookdown at darken, right_top_sancho zorder 0
    dad "... and her beloved"
    show dad smile at left_top_dad zorder 1
    show sancho wince at darken, right_top_sancho zorder 0
    dad "... and her beloved{fast} {i}family of twelve{/i}!"
    show dad smile at darken, left_top_dad zorder 0
    show sancho sadsigh at light_tint, right_top_sancho zorder 1
    don "{size=20}...Haah... I will never hear the end of that one...{/size}"

    show outis smug at right_top_outis zorder 1
    hide sancho
    outis "Taking into consideration that we still have 27 charged Golden Boughs at our disposal, we'll plan to deploy Don Quixote after the next Jia Family Tactical Orbital Laser Strike..."
    show dad normal at left_top_dad zorder 1
    show outis smug at darken, right_top_outis zorder 0
    dad "Some type of sky-bound weapon?"
    hide outis
    show sancho normal at darken, right_top_sancho zorder 0
    dad "Sancho! Does that not remind you of the legend of Bartholomew, Fixer of the East Seven Association?"
    show dad happy at left_top_dad zorder 1
    dad "...and his companion, an eagle, which espied the weak points of many a military formation from a safe distance!"
    show sancho wince at light_tint, right_top_sancho zorder 1
    show dad normal at darken, left_top_dad zorder 0
    stop music fadeout 1.0
    don "Haah... Father, please."
    show sancho starssmallsmile at light_tint, sancho_vibrate zorder 1
    play music "audio/Sueño Imposible 3.wav" fadein 1.0
    don "Haah... Father, please.{fast} Your information is horribly outdated!"
    show sancho starshappy at light_tint, sancho_vibrate_more zorder 1
    # Changing the characters per second (CPS) for just these lines allows Don Quixote to talk twice as fast and share her excitement
    don "{cps=[default_cps*2]}There's so much more to tell you about!{/cps}"
    don "{cps=[default_cps*2]}In modern times, it rather brings to mind the High Altitude Zwei Defense Array — which was crafted by none other than the newest and most famous flight-based Workshop...{/cps}"
    show dad normal at left_top_dad zorder 1
    show sancho starshappy at darken, right_top_sancho zorder 0
    dad "Flight-based Workshop, you say?"
    show dad huh at left_top_dad zorder 1
    dad "Have the humans discovered the secret to flight?"
    show dad huh at darken, left_top_dad zorder 0
    show sancho starsnormal at light_tint, right_top_sancho zorder 1
    don "'Tis quite the tale unto itself!"
    show sancho starshappy at light_tint, right_top_sancho zorder 1
    don "{cps=[default_cps*2]}We begin nary a year ago. The Tres Association, under a most clandestine commission from the Hana Association...{/cps}"
    show dad smile at dad_jump
    show sancho starssmallsmile at sancho_jump
    dosquixotes "A heh heh heh! Heh heh heh!"
    "In no time, their in-depth Fixer discussion becomes unintelligible to anyone else but the two of them."
    show dad happy at light_tint, left_top_dad zorder 1
    show sancho normal at darken, right_top_sancho zorder 0
    stop music fadeout 5.0
    dad "You simply must tell me about even more of your recent travels over some ice cream!"
    dad "Come along, all of you! You deserve my thanks."

    scene black with dissolve
    $ current_location = "Ice Cream Parlor"
    dad "After this, I believe I shall take a well deserved rest."
    dad "Wake me after a time, won't you Sancho?"
    don "Of course, Father."
    dad "I think that 10 or 20 years should suffice."
    don "..."
    don "... Father."
    dad "Oh, don't look at me so! I'm clearly joking!"
    dad "Five years should be plenty!"
    "FIN!"
    
    # Roll the credits
    scene black with dissolve
    show screen credits_scroll
    pause credits_duration
    hide screen credits_scroll
    return

# Define the credids screen and rolling animation for the end of the game
transform credits_scroll:
    ypos 1200 
    linear credits_duration ypos -2800

screen credits_divider():
    null height 10
    frame:
        background "#ffffff55"
        xsize 400
        ysize 2
        xalign 0.5
    null height 10

screen credits_scroll():
    style_prefix "credits"
    
    frame at credits_scroll:
        background "#000000aa"
        has vbox
        spacing 40
        xalign 0.5
        yalign 0.5
        xsize 800 
        ysize 600
        
        text "Credits" size 60 color "#ffffff"
        
        text "Written and Scripted by" size 40 color "#ffffff"
        text "lcb_oil" size 40 color "#b01c37"
        
        # Divider
        use credits_divider()
        
        text "Art" size 40 color "#ffffff"
        text "Project Moon" size 30 color "#ffffff"
        text "(With some not-so-skillful edits by lcb_oil)" size 20 color "#ffffff"
        
        # Divider
        use credits_divider()
        
        text "Music" size 40 color "#ffffff"
        text "Project Moon" size 30 color "#ffffff"
        
        # Divider
        use credits_divider()
        
        text "Engine" size 40 color "#ffffff"
        text "Made with Ren'Py v[renpy.version_only]" size 20 color "#ffffff"

        text "GUI Setup Based Upon" size 30 color "#ffffff"
        text "Easy Renpy GUI Template by Feniks" size 30 color "#b01c37"
        text "https://feniksdev.itch.io/easy-renpy-gui" size 20 color "#ffffff"

        # Divider
        use credits_divider()
        
        text "Special Thanks" size 40 color "#ffffff"
        text "Lunartique07" size 30 color "#4e3076"
        text "Thank you for making game assets available to everyone!" size 20 color "#ffffff"
        text "Limbus Company Wiki" size 30 color "#c40000"
        text "https://limbuscompany.wiki.gg/" size 20 color "#ffffff"
        text "... and you!" size 40 color "#ffffff"

        use credits_divider()

        text "Thank you to everyone who has supported my works." size 20 color "#686868"
        text "It means the world to me!" size 20 color "#686868"

        use credits_divider()
        
        text "This game is a fan-made parody of Limbus Company, and is not associated with Project Moon." size 20 color "#ffffff"
        text "Happy April Fools Day 2025!" size 20 color "#ffffff"


style credits_vbox:
    spacing 40
    xalign 0.5
    yalign 0.5

style credits_text:
    text_align 0.5
    xalign 0.5