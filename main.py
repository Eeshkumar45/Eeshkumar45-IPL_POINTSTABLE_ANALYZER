import numpy as np
import os
try:
    os.mkdir('files')
except:
    pass
class team:
    def __init__(self,name,played,won):
        self.name = name
        self.played = played
        self.won = won
    def win(self):
        self.played +=1
        self.won +=1
    def lost(self):
        self.played +=1
#returns current pointstable
def get_pt():
    l = [team('x',1,1),team('x',1,1),team('x',1,1),team('x',1,1),team('x',1,1),team('x',1,1),team('x',1,1),team('x',1,1)]
    global CSK,DC,KKR,KXIP,MI,RCB,RR,SRH
    var = [CSK,DC,KKR,KXIP,MI,RCB,RR,SRH]
    for i in range(8):
        l[i].name = var[i].name
        l[i].played = var[i].played
        l[i].won = var[i].won
    return l
#sets points table to l
def set_pt(l):
    global CSK, DC, KKR, KXIP, MI, RCB, RR, SRH
    var = [CSK, DC, KKR, KXIP, MI, RCB, RR, SRH]
    for i in range(8):
        var[i].name = l[i].name
        var[i].played = l[i].played
        var[i].won = l[i].won
def match(l,w):
    l[w].win()
    l[not w].lost()

#  sorts pointstable(l) considering number of matches won
def sort_pt(l):
    max = 0
    max_t = None
    max_in = None
    new_pt = []
    for i in range(8):
        max = 0
        for i in range(len(l)):
            if l[i].won >= max:
                max = l[i].won
                max_t = l[i]
                max_in = i
        new_pt.append(l.pop(max_in))
    return new_pt


vark = np.zeros((8,8))

#
def make_info(ls):
    global vark
    for l in ls:
        for i in range(8):
            if l[i].name == 'CSK':
                vark[i][0] += 1
            elif l[i].name == 'DC':
                vark[i][1] += 1
            elif l[i].name == 'KKR':
                vark[i][2] += 1
            elif l[i].name == 'KXIP':                          # 0   1   2       3   4   5    6    7
                vark[i][3] += 1                                #CSK, DC, KKR, KXIP, MI, RCB, RR, SRH
            elif l[i].name == 'MI':
                vark[i][4] += 1
            elif l[i].name == 'RCB':
                vark[i][5] += 1
            elif l[i].name == 'RR':
                vark[i][6] += 1
            elif l[i].name == 'SRH':
                vark[i][7] += 1

#  returns pointstable as one string
def make_pt(l):
    global  vark
    #l = sort_pt(l)
    text = []

    for i in l:
        text.append(str(i.name)+' '+str(i.played)+' '+str(i.won)+'\n')
    return ' '.join(text)


#current points tabel
MI = team('MI',12,8)
RCB = team('RCB',12,7)
DC = team('DC',12,7)
KXIP = team('KXIP',13,6)
KKR = team('KKR',13,6)
SRH = team('SRH',12,5)
RR = team('RR',13,6)
CSK = team('CSK',13,5)

l = [CSK, DC, KKR, KXIP, MI, RCB, RR, SRH]



#remaining Shedule
shedule = [

           [DC,MI],
           [RCB,SRH],
           [CSK,KXIP],
           [KKR,RR],
           [DC,RCB],
           [SRH,MI]]

tabels = []

tabels.append([get_pt()])
#  main
for game in shedule:
    om = []
    for i in tabels[-1]:
        set_pt(i)
        match(game,0)
        om.append(get_pt())
        set_pt(i)
        match(game,1)
        om.append(get_pt())
    tabels.append(om)



k = 0
sorted = []

for i in tabels[-1]:
    f = open('files\\'+str(k)+'.txt','w')
    p = sort_pt(i)
    sorted.append(p)
    f.write(make_pt(p))
    f.close()
    k+=1
make_info(sorted)
print('total possible outcomes :',len(sorted))

GREEN = "\033[92m"
ENDC = '\033[0m'
RED   = "\033[1;31m"
for o in range(8):
    print('Standing at number ',GREEN,o+1,ENDC)
    for i in range(8):
        if vark[o][i] == 0:
            col = RED
        else:
            col = GREEN
        print(col,l[i].name,ENDC,':',col,vark[o][i],ENDC,'times. ','-->',col,(vark[o][i]*100)/len(sorted),ENDC,'%')
    print('')