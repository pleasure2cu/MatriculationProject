def ein_paar(tisch):
    ränge = []
    for  karte in tisch:
        ränge.append(karte[0])
    for rang in ränge:
        if ränge.count(rang) > 1:
            return True


def zwei_paare(tisch):
    counter = 0
    ränge = []
    for  karte in tisch:
        ränge.append(karte[0])
    for rang in ränge:
        if ränge.count(rang) > 1:
            counter += 1

    if counter > 3:
        return True


def drilling(tisch):
    ränge = []
    for  karte in tisch:
        ränge.append(karte[0])
    for rang in ränge:
        if ränge.count(rang) > 2:
            return True
    
                        

def strasse(tisch):
    ränge = {'A':0, 'K':1, 'Q':2, 'J':3, 'T':4, '9':5, '8':6, '7':7, '6':8, '5':9, '4':10, '3':11, '2':12}
    liste = [False, False, False, False, False, False, False, False, False, False, False, False, False, False]

    for x in range(7):
        liste[ränge[tisch[x][0]]] = True
    if liste[0]:
        liste[13] = True


    counter = 0
    for x in liste:
        if x:
            counter += 1
            if counter == 5:
                return True
        else:
            counter = 0



def flush(tisch):
    s = 0
    h = 0
    c = 0
    d = 0

    for karte in tisch:
        if karte[1] == 's':
            s += 1
            
        elif karte[1] == 'h':
            h += 1

        elif karte[1] == 'c':
            c += 1

        else:
            d += 1

    if s > 4:
        return True
    
    elif h > 4:
        return True
    
    elif c > 4:
        return True
    
    elif d > 4:
        return True


def full_house(tisch):
    ränge = []
    for  karte in tisch:
        ränge.append(karte[0])
    for rang in ränge:
        if ränge.count(rang) > 2:
            for x in range(ränge.count(rang)):
                ränge.remove(rang)

    if len(ränge) < 5:
        for rang in ränge:
            if ränge.count(rang) > 1:
                return True



def vierlinge(tisch):
    ränge = []
    for  karte in tisch:
        ränge.append(karte[0])
    for rang in ränge:
        if ränge.count(rang) == 4:
            return True


def straight_flush(tisch):
    s = []
    h = []
    c = []
    d = []
    tisch2 = []

    for karte in tisch:
        if karte[1] == 's':
            s.append(tisch.index(karte))
            
        elif karte[1] == 'h':
            h.append(tisch.index(karte))

        elif karte[1] == 'c':
            c.append(tisch.index(karte))

        else:
            d.append(tisch.index(karte))

    if len(s) > 4:
        for x in s:
            tisch2.append(tisch[x])

    elif len(h) > 4:
        for x in h:
            tisch2.append(tisch[x])

    elif len(c) > 4:
        for x in c:
            tisch2.append(tisch[x])

    elif len(d) > 4:
        for x in d:
            tisch2.append(tisch[x])

    if len(tisch2) > 0:
        ränge = {'A':0, 'K':1, 'Q':2, 'J':3, 'T':4, '9':5, '8':6, '7':7, '6':8, '5':9, '4':10, '3':11, '2':12}
        liste = [False, False, False, False, False, False, False, False, False, False, False, False, False, False]

        for karte in tisch2:
            liste[ränge[karte[0]]] = True
        if liste[0]:
            liste[13] = True

    
        counter = 0
        for x in liste:
            if x:
                counter += 1
                if counter == 5:
                    return True
            else:
                counter = 0


def high_card_genau(tisch):
    ränge = {'A':14, 'K':13, 'Q':12, 'J':11, 'T':10, '9':9, '8':8, '7':7, '6':6, '5':5, '4':4, '3':3, '2':2}
    tisch2 = tisch[:]
    
    for x in range(7):
        tisch2[x] = ränge[tisch2[x][0]]
    tisch2.sort(reverse = True)
    tisch2 = tisch2[:5]
    return tisch2


def ein_paar_genau(tisch):
    ränge = {'A':14, 'K':13, 'Q':12, 'J':11, 'T':10, '9':9, '8':8, '7':7, '6':6, '5':5, '4':4, '3':3, '2':2}

    karten = []
    for karte in tisch:
        karten.append(ränge[karte[0]])
    karten.sort()
    for rang in karten:
        if karten.count(rang) == 2:
            karten.remove(rang)
            karten.remove(rang)
            karten.append(10*rang)
            break
    output = karten[2:]
    output.reverse()
    return output

    
