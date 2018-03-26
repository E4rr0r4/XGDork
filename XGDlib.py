


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



def     rand_agent ():

        rnd_n = randint(5, 4200)

        agent_file = open('agents.txt', 'r')
        user_agent = str(agent_file.readlines()[rnd_n])
        agent_file.close()
        user_agent = user_agent.replace('\n', '')
        return user_agent


def     rand_client ():

        rnd_n = randint(0, 10)

        client_file = open('clients.txt', 'r')
        client_name = str(client_file.readlines()[rnd_n])
        client_file.close()
        client_name = client_name.replace('\n', '')
        return client_name


def     rand_gsl ():

        rnd_n = randint(0, 3)

        gsl_file = open('gs_l.txt', 'r')
        gsl_client = str(gsl_file.readlines()[rnd_n])
        gsl_file.close()
        gsl_client = gsl_client.replace('&', '')
        gsl_client = gsl_client.replace('\n', '')
        return gsl_client


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



def     bypass_GST (dork, mod):
        
        
        if (mod == 1):
            dork = dork.replace('inurl:', 'inurl+:')
            dork = dork.replace('intext:', 'intext+:')
            dork = dork.replace('site:', 'site+:')
            dork = dork.replace('intitle:', 'intitle+:')

        if (mod == 2):
            dork = dork.replace('inurl:', 'inur+l:')
            dork = dork.replace('site:', 'sit+e:')
            dork = dork.replace('intext:', 'intex+t:')
            dork = dork.replace('intitle', 'intitl+e:')

        if (mod == 3):
            dork = dork.replace(' ', '   ')
            dork = dork.replace('inurl:', 'i+ n+ u+ r+ l+:')
            dork = dork.replace('intext:', 'i+ n+ t+ e+ x+ t+:')
            dork = dork.replace('intitle:', 'i+ n+ t+ i+ t+ l+ e+:')
            dork = dork.replace('site:', 's+ i+ t+ e+:')

        if (mod == 4):
            dork = dork.replace(' ', '  ')
            dork = dork.replace('inurl:', '%+%inurl+:%+%')
            dork = dork.replace('intext:', '%+%intext+:%+%')
            dork = dork.replace('site:', '%+%site+:%+%')
            dork = dork.replace('intitle:', '%+%intitle+:%+%')

        return dork




def     myParserGSE (greq):

        i = 0 
        ca = 0
        cb = 0
        urls = []

        if (greq.find("<b>About this page</b><br><br>Our systems have detected unusual traffic from your computer network.") > -1):
            print colored(" [!] Google Security Traffic page detected ! < Unusual Traffic >", 'red')
            print colored(" [*] Change your IP - wait 1/2 hours - Bypass this !", 'blue')
            exit()

        while (i < len(greq)-1):
                
            if (greq[i] == 'h'):
                ca = i
                while (i < len(greq)-1 and greq[i] != ':'):
                    i += 1
                cb = i
                tmp = block_cutter (greq, ca, cb)
                if (tmp == 'http:' or tmp == 'https:'):
                    while (i < len(greq)-1 and greq[i] != ' '):
                        i += 1
                    cb = i
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

                    if (url_found.find('<b>') > -1):
                        url_found = url_found.replace('<b>', '')
                    if (url_found.find('</b>') > -1):
                        url_found = url_found.replace('</b>', '')
                    if (url_found.find('"') > -1):
                        url_found = url_found.replace('"', '')
                    if (url_found.find('<br>') > -1):
                        url_found = url_found.replace('<br>', '')
                    if (url_found.find('</br>') > -1):
                        url_found = url_found.replace('</br>', '')
                    
                    
                    if (url_found.find('%253F') > -1):
                        url_found = url_found.replace('%253F', '')
                    if (url_found.find('%3F') > -1):
                        url_found = url_found.replace('%3F', '?')
                    if (url_found.find('%253D') > -1):
                        url_found = url_found.replace('%253D', '=')
                    if (url_found.find('%2526') > -1):
                        url_found = url_found.replace('%2526', '&')
                    if (url_found.find('%3D') > -1):
                        url_found = url_found.replace('%3D', '=')
                    if (url_found.find('%26') > -1):
                        url_found = url_found.replace('%26', '&')


                    if (url_found.find('.google.') == -1 and url_found.find('.gstatic.') == -1 and url_found.find('injection-sql') == -1 and url_found.find('sql-injection') == -1 and url_found.find('sql-injections') == -1 and url_found.find('sql-dorks') == -1 and url_found.find('dorks') == -1 and url_found.find('hack') == -1 and url_found.find('scribd') == -1 and url_found.find('pastebin') == -1 and url_found.find('stackoverflow') == -1 and url_found.find('over-blog') == -1 and url_found.find('github') == -1 and url_found.find('blogspot') == -1 and url_found.find('facebook') == -1):
                        urls.append(url_found)
                        print (" [!] URL Found: "+url_found)
                    
            i += 1

        urls = list(set(urls))
        return urls
        

