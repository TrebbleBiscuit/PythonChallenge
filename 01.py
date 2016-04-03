# http://www.pythonchallenge.com/pc/def/map.html

"""
# First Method

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
phrase = raw_input("Enter phrase to translate: ")
for x in phrase:
    if x == " " or x == "." or x == "(" or x == ")":
        print x
    else:
        for y in range(len(alphabet)):
            if alphabet[y].lower() == x:
                try:
                    print alphabet[y+2].lower(),
                except IndexError:
                    print alphabet[y-24].lower(),
"""

# Better Method
from string import maketrans
alph = "abcdefghijklmnopqrstuvwxyz"
alphshift = "cdefghijklmnopqrstuvwxyzab"
translator = maketrans(alph, alphshift)
phrase = raw_input("Enter phrase to translate: ").lower()
print phrase.translate(translator)
