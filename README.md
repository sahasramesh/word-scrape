# word-scrape
Python program that takes in letters as input and returns every word that can be made with those letters. Inspired by the iPhone game Wordscapes. 

## Set up notes
In order to run any of this code, you will to have Python 3 or later installed on your computer. Click [here](https://www.python.org/downloads/) to download.

After downloading Python, download the word_finder.py and everyword.rtf files in this repository. Move them to the Documents file on your computer. 

Next open the Command Prompt or Terminal (depending on if you're using a Windows computer or a Mac). 

Start by opening the location of the program file by typing

`cd Documents/` 

Press enter and type in the following command:

`python3 word_finder.py`

Upon pressing enter, a window will pop up that will prompt you to enter letters. Now all you have to do is enter the letters you want and the program will search through a list of over 58,000 words for words that match your letters.

After closing the window, if you look at your Command Prompt/Terminal, you should see some output that tells you how long the program ran for, how many letter combinations were computed, and how many words were generated.

## Files
- **word_finder.py** - This is the main file that includes all the logic.
- **everyword.rtf** - This is a text file containing over 58,000 words. This file is referenced in word_finder.py and is looped through for every possible occurence of the inputted letters.
- **wordscrapelogo.icns** - A macOS icon version of the WordScrape logo
- **wordscrapelogo.png** - A png version of the WordScrape logo