def     myParserSQLE (url):
        
        lvl = 0
        user_agent = rand_agent()
        headers = {'User-Agent': user_agent}
        wb_req = type(requests)

        try:
            wb_req = requests.get(url, headers=headers)
            data = wb_req.text.encode('utf-8')
            #SFind
            if (data.find('MySQL') > -1):
                lvl += 2
            if (data.find('SQL') > -1):
                lvl += 2
            if (data.find('SQL syntax') > -1):
                lvl += 2
            if (data.find('Warning:') > -1):
                lvl += 3
            if (data.find('Invalid argument supplied for') > -1):
                lvl += 1
            if (data.find('Notice: Undefined variable: ') > -1):
                lvl += 2
            if (data.find('supplied argument is not a valid MySQL result resource in') > -1):
                lvl += 4
            if (data.find('valid MySQL result') > -1):
                lvl += 5
            if (data.find('Incorrect syntax near') > -1):
                lvl += 4
            if (data.find('You have an error in your SQL syntax') > -1):
                lvl += 4
            if (data.find('mysql_num_rows(): ') > -1):
                lvl += 5
            if (data.find('mysql_num_row():') > -1):
                lvl += 5
            if (data.find('mysql_fetch_array(): ') > -1):
                lvl += 4
            if (data.find('mysql_query(): ') > -1):
                lvl += 4
            if (data.find('Warning: mysql_result(): ') > -1):
                lvl += 4
            if (data.find('Warning: Unknown(): ') > -1):
                lvl += 3
            if (data.find('Warning: array_merge(): ') > -1):
                lvl += 3
            if (data.find('Warning: require(): ') > -1):
                lvl += 3
            if (data.find('MySQL Error: 1064') > -1):
                lvl += 4
            if (data.find('SQL Error: 1064') > -1):
                lvl += 4
            if (data.find('SQL Error : 1054 Unknown column') > -1):
                lvl += 4
            if (data.find('SQL Error: 1146') > -1):
                lvl += 4
            if (data.find('SQL Error: 2006') >- 1):
                lvl += 4
            if (data.find('SQL Error: 1406') > -1):
                lvl += 4
            if (data.find('SQL Error: 1030') > -1):
                lvl += 4
            if (data.find('SQL Error: 1034') > -1):
                lvl += 4
            if (data.find('SQL Error: 1690') > -1):
                lvl += 4
            if (data.find('SQL Error:') > -1):
                lvl += 1
            if (data.find('Unable to jump to row') > -1):
                lvl += 1
            if (data.find('Session halted.') > -1):
                lvl += 3
            if (data.find('Access denied for') > -1):
                lvl += 3
            if (data.find('ODBC SQL Server Driver') > -1):
                lvl == 1
            if (data.find('argument should be an array in') > -1):
                lvl += 4
            if (data.find(' expects parameter 1 to be resource, boolean given in ') > -1):
                lvl += 3
            if (data.find('Warning: array_key_exists()') > -1):
                lvl += 2
            if (data.find('Warning: parse_ini_file') > -1):
                lvl += 2
            if (data.find('SAFE MODE Restriction in effect.') > -1):
                lvl += 1


            if (lvl > 0 and lvl < 4):
                print colored(" [!] Vulnerable LVL: "+str(lvl)+" - Very Low", 'green')
                return lvl
            elif (lvl > 3 and lvl < 6):
                print colored(" [!] Vulnerable LVL: "+str(lvl)+" - Low", 'green')
                return lvl
            elif (lvl > 5 and lvl < 9):
                print colored(" [!] Vulnerable LVL: "+str(lvl)+" - Medium", 'green')
                return lvl
            elif (lvl > 8 and lvl < 15):
                print colored(" [!] Vulnerable LVL: "+str(lvl)+" - Hight *Critical", 'green')
                return lvl
            elif (lvl > 14):
                print colored(" [!] Vulnerable LVL: "+str(lvl)+" - Legendary *Critical+", 'green')
                return lvl
            else :
                print colored(" [-] Grrr ...", 'red')
                return lvl
        except requests.exceptions.ConnectionError:
            #wb_req.status_code = "Connection refused"
            print colored(" [-] Request Error, ignored ... ", 'red')
        except requests.quests.exceptions.TooManyRedirects:
            #wb_req.status_code = "Connection refused"
            print colored(" [-] Request Error, ignored ... ", 'red')
    


