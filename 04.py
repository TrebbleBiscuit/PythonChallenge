# http://www.pythonchallenge.com/pc/def/linkedlist.php

import urllib
#for x in range(400):
#    print x
nothing = 12345
for x in range(400):
    print("Plugging in " + str(nothing))
    page = urllib.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + str(nothing)).read()
    if page == "Yes. Divide by two and keep going.":
        nothing = str(int(nothing)/2)
    else:
        nothing = ""
        for x in page:
            if x.isdigit():
                nothing += x
    nothing = nothing[-5:]
    print page,
    if nothing == "":
        exit()
