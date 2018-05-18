from bs4 import BeautifulSoup
import re
import urllib.request
from urllib.parse import quote
import argparse
import sys
import json

# adapted from http://stackoverflow.com/questions/20716842/python-download-images-from-google-image-search

def get_soup(url,header):
    #function pour reprendre le code avec le header 
    return BeautifulSoup(urllib.request.urlopen(urllib.request.Request(url,headers=header)),'html.parser')

def main(args):

    parser = argparse.ArgumentParser(description='LR-Physics Scraping Python Function')
    parser.add_argument(
            '-s', '--search', 
            default='place holder LR-Physics', 
            type=str, 
            help='Ici il faut plugger la query entre \" ca se fera en lui passant une string'
    )
    args = parser.parse_args()
    query = args.search #raw_input(args.search)
    #query defined by the argparse comment 
    
    
    max_images = 1
    # ici max-image si un jour LR-Physics veut plus il suffit de changer le 1 en 5
    
    query= quote(query , safe ='')
    #escape la query pour eviter que url ne soit pas conforme
    
    url="https://www.google.co.in/search?q="+query+"&source=lnms&tbm=isch"
    header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
    #definir query et header
    
    soup = get_soup(url,header)
    ActualImages=[]# contains the link for Large original images, type of  image
    allLinks = soup.find_all("div",{"class":"rg_meta"})
    # tirer de stack overflow et permet de laisser place si plusierus image returnee

    firstImgSrc = allLinks[0].get_text()
    firstImgSrcJSon =  (json.loads(firstImgSrc))
    LinkToReturn = firstImgSrcJSon["ou"]
    #ici je vais chercher ce que je pense sert a lazyloader l'image
    print (LinkToReturn)
    return (LinkToReturn) #retour de l'url si plusieurs img possible retour array -> futur

        

if __name__ == '__main__':
    from sys import argv
    try:
        main(argv)
    except KeyboardInterrupt:
        pass
    sys.exit()
#permet de ne pas lancer la query si juste module