def     marvin_ppa (url, out_file):
        
        print colored("\n [Marvin Ppa] work on "+url, 'blue')
        
        qurl = url+"%%2727"
        if (url.find('search.php?search_id=') > -1):
            qurl = block_cutter(url, 0, (url.find('search.php?search_id=')+len("search.php?search_id=")-1))
            qurl += "1%%2727"
    
        if (myParserSQLE (qurl) > 0):
            dump = open(out_file, 'a')
            dump.write(url+"\n")
            dump.close()
            return 1
        else:
            return 0


def     moulinette (urls, out_file):

        i = 0
        n = 0
        stress = 0
        while (i < len(urls)):
            stress = marvin_ppa (urls[i], out_file)
            if (stress == 1):
                n += 1
            i += 1
        return n



def     search_engine (dork, n_page, out_file, bp):

        
        IP_PO = ipuser()
        print colored(" [*] Public IP overview: "+IP_PO, 'blue')

        su_filter = ""
        urls_found = []
        i = 1
        
        print colored(" [*] GSE Crawling wait ...\n", 'cyan')
        while (i <= n_page):

            g_page = str(i*10)

            user_agent = rand_agent()
            headers = {'User-Agent': user_agent}
            print colored("\n\n [+] User-Agent: "+user_agent, 'green')
            
            if (bp > 0):

                Client = rand_client()
                print colored(" [+] Client: "+Client, 'green')

                GS_L = rand_gsl()
                print colored(" [+] GS_L: "+GS_L+"\n\n", 'green')
                
                time.sleep(randint(5, 10))
                nurl = "http://www.google.ru/search?q="+dork+"&start="+g_page+"&"+Client+"&"+GS_L
            
            else:
                time.sleep(randint(2, 5))
                nurl = "http://www.google.ru/search?q="+dork+"&start="+g_page
            
        
            greq = requests.get(nurl, headers=headers)
            gdata = greq.text.encode('utf-8')

            urls_found += myParserGSE (gdata)
    
            i += 1

        print colored("\n [*] GSE Crawling finished, Marvin Ppa > \n", 'cyan')
        nbr = moulinette (urls_found, out_file)
        print colored("\n [!] URLs Saved: "+str(nbr)+" in '"+out_file+"' !", 'green')
        print colored(" [*] Verify if is not fake positive ! ... \n\n", 'red')








        
