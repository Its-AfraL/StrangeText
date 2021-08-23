"""
MIT License

Copyright (c) 2021 Its-AfraL

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""

import time
import random
from colorama import Fore, Style
from pyfade import Fade, Colors
import os

logo = """
          ____   _                           _____           _ 
         |___ \_| |__ _ _ __   __ _ _ __  __|_   ______  ___| |
         / ___|__ |__` | '_ \ / _` | '_ \/ _ \| |/ _ \ \/ |__ |
        | (___ _| |  | | |_) | | | | |_) \__  | |\__  >  < _| |
         \____|__/   |_|_.__/|_| |_| .__/|___/|_||___/_/\_|__/ 
                                    \___|                      

        [µ] Created by AfraL : https://www.github.com/Its-AfraL
        [?] Generate Strange Text with random MAJ and low chars
        [$] Thanks for Use

"""

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def strange(text):
    """Function Created for StrangeText OpenSource Script

    This function is the used function used by StrangeText to generate strange text
    
    Work Method : - Function take first character of the text
                  - She generate a random number
                  - If this random number is 1, she lower the character and add him to strange_text output variable
                  - Else, she upper the character and add him to strange_text output variable

                  - She repeat that for all character in str variable

    Arguments :

                text : Text to make strange using this function
                
    """

    chars_number = int(len(text)) 
    random_number = int(random.randint(1,2))
        
    if random_number == 1:
        strange_text = text[0].lower()

    elif random_number == 2:
        strange_text = text[0].upper()

    else:
        raise ValueError

    for strange_range in range(1, chars_number):
        random_number = int(random.randint(1,2))
        
        if random_number == 1:
            strange_text = strange_text + text[int(strange_range)].lower()

        elif random_number == 2:
            strange_text = strange_text + text[int(strange_range)].upper()

        else:
            raise ValueError

    return strange_text

def main():
    """This is the main function of StrangeText OpenSource script

    Work Method :
                - First she show the CLI with ascii art
                - This function ask for a text to make strange
                - Then she just call the strange() function to make this text strange (see line 8)
                - She print the output to the user

    Arguments :
                - None
    
    """
    
    global text

    clear()
    print(Fade.Vertical(Colors.green_to_yellow, logo, speed=1))

    text = input(Fore.YELLOW + Style.BRIGHT + ">>> StRanGE TeXT.? ")
    text = str(text.lower())
    print(Fore.YELLOW + Style.NORMAL + "\n>>> [*] GenEraTING yoUR StrAnGE TeXt...")
    time.sleep(1)

    try:

        strange_text = strange(text=text)
        print(Fore.YELLOW+ Style.NORMAL + ">>> [+] SucCeSSFullY GeneRAteD yoUr sTrangE TeXT\n")

        print(Fore.YELLOW + Style.BRIGHT + "<? Basic Text     : " + Fore.GREEN + Style.BRIGHT + text)
        print(Fore.YELLOW + Style.BRIGHT + f"<? StrAnGe OutPuT : " +  Fore.GREEN + Style.BRIGHT + strange_text + Fore.WHITE + Style.NORMAL + "\n")

    except:

        print(Fore.RED + Style.NORMAL + "\n[-] ErrOr : Can'T MakE thIs TexT StrAnGe, rEtrY")


if __name__ == "__main__":
    try:
        main()
    except:
        print(Fore.RED + Style.NORMAL + "\n\n[INTERNAL ERROR] Quitting the script...")