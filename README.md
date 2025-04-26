# Limbus Company Visual Novel Template
Based on my April Fool's Day project, now you can create your own Limbus Company stories! 

![Demo footage of the included April Fool's Day story](documentation\conjectures.gif)

## Features
- Replicates the Limbus Company Story UI (mostly!)
- Basic hookups to show character titles and location names
- Plays the "click" sound when the player advances to the next screen of text
- Comes with my example story **Top Secret Canto XXVIII Preview Footage** to show you how it's used!

## Requirements
### Renpy
[Download Ren'py for free here!](https://www.renpy.org/latest.html)

Renpy is a free Python-based visual novel game engine. It has been used to make some really popular games like Doki Doki Literature Club and Slay the Princess. 

Renpy is needed to play your game (and to publish it for other people to play).

### Text Editor

You can use any text editor to create your game.

I use [Visual Stuidio Code](https://code.visualstudio.com/).

## Getting Started
1. Download this code. You can click on the green **Code** button in the upper right corner, then choose **Download ZIP**.
2. Unzip all of the code somewhere on your computer
3. Open Ren'py
4. Click **preferences** in the lower right corner
5. In the **General** tab, find the setting for **Projects Directory**. You can either change this to where you unzipped this code, or put the unzipped code into the folder that's already set here
6. You can now run this game with Ren'py. Edit it, and have fun! 

## Need Help?
Ren'py comes with a tutorial and an example game called The Question. Both of these projects show you how to do lots of things -- check out and play with their scripts!

If you need more help you can contact me:

- Tumblr - `lcb-oil`
- Discord - `lcb_oil`

I can't help with all issues, but I'd be happy to help point the way! 

## FAQs
### Do I need to know how to program to use this?
Not very much. I've done my best to leave useful comments to help you get started!

### What files should I edit?
You will probably only need to edit two files:

| File Name | Details |
|--|--|
|`script.rpy`| Holds the story text. Defines the characters and their names and colors that are shown while they are speaking.  Do most of your creating here!|
|`dialogue_screens.rpy` | Controls the UI. Also has the character's titles (like "Sinner #3"). You may want to edit this if you want to further cutomize the UI.

### Live Reloading
Once you've started the game from Ren'py, press `Shift + R` while playing it to enter live reload mode. 

Now when you save an update to your files, you'll see your changes appear automatically in the game. This makes it a lot more fun to edit!  

### Where can I find more character sprites, music, and other things from Limbus Company to add to the game?

| Location | Details |
|--|--|
| [Limbus Company Wiki](https://limbuscompany.wiki.gg/) | Character sprites are organized and easy to find on each page of the wiki. |
|[Lunartique07's Organized Limbus Company Assets](https://drive.google.com/drive/folders/1Nk9WWMxEcovs5Ewku5ICT1PbfByNcV_z?usp=sharing) | Absolutely everything from the game can be found here. Includes music, art, character sprites, UI elements, and much much more.| 

### How do I add more sprites to the game?
Add them to the `images` folder. After that you can use them in `script.rpy` using the name of the image.

### How do I create a title for a character, like "Sinner #3"?
They are set up in `dialogue_screens.rpy`. 

This is very unideal, sorry about the confusion...

### How do I change the location text in the upper left corner?
Add a line to your `script.rpy` like this:
```python
$ current_location = "Backstreets of P Corp." 
```

### How do I give my game a different name?
Check out `options.rpy`.

Replace the name `limbus_company_format` in `config.name`, `build.name`, and `config.save_directory`.

### How do I open the menu in the game?
I hid the default Ren'py menu, since it doens't match the Limbus Company style.

You can still access it by right-clicking while playing.

### When text gets too long, like character names or titles, parts of the UI break!
Apologies, this is really not very well optimized since I made it in a day. I hope it's still fun to play with! 

### Can I make a pull request?
Absolutely. I welcome any contributions.

### Are there any limits to how I can use this?
All code and text authored by me is free for you to use without attribution or limitation. 

Made with help from the lovely template [Easy Renpy GUI Template](https://feniksdev.itch.io/easy-renpy-gui), which Feniks also kindly allows all to freely use. 

Limbus Company (c) Project Moon

