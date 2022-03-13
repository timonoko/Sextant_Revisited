

def gensym5(paper=[]):

    def gensym6(y=[]):
        return int((HEI - (HEI * ((y - MIN) / (MAX - MIN)))))


    def gensym7(m=[],d=[]):
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
    imagetext(KUVA,[30, [30, []]],["FreeSans.ttf",[30,[iff(paper,[80, [80, [0, []]]],YELLOW),[]]]],compress([34, [83, [85, [78, [32, [65, [78, [71, [76, [69, [32, [64, [32, [72, [69, [76, [83, [73, [78, [75, [73, []]]]]]]]]]]]]]]]]]]]]][1]))
    imagetext(KUVA,[30, [70, []]],["FreeSans.ttf",[30,[iff(paper,[80, [80, [0, []]]],YELLOW),[]]]],compress([34, [69, [86, [69, [82, [89, [32, [77, [79, [78, [84, [72, [44, [32, [68, [65, [89, [32, [38, [32, [72, [79, [85, [82, []]]]]]]]]]]]]]]]]]]]]]]]][1]))
    
    ycoord=gensym6
    
    xcoord=gensym7
    for a in range(MIN,(1 + MAX)):
        imagetext(KUVA,[0,[ycoord(a),[]]],["FreeSans.ttf",[10,[iff(paper,BLACK,WHITE),[]]]],int(a))
        imagedraw(KUVA,[0,[ycoord(a),[]]],[WID,[ycoord(a),[]]],GREY)
        if equal(0,(int(a) % 10)):
            Nprint(a)
            imagedraw(KUVA,[0,[ycoord(a),[]]],[WID,[ycoord(a),[]]],iff(paper,[80, [80, [0, []]]],YELLOW))
    for m in range(1,(1 + 12)):
        imagetext(KUVA,[xcoord(m,1),[(HEI - 15),[]]],["FreeSans.ttf",[15,[iff(paper,[80, [80, [0, []]]],YELLOW),[]]]],m)
        imagedraw(KUVA,[(xcoord(m,1) - 1),[(HEI - 11),[]]],[(xcoord(m,1) - 1),[0,[]]],iff(paper,[80, [80, [0, []]]],YELLOW))
        for d in range(1,(1 + 28),3):
            imagetext(KUVA,[xcoord(m,d),[(HEI - 11),[]]],["FreeSans.ttf",[10,[iff(paper,BLACK,WHITE),[]]]],d)
            imagedraw(KUVA,[xcoord(m,d),[(HEI - 11),[]]],[xcoord(m,d),[0,[]]],GREY)
    for h in range(3,(1 + 21)):
        h2=(h - 2)
        Nprint(h)
        
        printc(13)
        printc(10)

        def gensym8():
            if (h < 13):
                return iff(paper,[0, [120, [0, []]]],GREEN)
            else:
                return iff(paper,[120, [0, [0, []]]],RED)

        COLOR=gensym8()
        x2=0
        y2=0
        for m in range(1,(1 + 12)):
            for d in range(1,(1 + 28),10):
                alt=sun_alt(m,d,h2,0)
                y=int(ycoord(alt))
                x=int(xcoord(m,d))
                if (equal(m,6) and equal(d,1)):
                    imagetext(KUVA,[x,[y,[]]],["FreeSansBold.ttf",[15,[COLOR,[]]]],h)
                if (y < HEI):
                    imagedraw(KUVA,[x2,[y2,[]]],[x,[y,[]]],COLOR)
                x2=x
                y2=y
    showimage(KUVA)
    return saveimage(KUVA,"KUVA.PNG")

eka=gensym5
defq('eka','lambda x: eka(a1(x))')


