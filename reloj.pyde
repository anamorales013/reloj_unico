Y = 0

def setup() :
    size(300, 600)

def draw() :
    global Y
    background(175)


    ellipse(width/ 2, Y, 50, 50)
    fill(168, 0, 90)
    if Y > height :
        Y = 0
    else:
        Y = map(second(), 0, 59, 0, height)



    ellipse(width/ 2, Y, 50, 50)
    fill(138, 20, 40)
    if Y > height :
        Y = 0
    else:
        Y = map(minute(), 0, 60, 0, height)



        ellipse(width/ 2, Y, 50, 50)
    fill(193, 13, 20)
    if Y > height :
        Y = 0
    else:
        Y = map(hour(), 0, 24, 0, height)