def zwei_paare_genau(tisch):
    ränge = {'A':14, 'K':13, 'Q':12, 'J':11, 'T':10, '9':9, '8':8, '7':7, '6':6, '5':5, '4':4, '3':3, '2':2}
    stpair = ''
    ndpair = ''
    tisch2 = []

    for x in range(7):
        tisch2.append(ränge[tisch[x][0]])

    tisch2.sort(reverse=True)
    
    for x in range(6):
        if tisch2[x] == tisch2[x+1]:
            if stpair == '':
                stpair = tisch2[x]
            elif ndpair == '':
                ndpair = tisch2[x]
                break
                
    tisch2.remove(stpair)
    tisch2.remove(stpair)
    tisch2.append(stpair * 10)
    tisch2.remove(ndpair)
    tisch2.remove(ndpair)
    tisch2.append(ndpair * 10)
    tisch2.sort(reverse=True)

    output = tisch2[:3]

    return output


def drilling_genau(tisch):
    ränge = {'A':14, 'K':13, 'Q':12, 'J':11, 'T':10, '9':9, '8':8, '7':7, '6':6, '5':5, '4':4, '3':3, '2':2}
    tisch2 = []

    for karte in tisch:
        tisch2.append(ränge[karte[0]])

    tisch2.sort(reverse=True)

    for rang in tisch2:
        if tisch2.count(rang) == 3:
            tisch2.remove(rang)
            tisch2.remove(rang)
            tisch2.remove(rang)
            tisch2.append(rang * 10)
            break

    tisch2.sort(reverse = True)

    output = tisch2[:3]

    return output


