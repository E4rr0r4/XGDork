


import os
import sys
import requests
from random import randint
from termcolor import colored
from XGDlib import search_engine, bypass_GST, dump_page


argc = len(sys.argv)
iargs = 1

data_dork = ""
data_page = -1
data_file = ""
data_bypass = -1
data_cdom = ""

while (iargs < argc):

    if (argc < 2):
        print ("Params Error, please use XGDork.py --help ! \n")
        exit()

    if ((sys.argv[iargs] == '-h' or sys.argv[iargs] == '--help') and argc == 2):
        print ("\n USE : XGDork.py -d 'your_dork' -p 'page_number' -o 'out_file' \n")
        print (" -d 'your_dork'  :add your dork")
        print (" -cd 'your_custom_domain'  :add custom domain (e,g .com)")
        print (" -p 'page_number'  :add pages number")
        print (" -p 'range(n1,n2)' OR 'n1,n2'  :add pages number with range")
        print (" -o 'out_file'  :save result")
        print (" -b '[1-4]'  :active bypass mode, rand(domain) actived\n")
        exit()

    if (sys.argv[iargs] == '-d'):
        data_dork = sys.argv[iargs+1]
    if (sys.argv[iargs] == '-p'):
        data_page = sys.argv[iargs+1]
    if (sys.argv[iargs] == '-cd'):
        data_cdom = sys.argv[iargs+1]
    if (sys.argv[iargs] == '-o'):
        data_file = sys.argv[iargs+1]
    if (sys.argv[iargs] == '-b'):
        data_bypass = int(sys.argv[iargs+1])

    iargs += 1


if (data_dork != '' and data_page > 0 and data_file != ''):

        print ("\n\n")
        print colored("  __  ______ ____             _     ", 'blue')
        print colored("  \ \/ / ___|  _ \  ___  _ __| | __ ", 'blue')
        print colored("   \  / |  _| | | |/ _ \| '__| |/ / ", 'blue')
        print colored("   /  \ |_| | |_| | (_) | |  |   <  ", 'blue')
        print colored("  /_/\_\____|____/ \___/|_|  |_|\_\ \n", 'blue')
        print colored(" --- ViraX Google Dork Scanner --- ", 'cyan')
        print colored("Original code by ViraX")

        print colored("Version: a1.0.7 for Python 2.7")
        print colored("Contributor(s)")
        print colored("- ")
        print ("\n")

        print colored(" [!] DISCLAIMER: This program makes it easy to find vulnerable SQL injection URLs, it's a very simple program (naive), it will be improved ... I am not responsible for illegal acts that you would do with this program !, only educational . [!] \n", 'green')
        print ("it will be improved, wait ...")

        print colored("\n [!] XGDork Start ... [!] \n", 'blue')

        nfile = open(data_file, 'w')
        nfile.write("--- XGDork Result --- \n")
        nfile.close()
        
        if (data_bypass > 0):
            print colored(" [*] Warning: Bypass mode is active, the search will be much less precise, the search time increase, max number of pages reduced to 5, may have altered your search !", 'red')
            print colored(" [!] it may not work ! ", 'red')

            print colored(" [!] TimeLoop += \n", 'red')
            data_dork = bypass_GST (data_dork, data_bypass)

        search_engine (data_dork, data_page, data_file, data_bypass, data_cdom)
        exit(1)

else:
    print ("! USE : XGDork.py -h [OR] --help !")
    exit()
