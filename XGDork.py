


import os
import sys
import requests
from random import randint
from termcolor import colored
from XGDlib import search_engine


argc = len(sys.argv)
if (argc == 2):
    if (sys.argv[1] == '-h' or sys.argv[1] == '--help'):
        print (" USE : XGDork.py -d 'your dork' -p 'pages_number' -o 'out_file' ")
        exit()
elif (argc == 7):

    p_dork = sys.argv[1]
    data_dork = sys.argv[2]
    p_page = sys.argv[3]
    data_page = sys.argv[4]
    p_file = sys.argv[5]
    data_file = sys.argv[6]

    if (p_dork == '-d' and p_page == '-p' and p_file == '-o' and data_dork != '' and data_page != '' and data_file != ''):
            
        print ("\n\n")
        print colored("  __  ______ ____             _     ", 'blue')
        print colored("  \ \/ / ___|  _ \  ___  _ __| | __ ", 'blue')
        print colored("   \  / |  _| | | |/ _ \| '__| |/ / ", 'blue')
        print colored("   /  \ |_| | |_| | (_) | |  |   <  ", 'blue')
        print colored("  /_/\_\____|____/ \___/|_|  |_|\_\ \n", 'blue')
        print colored("XGDork - ViraX Google Dork Scanner", 'grey')
        print colored("Original code by ViraX")

        print colored("Version: a0.7.5 for Python 2.7")
        print colored("Contributor(s)")
        print colored("- ")
        print ("\n")

        print colored(" [!] DISCLAIMER: This program makes it easy to find vulnerable SQL injection URLs, it is only a prototype, it is very simple, it will be improved ... I am not responsible for illegal acts that you would do with this program !, only educational . [!] \n", 'green')
        print ("it will be improved, wait ...")

        print colored("\n [!] XGDork Start ... [!] \n", 'blue')

        nfile = open(data_file, 'w')
        nfile.write("--- XGDork Result --- \n")
        nfile.close()

        search_engine (data_dork, int(data_page), data_file)
        exit(1)
    else:
        print ("! Error Params ! USE: XGDork.py -h [OR] --help !")
else:
    print ("! USE : XGDork.py -h [OR] --help !")
    exit()