def strasse_genau(tisch):
    ränge = {'A':0, 'K':1, 'Q':2, 'J':3, 'T':4, '9':5, '8':6, '7':7, '6':8, '5':9, '4':10, '3':11, '2':12}
    liste = [False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    stärke = 0

    for x in range(7):
        liste[ränge[tisch[x][0]]] = int(1)
    if liste[0]:
        liste[13] = True


    
    counter = 0
    for x in range(14):
        if liste[x]:
            counter += 1
            if counter == 5:
                stärke = -1 * x                
        else:
            counter = 0

    return stärke



def flush_genau(tisch):
    ränge = {'A':14, 'K':13, 'Q':12, 'J':11, 'T':10, '9':9, '8':8, '7':7, '6':6, '5':5, '4':4, '3':3, '2':2}
    s = []
    h = []
    c = []
    d = []
    output = []

    
    for karte in tisch:
        if karte[1] == 's':
            s.append(ränge[karte[0]])
            
        elif karte[1] == 'h':
            h.append(ränge[karte[0]])

        elif karte[1] == 'c':
            c.append(ränge[karte[0]])

        else:
            d.append(ränge[karte[0]])

    if len(s) > 4:
        s.sort(reverse = True)
        output = s[:5]

    elif len(h) > 4:
        h.sort(reverse = True)
        output = h[:5]

    elif len(c) > 4:
        c.sort(reverse = True)
        output = c[:5]

    elif len(d) > 4:
        d.sort(reverse = True)
        output = d[:5]

    return output


def full_house_genau(tisch):
    ränge = {'A':14, 'K':13, 'Q':12, 'J':11, 'T':10, '9':9, '8':8, '7':7, '6':6, '5':5, '4':4, '3':3, '2':2}
    drilling1 = ''
    drilling2 = ''
    paar1 = ''
    paar2 = ''
    tisch2 = []
    
    for x in range(7):
        tisch2.append(tisch[x][0])

    for x in range(5):
        for y in range(x+1, 6):
            if tisch2[x] == tisch2[y]:
                for z in range(y+1, 7):
                    if tisch2[x] == tisch2[z]:
                        if drilling1 == '':
                            drilling1 = tisch2[x]
                        else:
                            drilling2 = tisch2[x]

    tisch2.remove(drilling1)
    tisch2.remove(drilling1)
    tisch2.remove(drilling1)

    if drilling2 != '':
        tisch2.clear()
        if ränge[drilling1] > ränge[drilling2]:
            tisch2.append(ränge[drilling1]*100)
            tisch2.append(ränge[drilling2]*10)
        else:
            tisch2.append(ränge[drilling1]*10)
            tisch2.append(ränge[drilling2]*100)

    else:
        for x in range(3):
            for y in range(x+1, 4):
                if tisch2[x] == tisch2[y]:
                    if paar1 == '':
                        paar1 = tisch2[x]
                    else:
                        paar2 = tisch2[x]

    if paar2 != '':
        tisch2.clear()
        if paar1 > paar2:
            tisch2.append(ränge[drilling1]*100)
            tisch2.append(ränge[paar1]*10)
        else:
            tisch2.append(ränge[drilling1]*100)
            tisch2.append(ränge[paar2]*10)

    elif paar1 !='':
        tisch2.clear()
        tisch2.append(ränge[drilling1]*100)
        tisch2.append(ränge[paar1]*10)

    return tisch2


def vierlinge_genau(tisch):
    ränge = {'A':14, 'K':13, 'Q':12, 'J':11, 'T':10, '9':9,
             '8':8, '7':7, '6':6, '5':5, '4':4, '3':3, '2':2}
    karten = []
    output = []

    for karte in tisch:
        karten.append(ränge[karte[0]])

    karten.sort(reverse = True)

    for karte in karten:
        if karten.count(karte) == 4:
            karten.remove(karte)
            karten.remove(karte)
            karten.remove(karte)
            karten.remove(karte)
            output.append(karte*10)
            output.append(karten[0])
            break

    return output
            
    


def straight_flush_genau(tisch):
    ränge = {'A':0, 'K':1, 'Q':2, 'J':3, 'T':4, '9':5, '8':6, '7':7, '6':8, '5':9, '4':10, '3':11, '2':12}
    liste = [False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    stärke = 0
    s = []
    h = []
    c = []
    d = []
    tisch2 = []
    

    for karte in tisch:
        if karte[1] == 's':
            s.append(ränge[karte[0]])
            
        elif karte[1] == 'h':
            h.append(ränge[karte[0]])

        elif karte[1] == 'c':
            c.append(ränge[karte[0]])

        else:
            d.append(ränge[karte[0]])

    if len(s) > 4:
        for x in s:
            liste[x] = True

    elif len(h) > 4:
        for x in h:
            liste[x] = True

    elif len(c) > 4:
        for x in c:
            liste[x] = True

    elif len(d) > 4:
        for x in d:
            liste[x] = True

    

    if liste[0]:
        liste[13] = True


    
    counter = 0
    for x in range(14):
        if liste[x]:
            counter += 1
            if counter == 5:
                stärke = -1 * x
                break
        else:
            counter = 0

    return stärke




def beurteilen(eigene_hand, kombinationen, out_q):
    kombinationen.sort()
    meine_kombination = []
    meine_kombination += eigene_hand[:2]
    counter = 0
    mein_counter = 0

    letzter_river = ''
    letzter_rang = 0
    
    for gegner_kombination in kombinationen:
        counter += 1
        



        if letzter_river == gegner_kombination[4]:

            if letzter_rang == 8:
                if not zwei_paare(gegner_kombination):
                    if not drilling(gegner_kombination):
                        if not strasse(gegner_kombination):
                            if not flush(gegner_kombination):
                                if not ein_paar(gegner_kombination):
                                    mein_counter += 1
                                else:
                                    if ein_paar_genau(gegner_kombination) < ein_paar_genau(meine_kombination):
                                        mein_counter += 1

            elif letzter_rang == 9:
                if not ein_paar(gegner_kombination):
                    if not strasse(gegner_kombination):
                        if not flush(gegner_kombination):
                            if high_card_genau(gegner_kombination) < high_card_genau(meine_kombination):
                               mein_counter += 1

            elif letzter_rang == 7:
                if not drilling(gegner_kombination):
                    if not strasse(gegner_kombination):
                        if not flush(gegner_kombination):
                            if not zwei_paare(gegner_kombination):
                                mein_counter += 1
                            else:
                                if zwei_paare_genau(gegner_kombination) < zwei_paare_genau(meine_kombination):
                                    mein_counter += 1

            elif letzter_rang == 6:
                if not strasse(gegner_kombination):
                    if not flush(gegner_kombination):
                        if not full_house(gegner_kombination):
                            if not vierlinge(gegner_kombination):
                                if not drilling(gegner_kombination):
                                    mein_counter += 1
                                else:
                                    if drilling_genau(gegner_kombination) < drilling_genau(meine_kombination):
                                        mein_counter += 1

            elif letzter_rang == 5:
                if not flush(gegner_kombination):
                    if not full_house(gegner_kombination):
                        if not vierlinge(gegner_kombination):
                            if not strasse(gegner_kombination):
                                mein_counter += 1
                            else:
                                if strasse_genau(gegner_kombination) < strasse_genau(meine_kombination):
                                    mein_counter += 1

            elif letzter_rang == 4:
                if not full_house(gegner_kombination):
                    if not vierlinge(gegner_kombination):
                        if not flush(gegner_kombination):
                            mein_counter += 1
                        else:
                            if not straight_flush(gegner_kombination):
                                if flush_genau(gegner_kombination) < flush_genau(meine_kombination):
                                    mein_counter += 1

            elif letzter_rang == 3:
                if not vierlinge(gegner_kombination):
                    if not straight_flush(gegner_kombination):
                        if not full_house(gegner_kombination):
                            mein_counter += 1
                        else:
                            if full_house_genau(gegner_kombination) < full_house_genau(meine_kombination):
                                mein_counter += 1


            elif letzter_rang == 2:
                if not straight_flush(gegner_kombination):
                    if not vierlinge(gegner_kombination):
                        mein_counter += 1
                    else:
                        if vierlinge_genau(gegner_kombination) < vierlinge_genau(meine_kombination):
                            mein_counter += 1

            else:
                if straight_flush(gegner_kombination):
                    if straight_flush_genau(meine_kombination) > straight_flush_genau(gegner_kombination):
                        mein_counter += 1
                else:
                    mein_counter += 1


            
            

            


            


            


            


            


            


            







        else:
            letzter_river = gegner_kombination[4]
            meine_kombination[2:7] = gegner_kombination[:5]
        
            if straight_flush(meine_kombination):
                letzter_rang = 1
                if straight_flush(gegner_kombination):
                    if straight_flush_genau(meine_kombination) > straight_flush_genau(gegner_kombination):
                        mein_counter += 1
                else:
                    mein_counter += 1

            elif vierlinge(meine_kombination):
                letzter_rang = 2
                if not straight_flush(gegner_kombination):
                    if not vierlinge(gegner_kombination):
                        mein_counter += 1
                    else:
                        if vierlinge_genau(gegner_kombination) < vierlinge_genau(meine_kombination):
                            mein_counter += 1

            elif full_house(meine_kombination):
                letzter_rang = 3
                if not vierlinge(gegner_kombination):
                    if not straight_flush(gegner_kombination):
                        if not full_house(gegner_kombination):
                            mein_counter += 1
                        else:
                            if full_house_genau(gegner_kombination) < full_house_genau(meine_kombination):
                                mein_counter += 1

            elif flush(meine_kombination):
                letzter_rang = 4
                if not full_house(gegner_kombination):
                    if not vierlinge(gegner_kombination):
                        if not straight_flush(gegner_kombination):
                            if not flush(gegner_kombination):
                                mein_counter += 1
                            else:
                                if flush_genau(gegner_kombination) < flush_genau(meine_kombination):
                                    mein_counter += 1

            elif strasse(meine_kombination):
                letzter_rang = 5
                if not flush(gegner_kombination):
                    if not full_house(gegner_kombination):
                        if not vierlinge(gegner_kombination):
                            if not strasse(gegner_kombination):
                                mein_counter += 1
                            else:
                                if strasse_genau(gegner_kombination) < strasse_genau(meine_kombination):
                                    mein_counter += 1

            elif drilling(meine_kombination):
                letzter_rang = 6
                if not strasse(gegner_kombination):
                    if not flush(gegner_kombination):
                        if not full_house(gegner_kombination):
                            if not vierlinge(gegner_kombination):
                                if not drilling(gegner_kombination):
                                    mein_counter += 1
                                else:
                                    if drilling_genau(gegner_kombination) < drilling_genau(meine_kombination):
                                        mein_counter += 1
                                        
            elif zwei_paare(meine_kombination):
                letzter_rang = 7
                if not drilling(gegner_kombination):
                    if not strasse(gegner_kombination):
                        if not flush(gegner_kombination):
                            if not zwei_paare(gegner_kombination):
                                mein_counter += 1
                            else:
                                if zwei_paare_genau(gegner_kombination) < zwei_paare_genau(meine_kombination):
                                    mein_counter += 1

            elif ein_paar(meine_kombination):
                letzter_rang = 8
                if not zwei_paare(gegner_kombination):
                    if not drilling(gegner_kombination):
                        if not strasse(gegner_kombination):
                            if not flush(gegner_kombination):
                                if not ein_paar(gegner_kombination):
                                    mein_counter += 1
                                else:
                                    if ein_paar_genau(gegner_kombination) < ein_paar_genau(meine_kombination):
                                        mein_counter += 1

            else:
                letzter_rang = 9
                if not ein_paar(gegner_kombination):
                    if not strasse(gegner_kombination):
                        if not flush(gegner_kombination):
                            if high_card_genau(gegner_kombination) < high_card_genau(meine_kombination):
                                mein_counter += 1

    
    out_q.put(mein_counter/counter*100)
    
        




import kombinieren
import multiprocessing
    
            


def b():
    eigene_hand = input('Meine Karten: ').split(sep=', ')
    tisch = input('Tisch: ').split(sep=', ')
    VPIP = int(input('VPIP: '))
    kombinationen = kombinieren.kombinieren(tisch, eigene_hand, VPIP)
    vari = 8 
    chunksize = int(len(kombinationen)/vari)
    procs = []
    out_q = multiprocessing.Queue()
    for x in range(vari):
        p = multiprocessing.Process(
            target = beurteilen,
            args = (eigene_hand, kombinationen[chunksize * x: chunksize * (x + 1)], out_q))
        procs.append(p)
        p.start()

    resultat = 0
    for x in range(vari):
        resultat += out_q.get()
        

    for p in procs:
        p.join()

    resultat = (resultat/vari)
    print(str(round(resultat, 2))+'%')
    if resultat != 0:
            print('1:'+str(round((100/resultat-1), 2))+'\n')


    # Turn
    if len(tisch) == 3:
        turn = ''
        while True:
            antwort = input('Pot oder Turn: ')
            if antwort == '':
                return
            try:
                antwort = int(antwort)
                if resultat != 0 and resultat != 100:
                    print('Max. Einsatz: '+str(round(antwort/(100/resultat-1)))+'\n')
                elif resultat == 100:
                    print('Gehen Sie all-in')
                else:
                    print('Max. Einsatz: 0')
            except ValueError:
                turn = antwort
                break
      
        tisch.append(turn)
        kombinationen = kombinieren.kombinieren(tisch, eigene_hand, VPIP)
        vari = 8 
        chunksize = int(len(kombinationen)/vari)
        procs = []
        out_q = multiprocessing.Queue()
        for x in range(vari):
            p = multiprocessing.Process(
                target = beurteilen,
                args = (eigene_hand, kombinationen[chunksize * x: chunksize * (x + 1)], out_q))
            procs.append(p)
            p.start()

        resultat = 0
        for x in range(vari):
            resultat += out_q.get()
        

        for p in procs:
            p.join()

        resultat = (resultat/vari)
        print(str(round(resultat, 2))+'%')
        if resultat != 0:
            print('1:'+str(round((100/resultat-1), 2))+'\n')


    # River
    if len(tisch) == 4:
        river = ''
        while True:
            antwort = input('Pot oder River: ')
            if antwort == '':
                return
            try:
                antwort = int(antwort)
                if resultat != 0 and resultat != 100:
                    print('Max. Einsatz: '+str(round(antwort/(100/resultat-1)))+'\n')
                elif resultat == 100:
                    print('Gehen Sie all-in')
                else:
                    print('Max. Einsatz: 0')
            except ValueError:
                river = antwort
                break
            
        if river == '':
            return
        tisch.append(river)
        kombinationen = kombinieren.kombinieren(tisch, eigene_hand, VPIP)
        vari = 8 
        chunksize = int(len(kombinationen)/vari)
        procs = []
        out_q = multiprocessing.Queue()
        for x in range(vari):
            p = multiprocessing.Process(
                target = beurteilen,
                args = (eigene_hand, kombinationen[chunksize * x: chunksize * (x + 1)], out_q))
            procs.append(p)
            p.start()

        resultat = 0
        for x in range(vari):
            resultat += out_q.get()
        

        for p in procs:
            p.join()

        resultat = (resultat/vari)
        print(str(round(resultat, 2))+'%')
        if resultat != 0:
            print('1:'+str(round((100/resultat-1), 2))+'\n')

    while True:
        antwort = input("Pot: ")
        if antwort == '':
            break
        else:
            if resultat != 0 and resultat != 100:
                print('Max. Einsatz: '+str(round(int(antwort)/(100/resultat-1)))+'\n')
            elif resultat == 100:
                print('Gehen Sie all-in')
            else:
                print('Max. Einsatz: 0')
                        
    return
    




