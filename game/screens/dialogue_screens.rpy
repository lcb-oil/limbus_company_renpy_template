## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

# Text for the company affiliations that appear above character names
init python:
    company_affiliations = {
        "Yi Sang": "Sinner #1",
        "Faust": "Sinner #2",
        "Don Quixote": "Sinner #3",
        "Heathcliff": "Sinner #6",
        "Ishmael": "Sinner #7",
        "Outis": "Sinner #12",
        "Gregor": "Sinner #13",
        "Don Quixote (Sr.)": "La Manchaland",
        "Hermann": "N Corp Therapist",
        "Dos Quixotes": "Two of Them!",
    }

# Define custom transforms
transform title_text_transform:
    rotate -10
    ypos -935
    xpos -340

transform nameplate_rotation:
    rotate -5

transform company_rotation:
    rotate -5

screen say(who, what):
    style_prefix "say"

    window:
        id "windowbg"
    window:
        id "window"
            
        # Faux Menu buttons, not actually clickable
        add "gui/limbus/red-ui-ribbon.png":
            xzoom 0.18
            yzoom 0.4
            rotate 0
            ypos -790 
            xpos 1350
        add "gui/limbus/ui_arm_flat.png":
            zoom 0.35 
            rotate 0
            ypos -820 
            xpos 1470
        add "gui/limbus/limbus-options-menu.png":
            zoom 0.35 
            rotate 0
            ypos -780 
            xpos 1325   
        
        # Location text label background
        add "gui/limbus/title-frame.png":
            zoom 1
            rotate -10
            ypos -950 
            xpos -360

        frame:
            background None
            at title_text_transform
            xysize (400, 60)
            
            text "[current_location]":
                color '#fddbb3'
                size 38
                font gui.name_text_font
                outlines [(0, "#000000", 2,2)]
                text_align 0.5
                xalign 0.5
                yalign 0.5
                layout "subtitle" 
                xsize 380 
                line_spacing -5
                adjust_spacing True 
                substitute True
                slow_cps 0

        add "gui/limbus/name-holder-arm.png":
            zoom 0.35 
            rotate 80
            ypos -940 
            xpos -280

        # If there is a named speaker, show the name box and colored background
        if who is not None:
            window:
                id "nameboxbg2"
                style "nameboxbg2"
                at nameplate_rotation
            window:
                id "nameboxbg"
                style "nameboxbg"
                at nameplate_rotation
            window:
                id "namebox"
                style "namebox"
                text who id "who"
                at nameplate_rotation
            window:
                id "companybg"
                style "companyboxbg"
                at company_rotation
            window:
                id "company"
                style "companybox"
                text company_affiliations.get(who, "") style "company_label"
                at company_rotation

            add "gui/limbus/title-holder-arm.png":
                zoom 0.28
                rotate -5
                ypos -70
                xpos -365  
            add "gui/limbus/name-holder-arm.png":
                zoom 0.35 
                rotate -5
                ypos -56 
                xpos -430  

        text what id "what" style "limbus_text"

    add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')
    config.character_id_prefixes.append('nameboxbg')

# Style for the dialogue window, shows the actual spoken text
style window:
    color "#dfbf97"
    xalign 0.5
    yalign 1.0
    xysize (1231, 277)
    padding (40, 10, 40, 40)
    xfill True
    yfill True
    background Transform("gui/limbus/dialogue-background.png", fit="contain", xalign=0.5, yalign=0.5)

style window:
    color "#0000009a" 
    xalign 0.5
    yalign 1.0
    xysize (1231, 277)
    padding (40, 10, 40, 40)
    xfill True
    yfill True

style say_dialogue:
    adjust_spacing False
    ypos 60

# The style for dialogue said by the narrator (ie no character)
style say_thought:
    is say_dialogue

# Style for the box containing the speaker's name
style namebox:
    xfill True
    yfill True
    xpos -273 
    ypos -122
    xysize (280, 105)
    background Transform(Frame("gui/limbus/name-frame.png", 5, 5, 5, 5, tile=False, xalign=0.0), blend="multiply")
    padding (5, 5, 5, 5)

init python:
    nameboxbg_pos = {
        'xpos': -260,
        'ypos': -105,
        'xysize': (252, 78)
    }

# Multiple backgrounds to create the color background effect under character names
style nameboxbg2:
    xpos nameboxbg_pos['xpos']
    ypos nameboxbg_pos['ypos'] 
    xfill True
    yfill True
    xysize nameboxbg_pos['xysize']
    background Transform("#00000073", blend="normal")
    padding (5, 5, 5, 5)

style nameboxbg:
    xpos nameboxbg_pos['xpos']
    ypos nameboxbg_pos['ypos']
    xfill True
    yfill True
    xysize nameboxbg_pos['xysize']
    background Transform("#ffef23", blend="add")
    padding (5, 5, 5, 5)

style say_label:
    color '#f93c3e'
    xalign 0.5
    yalign 0.5
    size gui.name_text_size
    font gui.name_text_font

# Style for the box containing the company affiliation
style companybox:
    xpos -294
    ypos -170
    xysize (250, 63)
    background Transform(Frame("gui/limbus/title-frame.png", 5, 5, 5, 5, tile=False, xalign=0.0), blend="normal")
    padding (5, 5, 5, 5)

style companyboxbg:
    xpos -294
    ypos -170
    xysize (250, 50)
    background Transform(Frame("#291b0f", 5, 5, 5, 5, tile=False, xalign=0.0), blend="normal")
    padding (5, 5, 5, 5)

# Style for the text with the company's name
style company_label:
    color '#9f6a3b'
    xalign 0.5
    yalign 0.5
    size gui.company_text_size
    font gui.name_text_font
    outlines [(0, "#000000", 2,2)]
    text_align 0.5
    xsize 300
    fit_first True
    kerning 1.5

## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            textbutton _("Back") action Rollback()
            textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Prefs") action ShowMenu('preferences')


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
# init python:
    # config.overlay_screens.append("quick_menu")

default quick_menu = False

style quick_hbox:
    xalign 0.5
    yalign 1.0 yoffset -8
    spacing 8

style quick_button:
    background None
    padding (15, 6, 15, 0)

style quick_button_text:
    size 21
    selected_color '#f93c3e'
    idle_color "#aaa"

## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox
        spacing 15

        use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit True

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = 6

# The style for the NVL "textbox"
style nvl_window:
    is default
    xfill True yfill True
    background "gui/nvl.png"
    padding (0, 15, 0, 30)

# The style for the text of the speaker's name
style nvl_label:
    is say_label
    xpos 645 xanchor 1.0
    ypos 0 yanchor 0.0
    xsize 225
    min_width 225
    textalign 1.0

# The style for dialogue in NVL
style nvl_dialogue:
    is say_dialogue
    xpos 675
    ypos 12
    xsize 885
    min_width 885

# The style for dialogue said by the narrator in NVL
style nvl_thought:
    is nvl_dialogue

style nvl_button:
    xpos 675
    xanchor 0.0