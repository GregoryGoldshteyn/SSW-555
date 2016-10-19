# -*- coding: UTF-8 -*-
import time
class Individual:
    'class for all individual'
    indilist=[]
    def __init__(self,uID):
        self.id=uID
        self.fName=""
        self.lName=""
        self.gender=""
        self.date_of_birth=[]
        self.married="false"
        self.alive="true"
        self.date_of_death=[]
        self.famc=[]
        self.fams=[]
	
    def addfamc(self,famc):
        self.famc.append(famc)
	
    def addfams(self,fams):
        self.fams.append(fams)
        self.married="true"
	
    def death(self,d,m,y):
        self.date_of_death=changetonum([d,m,y])
        self.alive="false"
		
    def divorce(self):
        self.married="false"
    
    def setfn(self,fname):
        self.fName=fname
        
    def setln(self,lname):
        self.lName=lname
        
    def setdob(self,d,m,y):
        self.date_of_birth=changetonum([d,m,y])
        
    def setgender(self,g):
        self.gender=g
        
	
class Family:
    'class for all family'
    famlist=[]
    def __init__(self,uID):
        self.id=uID
        self.husband=""
        self.wife=""
        self.date_of_marriage=[]
        self.state="married"
        self.date_of_divorce=[]
        self.children=[]
	

    def addchild(self,uID):
        i=100
        if len(uID)==5:
            i=int(uID[2])
        if len(uID)==6:
            i=int(uID[2]+uID[3])
        p=Individual.indilist[i-1]
        f=self
        self.children.append(p)
        p.addfamc(f)
		
    def divorce(self, d,m,y):
        self.state="divorce"
        self.date_of_divorce=changetonum([d,m,y])
        self.husband.divorce()
        self.wife.divorce()
        
    def setwife(self,uID):
        i=100
        if len(uID)==5:
            i=int(uID[2])
        if len(uID)==6:
            i=int(uID[2]+uID[3])
        p=Individual.indilist[i-1]
        f=self
        self.wife=p
        p.addfams(f)
    
    def sethusband(self,uID):
        i=100
        if len(uID)==5:
            i=int(uID[2])
        if len(uID)==6:
            i=int(uID[2]+uID[3])
        p=Individual.indilist[i-1]
        f=self
        self.husband=p
        p.addfams(f)
    
    def setdom(self,d,m,y):
        self.date_of_marriage=changetonum([d,m,y])
    
	
def readFile(url):
    input=open(url,'r')
    s=input.readline()
    flag1=1
    flag2=1
    i=''
    f=''
    b=''
    while s!="":     
        l=s.split(' ')
        if (l[0]=='0' and len(l)>=3 and l[2]=='INDI\n'):
            ptemp = Individual(l[1])
            Individual.indilist.append(ptemp)
        if(l[0]=='0' and len(l)>=3 and l[2]=='FAM\n'):
            ftemp = Family(l[1])
            Family.famlist.append(ftemp)
        if(l[0]=='1' and l[1]=='NAME'):
            ptemp.setfn(l[2])
            ptemp.setln(l[3])
        if(l[0]=='1' and l[1]=='SEX'):
            ptemp.setgender(l[2])
        if(l[0]=='1' and l[1]=='BIRT\n'):
            l=input.readline().split(' ')
            ptemp.setdob(l[2],l[3],l[4])
        if(l[0]=='1' and l[1]=='DEAT'):
            l=input.readline().split(' ')
            ptemp.death(l[2],l[3],l[4])
        if(l[0]=='1' and l[1]=='MARR\n'):
            l=input.readline().split(' ')
            ftemp.setdom(l[2],l[3],l[4])
        if(l[0]=='1' and l[1]=='HUSB'):
            ftemp.sethusband(l[2])
        if(l[0]=='1' and l[1]=='WIFE'):
            ftemp.setwife(l[2])
        if(l[0]=='1' and l[1]=='CHIL'):
            ftemp.addchild(l[2])
        if(l[0]=='1' and l[1]=='DIV'):
            l=input.readline().split(' ')
            ftemp.divorce(l[2],l[3],l[4])
        s=input.readline()

def getage(dob):
    t=time.strftime('%d %m %Y',time.localtime(time.time()))
    t=t.split(' ')
    if int(t[1])>dob[1]:
        return int(t[2])-dob[2]
    if int(t[1])==dob[1]:
        if int(t[0])>=dob[0]:
            return (int(t[2])-dob[2])
        else:
            return (int(t[2])-dob[2]-1)
    if int(t[1])<int(dob[1]):
        return (int(t[2])-dob[2]-1)
        
