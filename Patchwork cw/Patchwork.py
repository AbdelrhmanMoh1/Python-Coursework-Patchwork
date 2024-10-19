from graphics import *

#final digit
def finalDigit(win,p1,p2,colour):
    rec = Rectangle(p1,p2)
    rec.setFill(colour)
    rec.setOutline(colour)
    rec.draw(win)
    return rec
    
def finalMain(win,xMove,yMove,patternColour):
    patch = []
    x=0
    y=0
    colour=["white", patternColour]
    for i in range(0, 100, 10):
        tl = Point(0,0 + i)
        br = Point(100 - i,100)
        rectangle = finalDigit(win, tl, br,colour[i // 10 % 2])
        patch.append(rectangle)
    
    
    border = Rectangle(Point(0, 0), Point(100, 100))
    border.draw(win)
    patch.append(border)
    
    for movement in patch:
        movement.move(xMove,yMove)
    
    

def colourSelectorPenultimate(color, j, patternColour):
            
    if j == 0:
        if color % 2 == 0:
            backgroundColour = "white"
            recColour = patternColour
                
        else:
            backgroundColour = patternColour
            recColour = "white"
                    
    else:
        if color % 2 == 0:
            backgroundColour = patternColour
            recColour = "white"
                
        else:
            backgroundColour = "white"
            recColour = patternColour
            
    return  backgroundColour, recColour          

def drawRec(win, tl, br, colour):
    rec = Rectangle(tl,br)
    rec.setFill(colour)
    rec.draw(win)
    
    return rec

#penultimate digit
def penultimateDigit(win, xMove, yMove, patternColour):
    
    patch = []
    size= 25
    color = 0
    
    for j in range(0,size*4,50):
        for i in range(0,size*4,25):
            color += 1
            
            backgroundColour, recColour = colourSelectorPenultimate(color, j, patternColour)
            
            #Pattern1
            tl= Point(0+j,0+i)
            br= Point(25+j,25+i)
            rec = drawRec(win, tl, br, backgroundColour)
            patch.append(rec)
    
            tl= Point(5+j,0+i)
            br= Point(20+j,10+i)
            rec = drawRec(win, tl, br, recColour)
            patch.append(rec)
    
            
            tl= Point(5+j,15+i)
            br= Point(20+j,25+i)
            rec = drawRec(win, tl, br, recColour)
            patch.append(rec)
    
             
            #Pattern2
            tl= Point(25+j,0+i)
            br= Point(50+j,25+i)
            rec = drawRec(win, tl, br, backgroundColour)
            patch.append(rec)
    

            tl= Point(25+j, 5+i)
            br= Point(35+j, 20+i)
            rec = drawRec(win, tl, br, recColour)
            patch.append(rec)
    
            
            tl= Point(40+j, 5+i)
            br= Point(50+j, 20+i)
            rec = drawRec(win, tl, br, recColour)
            patch.append(rec)
    
            
    border = Rectangle(Point(0,0), Point(100,100))
    border.draw(win)
    patch.append(border)
     
    for movement in patch:
        movement.move(xMove, yMove)         

        
def drawRectangle(win, xMove, yMove, patternColour):
    rectangle = Rectangle(Point(0,0), Point(100,100))
    rectangle.setFill(patternColour)
    rectangle.draw(win)
    
    rectangle.move(xMove,yMove)

def arrays(dimension):
    if dimension == 5:                
        finaldigit=[4,9,12,14,17,19,20,22,24]
        pendigit=[0,1,2,3,5,10,15]
    
        colour1=[0,1,2,3,5,6,7,10,11,15]
        colour2=[4,8,12,16,20]
        colour3=[9,13,14,17,18,19,21,22,23,24]
    elif dimension == 7:
        finaldigit=[6,13,18,20,25,27,30,32,34,37,39,41,42,44,46,48]
        pendigit=[0,1,2,3,4,5,7,14,21,28,35]
        
        colour1=[0,1,2,3,4,5,7,8,9,10,11,14,15,16,17,21,22,23,28,29,35]
        colour2=[6,12,18,24,30,36,42]
        colour3=[13,19,20,25,26,27,31,32,33,34,37,38,39,30,41,43,44,45,46,47,48]
        
    elif dimension == 9:
        finaldigit=[8,17,24,26,33,35,40,42,44,49,51,53,56,58,60,62,65,67,69,71,72,74,76,78,80]
        pendigit=[0,1,2,3,4,5,6,7,9,18,27,36,45,54,63]
        
        colour1=[0,1,2,3,4,5,6,7,9,10,11,12,13,14,15,18,19,20,21,22,23,27,28,29,30,31,36,37,38,39,45,46,47,54,55,63]
        colour2=[8,16,24,32,40,48,56,64,72]
        colour3=[25,26,33,34,35,41,42,43,44,49,50,51,52,53,57,58,59,60,61,62,65,67,68,69,70,71,73,74,75,76,77,78,79,80]
    
    return finaldigit, pendigit, colour1, colour2, colour3


def colourSelector(position, colours, colour1, colour2, colour3):
    if position in colour1:
        return colours[0]
    
    elif position in colour2:
        return colours[1]
    
    else:
        return colours[2]


#antepenultimate digit
def antepenultimateDigit(win, dimension, colours):
    size = 100
    position = -1
    
    final, penultimate, colour1, colour2, colour3 = arrays(dimension)
        
    
    
    for rows in range(0, dimension * size, size):
        for columns in range(0, dimension * size, size):
            position += 1
            
            if position in final:
                patternColour = colourSelector(position, colours, colour1, colour2, colour3)
                finalMain(win, columns, rows, patternColour)
                
            elif position in penultimate:
                patternColour = colourSelector(position, colours, colour1, colour2, colour3)
                penultimateDigit(win, columns, rows, patternColour)
            
            else:
                patternColour = colourSelector(position, colours, colour1, colour2, colour3)
                drawRectangle(win, columns, rows, patternColour)
    
    

def userInput():
    dimensionOptions = [5, 7, 9]
    colourOptions = ["red", "green", "blue", "magenta", "orange", "yellow", "cyan"]
    dimension = 1
    colour = ['']*3
    
    while (dimension not in dimensionOptions):
        dimension = int(input(f"Choose a dimension (5, 7, 9): "))
        if dimension not in dimensionOptions:
            print(f"{dimension} is not in the options. Try Again!")
    
  
    for i in range(3):
        while (colour[i] not in colourOptions):
            colour[i] = input(f"Choose a colour (red, green, blue, magenta, orange, yellow, cyan) : ").lower() 
            if colour[i] not in colourOptions:
                print(f"There is no {colour[i]} colour in the options. Try Again!")
    
    return dimension, colour

def main():
     dimension, colour = userInput()
     width = dimension * 100
     height = width
     
     win = GraphWin("", width, height)
     antepenultimateDigit(win, dimension, colour)        
main()    
  
