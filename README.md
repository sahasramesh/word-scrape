# word-scrape
Python program that takes in letters as input and returns every word that can be made with those letters. Inspired by the iPhone game Wordscapes. 

## Set up notes
To run this file, download the word_finder.py and everyword.rtf files in this repository. Move them to the Documents file on your computer. 

Next open the Command Prompt or Terminal (depending on if you're using a Windows computer or a Mac). 

Before running the program, you will have to install a module called PySimpleGUI in order to be able to run the graphical user interface that is built into word_finder.py. To do so, type in

`pip install PySimpleGUI`

Press enter. Once you see a message saying that the software was successfully installed, you are ready to run the program. Start by opening the location of the program file by typing

`cd Documents/` 

Press enter and type in the following command:

`python3 word_finder.py`

Upon pressing enter, a window will pop up that will prompt you to enter letters. Now all you have to do is enter the letters you want and the program will search through a list of over 58,000 words for words that match your letters.

Whenever you want to stop the progam, click the Exit button in the bottom left. If you look at your Command Prompt/Terminal, you should see some output that tells you how long the program ran for, how many letter combinations were computed, and how many words were generated.

## Files
- **word_finder.py** - This is the main file that includes all the logic.
- **everyword.rtf** - This is a text file containing over 58,000 words. This file is referenced in wor_finder.py and is looped through for every possible occurence of the inputted letters.
- **someword** - This is a test file contaning much fewer words than everyword.rtf that I used to test initial versions of word_finder.py.
