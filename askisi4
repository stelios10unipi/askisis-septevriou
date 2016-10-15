import urllib
import urllib2
awards=[]
imdbr=[]
params = {'param1': 'value1'}
stoixeia=[]

name=(raw_input("Dwse Onoma Tainias:  "))
req = urllib2.Request("http://www.omdbapi.com/?t="+name+"&y=&plot=short&r=json", urllib.urlencode(params))
res = urllib2.urlopen(req)

data = res.read()
for i in data:
    stoixeia.append(i)
for i in range(len(stoixeia)):
    if(stoixeia[i]=="A"and stoixeia[i+1]=="w" and stoixeia[i+2]=="a" and stoixeia[i+3]=="r" and stoixeia[i+4] =="d" and stoixeia[i+5]=="s"):
        while(stoixeia[i]!=","):
           awards.append(stoixeia[i])
           i+=1
for i in range(len(stoixeia)):
    if(stoixeia[i]=="i"and stoixeia[i+1]=="m" and stoixeia[i+2]=="d" and stoixeia[i+3]=="b" and stoixeia[i+4] =="R" and stoixeia[i+5]=="a" and stoixeia[i+6]=="t"and stoixeia[i+7]=="i"and stoixeia[i+8]=="n"and stoixeia[i+9]=="g"):
        while(stoixeia[i]!=","):
           imdbr.append(stoixeia[i])
           i+=1


awa=" ".join(awards)
rating=" ".join(imdbr)
print rating
print awa
