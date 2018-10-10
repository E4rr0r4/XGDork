

# This program is a 'total' free software: you can redistribute it and/or modify - ViraX
# You can quoted me as a source.

# svpEx/Ex svpDx/Dx is a simple symetric encryption system Blaise Vigenere based improve in 256 with key.  

import os, sys, base64
from random import randint
from XGDlib import block_cutter
import requests
import termios, tty, time, select

def     svpEx  (string, keyuser, modulo):

    size_s = len(string)-1
    size_k = len(keyuser)
    i = 0
    k = 0

    ndata = ""
    tmp_list = []

    while (i <= size_s and k <= size_k and string[i] != ""):

        tmp_list.append(((ord(string[i]) + ord(keyuser[k])) % int(modulo)))

        if (tmp_list[i] > modulo):
            tmp_list[i] -= modulo
        elif (tmp_list[i] < 32):
            tmp_list[i] += 32

        tmp_list[i] = chr(tmp_list[i])
        k += 1
        i +=  1

        if (k == size_k):
            k = 0

    ndata = "".join(tmp_list)
    return ndata




def     svpDx  (string, keyuser, modulo):
    
    size_s = len(string)-1
    size_k = len(keyuser)
    i = 0
    k = 0

    ndata = ""
    tmp_list = []

    while (i <= size_s and k <= size_k and string[i] != ""):

        tmp_list.append(((ord(string[i]) - ord(keyuser[k])) % int(modulo)))

        if (tmp_list[i] > modulo):
            tmp_list[i] -= modulo
        elif (tmp_list[i] < 32):
            tmp_list[i] += 32

        tmp_list[i] = chr(tmp_list[i])
        k += 1
        i +=  1

        if (k == size_k):
            k = 0
    
    ndata = "".join(tmp_list)
    return ndata




def     Ex  (string, fstring, keyuser, modulo):
    
    nfile = file
    tmp_list = []
    if (string == "" and fstring != ""):
        nfile = open(fstring, 'r')
        tmp_list = nfile.readlines()
        string = "".join(tmp_list)
        nfile.close()

    string = string[::-1]
    string = svpEx (string, keyuser, modulo)
    string = base64.b64encode(string)
    string = str(string.encode('hex'))
    string = svpEx (string, keyuser, modulo)

    string = str(string.encode('hex'))
    string = str("**-*"+str(string)+"*-**")
    string = string.replace('0', 'G').replace('1', 'A').replace('2', 'R').replace('3','K').replace('4', 'Y').replace('5', 'W').replace('6', 'S').replace('7', 'N').replace('8', 'Z').replace('9', 'V').replace('a', ':').replace('b', ';').replace('c', '?').replace('d', ',').replace('e', '!').replace('f', '.')
    string = svpEx (string, str("1984+_-_/:*ViraX("+keyuser+")2018+-_-;*vIRAx+"), modulo)
    string = str(string.encode('hex'))
    string = str("---@"+str(string)+"@---")
    string = str(base64.b64encode(string))
    string = string.replace("==", '')
    string = string[::-1]
    string = str("###"+str(string)+"@@@")

    if (fstring != ""):
        nfile = open(fstring, 'w')
        nfile.write(string)
        nfile.close

    return string



def     Dx  (string, fstring, keyuser, modulo):
    
    i = 0
    nfile = file
    tmp_list = []
    if (string == "" and fstring != ""):
        nfile = open(fstring, 'r')
        tmp_list = nfile.readlines()
        string = "".join(tmp_list)
        nfile.close()

    string = string.replace("###", '').replace("@@@", '')
    string = string[::-1]
    string = str(str(string)+"==")
    string = str(base64.b64decode(string))
    string = str(string.replace("---@", '').replace("@---", ''))
    string = str(string.decode('hex'))
    string = svpDx (string, str("1984+_-_/:*ViraX("+keyuser+")2018+-_-;*vIRAx+"), modulo)
    string = string.replace('G', '0').replace('A', '1').replace('R', '2').replace('K','3').replace('Y', '4').replace('W', '5').replace('S', '6').replace('N', '7').replace('Z', '8').replace('V', '9').replace(':', 'a').replace(';', 'b').replace('?', 'c').replace(',', 'd').replace('!','e').replace('.', 'f')
    string = str(string.replace("**-*", '').replace("*-**", ''))
    string = str(string.decode('hex'))

    string = svpDx (string, keyuser, modulo)
    string = str(string.decode('hex'))
    string = base64.b64decode(string)
    string = svpDx (string, keyuser, modulo)
    string = string[::-1]
    
    if (fstring != ""):

        tmp_list = list(string)
        while (i < len(tmp_list)-1):
            if (tmp_list[i] == "*" and tmp_list[i+1] == "h"):
                tmp_list[i] = '\n'
            i += 1
        tmp_list[i] = ''
        string = "".join(tmp_list)

        nfile = open(fstring, 'w')
        nfile.write(string)
        nfile.close()
    
    return string


