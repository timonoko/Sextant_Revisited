

def gensym1(paper=[]):

    def gensym2(y=[]):
        return int((HEI - (HEI * ((y - MIN) / (MAX - MIN)))))


    def gensym3(m=[],d=[]):
        return int((WID * (((30 * (m - 1)) + (d - 1)) / 360)))

    global RED
    global GREEN
    global BLACK
    global WHITE
    global YELLOW
    global GREY
    GREY=[80, [80, [80, []]]]
    global WID
    WID=1000
    global HEI
    HEI=700
    global MAX
    MAX=int(sun_alt(6,21,10,1))
    global MIN
    MIN=int(sun_alt(12,22,10,1))
    global KUVA
    KUVA=0
    KUVA=newimage(WID,HEI,iff(paper,WHITE,BLACK))
    imagetext(KUVA,[30, [30, []]],cons("FreeSans.ttf",cons(30,cons(iff(paper,[80, [80, [0, []]]],YELLOW),[]))),compress([34, [83, [85, [78, [32, [65, [78, [71, [76, [69, [32, [64, [32, [72, [69, [76, [83, [73, [78, [75, [73, []]]]]]]]]]]]]]]]]]]]]][1]))
    imagetext(KUVA,[30, [70, []]],cons("FreeSans.ttf",cons(30,cons(iff(paper,[80, [80, [0, []]]],YELLOW),[]))),compress([34, [69, [86, [69, [82, [89, [32, [77, [79, [78, [84, [72, [44, [32, [68, [65, [89, [32, [38, [32, [72, [79, [85, [82, []]]]]]]]]]]]]]]]]]]]]]]]][1]))
    
    ycoord=gensym2
    
    xcoord=gensym3
    for a in range(MIN,(1 + MAX)):
        imagetext(KUVA,cons(0,cons(ycoord(a),[])),cons("FreeSans.ttf",cons(10,cons(iff(paper,BLACK,WHITE),[]))),int(a))
        imagedraw(KUVA,cons(0,cons(ycoord(a),[])),cons(WID,cons(ycoord(a),[])),GREY)
        if equal(0,(int(a) % 10)):
            Nprint(a)
            imagedraw(KUVA,cons(0,cons(ycoord(a),[])),cons(WID,cons(ycoord(a),[])),iff(paper,[80, [80, [0, []]]],YELLOW))
    for m in range(1,(1 + 12)):
        imagetext(KUVA,cons(xcoord(m,1),cons((HEI - 15),[])),cons("FreeSans.ttf",cons(15,cons(iff(paper,[80, [80, [0, []]]],YELLOW),[]))),m)
        imagedraw(KUVA,cons((xcoord(m,1) - 1),cons((HEI - 11),[])),cons((xcoord(m,1) - 1),cons(0,[])),iff(paper,[80, [80, [0, []]]],YELLOW))
        for d in range(1,(1 + 28),3):
            imagetext(KUVA,cons(xcoord(m,d),cons((HEI - 11),[])),cons("FreeSans.ttf",cons(10,cons(iff(paper,BLACK,WHITE),[]))),d)
            imagedraw(KUVA,cons(xcoord(m,d),cons((HEI - 11),[])),cons(xcoord(m,d),cons(0,[])),GREY)
    for h in range(3,(1 + 21)):
        h2=(h - 2)
        Nprint(h)
        
        printc(13)
        printc(10)

        def gensym4():
            if (h < 13):
                return iff(paper,[0, [120, [0, []]]],GREEN)
            else:
                return iff(paper,[120, [0, [0, []]]],RED)

        COLOR=gensym4()
        x2=0
        y2=0
        for m in range(1,(1 + 12)):
            for d in range(1,(1 + 28),10):
                alt=sun_alt(m,d,h2,0)
                y=int(ycoord(alt))
                x=int(xcoord(m,d))
                if (equal(m,6) and equal(d,1)):
                    imagetext(KUVA,cons(x,cons(y,[])),cons("FreeSansBold.ttf",cons(15,cons(COLOR,[]))),h)
                if (y < HEI):
                    imagedraw(KUVA,cons(x2,cons(y2,[])),cons(x,cons(y,[])),COLOR)
                x2=x
                y2=y
    showimage(KUVA)
    return saveimage(KUVA,"KUVA.PNG")

eka=gensym1
defq('eka','lambda x: eka(a1(x))')


