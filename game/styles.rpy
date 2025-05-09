################################################################################
## Initialization
################################################################################

## The init offset statement causes the initialization statements in this file
## to run before init statements in any other file.
init offset = -2

## Blink the bus icon for the click to continue (CTC) icon
image check_selected_foreground:
    "gui/limbus/bus_text_cursor.png"
    size (40, 40)
    alpha 1.0
    pause 0.5
    alpha 0.0
    pause 0.5
    repeat

## Calling gui.init resets the styles to sensible default values, and sets the
## width and height of the game.
init python:
    gui.init(1920, 1080)

define config.check_conflicting_properties = True

################################################################################
## GUI Configuration Variables
################################################################################
## Some choice gui values have been left in, to make them
## easier to adjust for accessibility purposes e.g. to allow
## players to change the default text font or size by rebuilding the gui.
## You may add more back if you need to adjust them, or find-and-replace
## any instances where they are used directly with their value.

# The text font for dialogue and choice menus
define gui.text_font = gui.preference("font", "DejaVuSans.ttf")
# The text font for buttons
define gui.interface_text_font = gui.preference("interface_font", "DejaVuSans.ttf")
# The default size of in-game text
define gui.text_size = gui.preference("size", 33)
# The font for character names
define gui.name_text_font = gui.preference("name_font", "Mikodacs.otf")
# The size for character names
define gui.name_text_size = gui.preference("name_size", 40)
define gui.dad_name_text_size = 35  # Custom size for Don Quixote Sr because his name is too long to fit
define gui.company_text_size = gui.preference("company_size", 28)

## Localization ################################################################

## This controls where a line break is permitted. The default is suitable
## for most languages. A list of available values can be found at
## https://www.renpy.org/doc/html/style_properties.html#style-property-language

define gui.language = "unicode"


################################################################################
## Style Initialization
################################################################################

init offset = -1

################################################################################
## Styles
################################################################################

style default:
    font gui.text_font
    size gui.text_size
    language gui.language
    color "#d7b993"

style input:
    adjust_spacing False

style hyperlink_text:
    hover_underline True
    color "#f93c3e"

style gui_text:
    color '#ffffff'
    size gui.text_size
    font gui.interface_text_font

style button:
    xysize (None, None)
    padding (0, 0)

style button_text:
    is gui_text
    yalign 0.5
    xalign 0.0
    ## The color used for a text button when it is neither selected nor hovered.
    idle_color '#888888'
    ## The color that is used for buttons and bars that are hovered.
    hover_color '#ff8335'
    ## The color used for a text button when it is selected but not focused. A
    ## button is selected if it is the current screen or preference value.
    selected_color '#ffffff'
    ## The color used for a text button when it cannot be selected.
    insensitive_color '#8888887f'

style label_text:
    is gui_text
    size 36
    color '#f93c3e'


style bar:
    ysize 38
    left_bar Frame("gui/bar/left.png", 6, 6, 6, 6, tile=False)
    right_bar Frame("gui/bar/right.png", 6, 6, 6, 6, tile=False)

style vbar:
    xsize 38
    top_bar Frame("gui/bar/top.png", 6, 6, 6, 6, tile=False)
    bottom_bar Frame("gui/bar/bottom.png", 6, 6, 6, 6, tile=False)

style scrollbar:
    ysize 18
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", 6, 6, 6, 6, tile=False)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", 6, 6, 6, 6, tile=False)
    unscrollable 'hide'

style vscrollbar:
    xsize 18
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", 6, 6, 6, 6, tile=False)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", 6, 6, 6, 6, tile=False)
    unscrollable 'hide'

style slider:
    ysize 38
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", 6, 6, 6, 6, tile=False)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize 38
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", 6, 6, 6, 6, tile=False)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding (6, 6, 6, 6)
    background Frame("gui/frame.png", 6, 6, 6, 6, tile=False)
