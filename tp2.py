from bs4 import BeautifulSoup
import requests
import re 
kl = open ( "Kings_Landing.html" , 'r')
klsoup = BeautifulSoup (kl,"html.parser")

def titre(soup):
    # return soup.find("title").text
    return soup.title.text

def afficher_h2(soup):
    l = soup.find_all("h2")
    for i in l:
        print(i.text) 

def nb_par_avec_lien(soup):
    l = soup.find_all("p")
    l = [x for x in l if x.find("a")]
    return len(l)
    # n = 0
    # for i in l:
    #     if(i.find("a")):
    #         n += 1
    # return n 

# print(nb_par_avec_lien(klsoup))
# afficher_h2(klsoup)
# print(titre(klsoup))
# mw-parser-output

def liens(url):
    fichier = requests.get(url).text
    soup = BeautifulSoup (fichier,"html.parser")
    soup = soup.find("div",class_="mw-body-content mw-content-ltr")
    links = soup.find_all("a")
    links = set([x.get("href") for x in links if re.search("^/wiki",x.get("href"))])
    return links
    

def liens_distance(page,d):
    if d == 0:
        return set()
    else:
        s = liens(page)
        for i in s:
            s = s | liens_distance("https://iceandfire.fandom.com" + i,d-1)
        return s

print(len(liens_distance("https://iceandfire.fandom.com/wiki/Petyr_Baelish",3)))