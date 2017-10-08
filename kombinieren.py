def kombinieren(tisch, handkarten, vpip):
    import hände

    output = []
    
    deck = ['As','2s','3s','4s','5s','6s','7s','8s','9s','Ts','Js','Qs','Ks',
            'Ah','2h','3h','4h','5h','6h','7h','8h','9h','Th','Jh','Qh','Kh',
            'Ad','2d','3d','4d','5d','6d','7d','8d','9d','Td','Jd','Qd','Kd',
            'Ac','2c','3c','4c','5c','6c','7c','8c','9c','Tc','Jc','Qc','Kc']


    deck.remove(tisch[0])
    deck.remove(tisch[1])
    deck.remove(tisch[2])
    if len(tisch) > 3:
        deck.remove(tisch[3])
        if len(tisch) == 5:
            deck.remove(tisch[4])

    deck.remove(handkarten[0])
    deck.remove(handkarten[1])

    
    for hand in hände.rangen[int(vpip)]:
        if hand[:2] in deck:
            if hand[2:] in deck:
                deck.remove(hand[2:])
                deck.remove(hand[:2])
                
        
                if len(tisch) == 3:
                    for x in range(len(deck)-1):
                        for y in range(x+1, len(deck)):
                            teil_output = []
                            teil_output+= tisch
                            teil_output.append(deck[x])
                            teil_output.append(deck[y])
                            teil_output.append(hand[:2])
                            teil_output.append(hand[2:])
                            output.append(teil_output)


                elif len(tisch) == 4:
                    for river in deck:
                        teil_output = []
                        teil_output += tisch
                        teil_output.append(river)
                        teil_output.append(hand[:2])
                        teil_output.append(hand[2:])
                        output.append(teil_output)


                else:
                    teil_output = []
                    teil_output += tisch
                    teil_output.append(hand[:2])
                    teil_output.append(hand[2:])
                    output.append(teil_output)


                deck.append(hand[:2])
                deck.append(hand[2:])


    return output   ### ausgegeben als liste [tischkarten, gegnerische Hand]
