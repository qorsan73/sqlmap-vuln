import os
os.system("pip install googlesearch-python")
os.system("pip install termcolor")
from googlesearch import search
from termcolor import colored
os.system('clear')
print ("\033[1;33m...................................................................................................")
print ("...................... .. ..........................................................................")
print ("...................  .7B#! .........................................................................")
print (".................  :?#@B7:..........................................................................")
print ("...............  ^Y#@#!  ...........................................................................")
print (".............  ^5@@@@&P~  .......   ................................................................")
print (".............!P@&Y~5&@@@G!. ...  ~?7:  .............................................................")
print ("........... 7&#J:   ^5&@@@G!. .!P@@@&Y^  ...........................................................")
print (".............::  ...  ^Y&@@@GJG@&5^!G@@5^  .........................................................")
print ("............. ........  :J&@@@@B^   .!G@@5^  .......................................................")
print ("......................  :J&@&@@@B?.    ~P@@P~  .....................................................")
print ("..................... ^5&@G7:J#@@@#?:    ~P@@P~  ...................................................")
print ("......................G@@5.   :?#@@@#J:    ^P@@P~. .................................................")
print ("......................:J#@B?.   .?B@@@#J: .!G@@@@G!. ...............................................")
print ("......................  :J#@#?.   .7B@@@&YB@@#\033[1;31mBB#@\033[1;33m@G!. ..................................")
print ("........................  :?#@#J:   .!#@@@@#\033[1;31mBGGGGB#@\033[1;33m@B7. ................................")
print ("........................... .?#@&J: ^Y#@&B\033[1;31mGGGGGBBBGB#@\033[1;33m@B7.  .............................")
print ("............................. .7B@&P&@#GP\033[1;31mGGGBBBBBBGGB#@\033[1;33m@B?.  ............................")
print ("............................... .7B@@#J\033[1;31m?YPPGBBBBBBBBBBGB#@@\033[1;33m#?:  .........................")
print ("................................. .!G@@P7\033[1;31m7YPGBBBBGGGGGGGGB#&\033[1;33m@#J:  .......................")
print ("................................... .!G@@P7\033[1;31m75PPGBGGGGGGGGGGG#\033[1;33m&@#J:  .....................")
print (".....................................  ~P@@P77\033[1;31mYPGGGGGGGGGGGGGG\033[1;33m#&@&Y:  ...................")
print (".......................................  ~P@@G5Y\033[1;31mY5GGBBBGGGGGGBB\033[1;33mGB&@&Y^...................")
print (".........................................  ~5@@#P\033[1;31mYY5GBGGGGGBBBBG\033[1;33mGB#@@&^ .................")
print ("...........................................  ^5&@#P\033[1;31m5Y5PGGGBBBBBBB\033[1;33m#&@B?...................")
print (".............................................  ^Y&@#P\033[1;31mYY5GGGGBBB&@\033[1;33m@@5. ...................")
print ("...............................................  ^Y&@&\033[1;31mGPPGGGB#@@@@\033[1;33m@@B7. .................")
print (".................................................  :J&@&B\033[1;31mGB&@@@@@@@\033[1;33m@&#Y^  ...............")
print ("...................................................  :J#@@@#J!G@@@#BGPGGY~  ........................")
print (".....................................................  :7J7:  .!5PJJPGGGGGY~........................")
print (".......................................................     ...  .~77JPGGGGP^ ......................")
print (".................................................................. :~7YPGP5^ .......................")
print (".................................................................... .!J!.:77:  ....................")
print ("......................................................................   .  :!7^  ..................")
print ("............................................................................. :!7^. ................")
print ("............................................................................... :!7^. ..............")
print ("................................................................................. .!7^ .............")
print ("................................................................................... .~~.............")
print (".................................................................................... ~P7............")
print (".......................................................................................:............")
print ("....................................................................................................")
print ("....................................................................................................")
print ()
print ("                                           \033[1;33mby: \033[1;31mqorsan taiz")
print ("                               \033[1;33mgithub: \033[1;31mhttps://github.com/qorsan73/sqlmap-vuln")
print ("                               \033[1;33mtelegram: \033[1;31mhttps://t.me/qorsantaez73")
print ()
query = "index.php?id="
for result in search(query, num_results=40):
    print(colored(result, 'green'))
