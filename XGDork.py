


import os
import sys
import requests
from random import randint
from termcolor import colored
from XGDlib import search_engine, bypass_GST, dump_page
from XGDumper import MOCA


argc = len(sys.argv)
iargs = 1
dump_module = 0

data_dork = ""
data_page = -1
data_file = ""
data_bypass = -1
data_cdom = ""

data_url = ""
data_param = ""
data_mod = 0
data_table = ""
data_fields = ""
fields_list = []

while (iargs < argc):

    if (argc < 2):
        print ("Params Error, please use XGDork.py --help ! \n")
        exit()

    if ((sys.argv[iargs] == '-h' or sys.argv[iargs] == '--help') and argc == 2):
        print ("\n USE : XGDork.py -d 'your_dork' -p 'page_number' -o 'out_file' \n")

        print (" [XGDork - Program]")
        print (" -d 'your_dork'  :add your dork")
        print (" -cd 'your_custom_domain'  :add custom domain (e,g .com)")
        print (" -p 'page_number'  :add pages number")
        print (" -p 'range(n1,n2)' OR 'n1,n2'  :add pages number with range")
        print (" -o 'out_file'  :save result")
        print (" -b '[1-4]'  :active bypass mode, rand(domain) actived\n")

        print (" [XGDump - Module]")
        print (" --xgdump [OR] -xgdump 'your_url_target' 'param_inject' 'mode' 'table' 'field1,field2..etc'   :try inject and dump infos \n")
    
        print (" --xgdump 'url' 'param_i' '1'   :try dump database_name")
        print (" --xgdump 'url' 'param_i' '2'   :try dump_tables")
        print (" --xgdump 'url' 'param_i' '3' 'table'   :try dump columns")
        print (" --xgdump 'url' 'param_i' '4' 'table' 'fields'   :try dump fields_data")
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


if ((data_dork != '' and data_page > 0 and data_file != '') or dump_module == 1):

        print ("\n\n")
        print colored("  __  ______ ____    42       _     ", 'blue')
        print colored("  \ \/ / ___|  _ \  ___  _ __| | __ ", 'blue')
        print colored("   \  / |  _| | | |/ _ \| '__| |/ / ", 'blue')
        print colored("   /  \ |_| | |_| | (_) | |  |   <  ", 'blue')
        print colored("  /_/\_\____|____/ \___/|_|  |_|\_\ \n", 'blue')
        print colored(" --- ViraX Google Dork Scanner --- ", 'cyan')
        print colored("Original code by ViraX")

        print colored("Version: b0.6.0 for Python 2.7")
        print colored("Contributor(s)")
        print colored("- ")
        print ("\n")

        print colored(" [!] DISCLAIMER: This program makes it easy to find vulnerable SQL injection URLs, it's a very simple program (naive), it will be improved ... I am not responsible for illegal acts that you would do with this program !, only educational . [!] \n", 'green')
        print ("it will be improved, wait ...")

        print colored("\n [!] XGDork Start ... [!] \n", 'blue')
        


        if (dump_module == 1):
            fields_list = data_fields.split(',')
            print colored("Warning: XGdump_module is only based on the simple attack for MySQL> = 5 (Generic+SimpleBypassWAF)... it's a naive module ...\n", 'red')
            print colored(" [*] URL: "+data_url, 'cyan')
            print colored(" [*] Param: "+data_param, 'cyan')
            print colored(" [*] Mode: "+str(data_mod)+"\n", 'cyan')
            MOCA(data_url, data_param, int(data_mod), data_table, fields_list)
            exit(0)
        else:

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
