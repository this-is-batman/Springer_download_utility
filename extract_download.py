import PyPDF2
import re
import urllib.request
import os
import sys
file = open("Springer Ebooks.pdf",'rb')
pdf = PyPDF2.PdfFileReader(file)
pages = pdf.getNumPages()
key = '/Annots'  # annotations
uri = '/URI'
ank = '/A'
list_links= [] #URL's in the pdf
for page in range(pages):
    pageSliced = pdf.getPage(page)   # a PageObject instance is created
    if key in pageSliced.keys():  # if the page has annotations i.e. URL, highlights
        ann = pageSliced[key]   # find the annotations in the page, PageObject is a DictionaryObj
        for a in ann:   # for all the annotations
            u = a.getObject()
            if uri in u[ank].keys():   # if the key is of the type '\URI' i.e. annotation is an URL
               #print(u[ank][uri])   Uncomment this line if you want to print the values of the URL
               list_links.append(u[ank][uri])

print("Enter the indices of the pdf's you want to download...")
input_list = input()
cnt=0
for indx in input_list.split():
    for i in list_links:
        cnt+=1
        if cnt==int(indx):
            print("Please wait a bit...Downloading!\n")
            response = urllib.request.urlopen(str(i))
            link = response.geturl()
            print(f'The link is {link}')
            match = re.split("F",link)  # the isbn number of the book
            down_link = "https://link.springer.com/content/pdf/10.1007%2F" + match[1] +".pdf"
            os.system("wget " + down_link)
            cnt=0
            break
        else:
            pass