def changetonum(date):
    date[0]=int(date[0])
    if date[1]=='JAN':
        date[1]=1
    if date[1]=='FEB':
        date[1]=2
    if date[1]=='MAR':
        date[1]=3
    if date[1]=='APR':
        date[1]=4
    if date[1]=='MAY':
        date[1]=5
    if date[1]=='JUN':
        date[1]=6
    if date[1]=='JUL':
        date[1]=7
    if date[1]=='AUG':
        date[1]=8
    if date[1]=='SEP':
        date[1]=9
    if date[1]=='OCT':
        date[1]=10
    if date[1]=='NOV':
        date[1]=11
    if date[1]=='DEC':
        date[1]=12
    date[2]=int(date[2])
    return date
    
def large_diff_couple():
    #US34
    result=[]
    for i in xrange(len(Family.famlist)):
        ft=Family.famlist[i]
        a=getage(ft.husband.date_of_birth)/getage(ft.wife.date_of_birth)
        if a>=2 or a<=0.5:
            result.append(ft)
    return result

def recentbirth():
    #US35
    t=time.strftime('%d %m %Y',time.localtime(time.time()))
    t=t.split(' ')
    result=[]
    for i in xrange(len(Individual.indilist)):
        p=Individual.indilist[i]
        if getage(p.date_of_birth)==0:
            if int(t[1])==p.date_of_birth[1]:
                result.append(p)
            if int(t[1])-p.date_of_birth[1]==1:
                if t[0]<p.date_of_birth[0]:
                    result.append(p)
                if t[0]==p.date_of_birth[0]:
                    if (p.date_of_birth[1]==2 or p.date_of_birth[1]==4 or p.date_of_birth[1]==6 or p.date_of_birth[0]==9 or p.date_of_birth[0]==11 or p.date_of_birth[0]==12):
                        result.append(p)
    return result
    
def recentdeath():
    #US36
    t=time.strftime('%d %m %Y',time.localtime(time.time()))
    t=t.split(' ')
    result=[]
    for i in xrange(len(Individual.indilist)):
        p=Individual.indilist[i]
        if p.alive=='false':
            if getage(p.date_of_death)==0:
                if t[1]==p.date_of_death[1]:
                    result.append(p)
                if t[1]-p.date_of_death[1]==1:
                    if t[0]<p.date_of_death[0]:
                        result.append(p)
                    if t[0]==p.date_of_death[0]:
                        if (p.date_of_birth[1]==2 or p.date_of_birth[1]==4 or p.date_of_birth[1]==6 or p.date_of_birth[0]==9 or p.date_of_birth[0]==11 or p.date_of_birth[0]==12):
                            result.append(p)
    return result
    
def recentsur():
    #US37
    dp=recentdeath()
    result=[]
    for i in xrange(len(dp)):
        d=dp[i]
        if len(d.fams)!=0:
            for j in xrange(len(d.fams)):
                f=d.fams[j]
                if len(f.children)!=0:
                    for k in range(len(f.children)):
                        if f.children[k].alive=='true':
                            result.append(f.children[k])
                if (d.gender=='M' and f.wife.alive=='true'):
                    result.append(f.wife)
                if (d.gender=='F' and f.husband.alive=='true'):
                    result.append(f.husband)
    return result

def rentbd():
    #US38
    t=time.strftime('%d %m %Y',time.localtime(time.time()))
    t=t.split(' ')
    result=[]
    for i in xrange(len(Individual.indilist)):
        p=Individual.indilist[i]
        if p.alive=='true':
            if (int(t[1])==p.date_of_birth[1] and int(t[0])<p.date_of_birth[0]):
                result.append(p)
            if((p.date_of_birth[1]-int(t[1]))==1 and int(t[0])>=p.date_of_birth[0]):
                result.append(p)
    return result

out=open('log.txt','w')
readFile('My_Family.ged')
r34=large_diff_couple()
for i in range(len(r34)):
    f=r34[i]
    print('Family with unique id:'+f.id+' has a large age difference')
    out.write('Family with unique id:'+f.id+' has a large age difference')
r35=recentbirth()
for i in range(len(r35)):
    p=r35[i]
    print('individual with unique id:'+p.id+' is rencent birth')
    out.write('individual with unique id:'+p.id+' is rencent birth')
r36=recentdeath()
for i in range(len(r36)):
    p=r36[i]
    print('individual with unique id:'+p.id+' is rencent death')
    out.write('individual with unique id:'+p.id+' is rencent death')
r37=recentsur()
for i in range(len(r37)):
    p=r37[i]
    print('individual with unique id:'+p.id+' is rencent survivors')
    out.write('individual with unique id:'+p.id+' is rencent survivors')
r38=rentbd()
for i in range(len(r38)):
    p=r38[i]
    print('birthday of individual with unique id:'+p.id+' is upcomming')
    out.write('birthday of individual with unique id:'+p.id+' is upcomming')