def     genDork     (out):
    
    d_npage = ""
    d_ext = ""
    d_param = ""
    d_data = ""
    d_keyword = ""
    size = 0

    nfile = file
    nfile = open("gd_namespage.txt", 'r')
    size = len(nfile.readlines())-1
    nfile.close
    nfile = open("gd_namespage.txt",'r')
    d_npage = str(nfile.readlines()[randint(0,size)].replace('\n',''))
    nfile.close()

    nfile = file
    nfile = open("gd_ext.txt", 'r')
    size = len(nfile.readlines())-1
    nfile.close()
    nfile = open("gd_ext.txt", 'r')
    d_ext = str(nfile.readlines()[randint(0,size)].replace('\n', ''))
    nfile.close()

    nfile = file
    nfile = open("gd_params.txt",'r')
    size = len(nfile.readlines())-1
    nfile.close()
    nfile = open("gd_params.txt", 'r')
    d_param = str(nfile.readlines()[randint(0,size)].replace('\n', ''))
    nfile.close()

    nfile = file
    nfile = open("gd_data.txt", 'r')
    size = len(nfile.readlines())-1
    nfile.close()
    nfile = open("gd_data.txt", 'r')
    d_data = str(nfile.readlines()[randint(0,size)].replace('\n', ''))
    nfile.close()

    nfile = file
    nfile = open("gd_keywords.txt", 'r')
    size = len(nfile.readlines())-1
    nfile.close()
    nfile = open("gd_keywords.txt", 'r')
    d_keyword = str(nfile.readlines()[randint(0,size)].replace('\n', ''))
    nfile.close()

    gdork = str("inurl:"+d_npage+d_ext+d_param+" "+d_keyword)

    if (out == 1):
        print gdork

    return gdork




def     s5o (hashstring):

    ca = 0
    cb = 0
    i = 0

    nurl = "http://www.nitrxgen.net/md5db/"+str(hashstring)
    r = requests.get(nurl)
    hash_value = r.text.encode('utf-8')
    if (hash_value == ''):
        nurl = "https://www.google.com/search?q="+str(hashstring)+" plain:"
        r = requests.get(nurl)
        data = r.text.encode('utf-8')
        nurl = "https://www.google.com/search?q=list intext:Hash:"+str(hashstring)+" & intext:Plain:"
        r = requests.get(nurl)
        data += r.text.encode('utf-8')
        while (i < len(data)-1):
                if (data[i] == 'H'):
                    ca = i
                    while (i < len(data)-1 and data[i] != ':'):
                        i += 1
                    cb = i
                    tmp = block_cutter(data, ca, cb)
                    if (tmp == 'Hash:'):
                        while (i < len(data)-1 and data[i] != 'A'):
                            i += 1
                        cb = i
                        found = block_cutter(data, ca, cb)
                        hash_view = block_cutter(found, found.find('<b>')+3, found.find('</b>')-1)
                        if (hash_view == hashstring):
                            hash_value = block_cutter(found, found.find('<b>Plain</b>:')+14, found.find('. A')-1)
                            if (hash_value != ''):
                                return hash_value

                i += 1
    else:
        return hash_value

    return hash_value




i = 1
argc = len(sys.argv)
if (argc >= 2):
    data_tool = str(sys.argv[1])
    data_result = ""
    data_string = ""
    data_fs = ""
    data_key = ""
    data_modulo = 256


    if (data_tool == "--Ex" or data_tool == "-Ex" or data_tool == "-ex"):
        while (i < argc):
            if (sys.argv[i] == "-s" or sys.argv[i] == "--string"):
                data_string = sys.argv[i+1]
            if (sys.argv[i] == "--filestring" or sys.argv[i] == "-fs"):
                data_fs = sys.argv[i+1]
            if (sys.argv[i] == "-k" or sys.argv[i] == "--key"):
                data_key = sys.argv[i+1]
            i += 1
        data_result = Ex (data_string, data_fs, data_key, data_modulo)
        print (">> "+data_result)

    elif (data_tool == "--Dx" or data_tool == "-Dx" or data_tool == "-dx"):
        while (i < argc):
            if (sys.argv[i] == "-s" or sys.argv[i] == "--string"):
                data_string = sys.argv[i+1]
            if (sys.argv[i] == "-k" or sys.argv[i] == "--key"):
                data_key = sys.argv[i+1]
            if (sys.argv[i] == "--filestring" or sys.argv[i] == "-fs"):
                data_fs= sys.argv[i+1]
            i += 1
        data_result = Dx (data_string, data_fs, data_key, data_modulo)
        print (">> "+data_result)

    elif (data_tool =="--gendork" or data_tool == "-GD" or data_tool == "-gd"):
        data_result = genDork (0)
        print (">> "+data_result)

    elif (data_tool == "--xmd5" or data_tool == "-XMD5" or data_tool == "-xmd5"):
        data_result = s5o (sys.argv[2])
        print (">> "+data_result)




