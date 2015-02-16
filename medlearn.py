#Author Robert Bikwemu
#
#   Looking to test Machine Learning on Journal/Author/Keyword 
#   in scholarly publication.
#
#

import pubmed
import urllib2
from bs4 import BeautifulSoup
li=[]

_baseurl = 'http://www.ncbi.nlm.nih.gov/pubmed?term='

def search(term):
        j=term.split(' ')
        li=[]
        l=[]
        for i in range(len(j)):
                h=len(j)-1
                if i < h:
                        li.append(j[i]+'%20')
                elif i==h:
                	li.append(j[i])

        b=''
        for i in range(len(li)):
                b=b+li[i]

        url=_baseurl+b
        b=urllib2.urlopen(url)
        soup=BeautifulSoup(b.read())
        k=soup.findAll('p',{'class','title'})

        for i in range(len(k)):
                #first page of results with 20 links to articles at most
                m=(k[i].find('a').get('href'))
                l.append(m[8:])



	

