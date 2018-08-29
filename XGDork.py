


import os
import sys
import time
import requests
from random import randint
from termcolor import colored
from XGDlib import search_engine, dump_page
from XGDumper import MOCA


argc = len(sys.argv)
iargs = 1
dump_module = 0

data_dork = ""
data_page = -1
data_file = ""
data_bypass = -1
data_cdom = ""
data_forcing = ""
data_timeout = -1

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

        print colored("\n [XGDork]", 'green')
        print (" USE : XGDork.py -d 'your_dork' -p 'page_number' -o 'out_file' \n")

        print ("  -d or --dork 'your_dork'    :add your dork, for search")
        print ("   e,g: -d .php?id= \n")

        print ("  -cd or --cdomain 'your_custom_domain'    :add custom google domain")
        print ("   e,g: -cd .com \n")

        print ("  -p or --page 'page_number'    :add pages max number")
        print ("   e,g: -p 10 \n")

        print ("  -p or --page 'range(n1,n2)' or 'n1,n2'    :add pages number with range")
        print ("   e,g: -p range(2,6) or 2,6 \n")

        print ("  -o or --outfile 'out_file'    :save result")
        print ("   e,g: -o urls_sqli.txt \n")

        print ("  -b or --bypass '1'    :active bypass mode")
        print ("   e,g: -b 1 \n")

        print ("  -f or --forcing 'param_i'    :stress url test, detect simple WAF and force error")
        print ("   e,g: -f id= \n")

        print ("  -t or --timeout  n    :add timeout for requests/SQLparser")
        print ("   e,g: -t 5 \n\n")

        print colored(" [XGDump - Mod]", 'green')
        print (" USE : XGDork.py  --xgdump 'your_url_target' 'param_inject' 'mode' 'table' 'field1,field2..etc'   :try inject and dump infos \n")
    
        print ("  --xgdump 'url' 'param_i' '1'    :try dump database_name_version")
        print ("   e,g: -xgdump 'www.testwebsite.com/data/item.php?id=1984' id= 1 \n")

        print ("  --xgdump 'url' 'param_i' '2'    :try dump_tables")
        print ("   e,g: -xgdump 'www.testwebsite.com/data/item.php?id=1984' id= 2 \n")

        print ("  --xgdump 'url' 'param_i' '3' 'table'    :try dump columns")
        print ("   e,g: -xgdump 'www.testwebsite.com/data/item.php?id=1984 id= 3 tbl_admin' \n")

        print ("  --xgdump 'url' 'param_i' '4' 'table' 'fields'    :try dump fields_data")
        print ("   e,g: -xgdump 'www.testwebsite.com/data/item.php?id=1984' id= 4 tbl_admin admin_id,admin_login,admin_password \n")

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


    if (sys.argv[iargs] == '-d' or sys.argv[iargs] == "--dork"):
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
    if (sys.argv[iargs] == '-t' or sys.argv[iargs] == '--timeout'):
        data_timeout = int(sys.argv[iargs+1])


    iargs += 1


if ((data_dork != '' and data_page > 0 and data_file != '') or dump_module == 1):

        print        ("\n\n")
        print colored("  __  ______ ____    42       _     ", 'blue')
        print colored("  \ \/ / ___|  _ \  ___  _ __| | __ ", 'blue')
        print colored("   \  / |  _| | | |/ _ \| '__| |/ / ", 'blue')
        print colored("   /  \ |_| | |_| | (_) | |  |   <  ", 'blue')
        print colored("  /_/\_\____|____/ \___/|_|  |_|\_\ \n", 'blue')
        print colored("  --- ViraX Google Dork Scanner --- \n", 'cyan')

        print        ("Original code by ViraX")
        print        ("Version: b0.9.0 for Python 2.7")
        print        ("Compatible for Android (NoRoot) - Termux \n")

        print colored("Contributor(s)/Source(s)", 'cyan')
        print        ("- SQLmap ('agents file') - https://github.com/sqlmapproject/ ")
        print        ("- ")
        print        ("\n")

        print colored(" [!] DISCLAIMER: A simple 'naive' tool to find SQLi Vulnerable websites in the wild via Google, I am not responsible for illegal acts that you would do with this program !, only educational . [!] \n", 'green')

        print        (" [*] it will be improved, wait ...")

        print colored("\n [!] XGDork Start ["+str(time.ctime())+"] ... [!] \n", 'blue')
        


        if (dump_module == 1):
            fields_list = data_fields.split(',')
            print colored("Warning: XGDump is only based on the simple attack for MySQL >= 5 (Generic)... it's a naive module ...\n", 'red')

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
                print colored(" [*] Warning: Bypass mode is active...", 'red')
                print colored(" [!] it may not work ! ", 'red')
                
            print colored(" [*] let's try with [ "+data_dork+" ] Happy hunting ! ;) ", 'cyan')
            search_engine (data_dork, data_page, data_file, data_bypass, data_cdom, data_forcing, data_timeout)
            print colored("\n [!] ["+str(time.ctime())+"] ... XGDork End [!] \n", 'blue')
            exit(1)

else:
    print ("! USE : XGDork.py -h [OR] --help !")
    exit()
