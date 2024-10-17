from graphics import*

def finalDigit(win, columns, rows, patternColour):
    
    patch = []
    
    p1= Point(0,0)
    p2= Point(100,100)
    
    line = Line(p1,p2)
    line.draw(win)
    patch.append(line)
    
    for i in range(10):
        p1.move(0,10)
        p2.move(0,-10)
        line = Line(p1,p2)
        line.draw(win)
        line.setFill(patternColour)
        patch.append(line)
        
    for i in range(10):
        p1.move(10,0)
        p2.move(-10,0)
        line = Line(p1,p2)
        line.draw(win)
        line.setFill(patternColour)
        patch.append(line)
     
    border = Rectangle(Point(0,0), Point(100,100))
    border.draw(win)
    patch.append(border)
     
    for parts in patch:
        parts.move(columns, rows)
     
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

def drawRectangle(win, tl, br, colour):
    rec = Rectangle(tl,br)
    rec.setFill(colour)
    rec.draw(win)
    
    return rec

def penultimateDigit(win, columns, rows, patternColour):
    
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
            rec = drawRectangle(win, tl, br, backgroundColour)
            patch.append(rec)
    
            tl= Point(5+j,0+i)
            br= Point(20+j,10+i)
            rec = drawRectangle(win, tl, br, backgroundColour)
            patch.append(rec)
    
            
            tl= Point(5+j,15+i)
            br= Point(20+j,25+i)
            rec = drawRectangle(win, tl, br, backgroundColour)
            patch.append(rec)
    
             
            #Pattern2
            tl= Point(25+j,0+i)
            br= Point(50+j,25+i)
            rec = drawRectangle(win, tl, br, backgroundColour)
            patch.append(rec)
    

            tl= Point(25+j, 5+i)
            br= Point(35+j, 20+i)
            rec = drawRectangle(win, tl, br, backgroundColour)
            patch.append(rec)
    
            
            tl= Point(40+j, 5+i)
            br= Point(50+j, 20+i)
            rec = drawRectangle(win, tl, br, backgroundColour)
            patch.append(rec)
    
            
    border = Rectangle(Point(0,0), Point(100,100))
    border.draw(win)
    patch.append(border)
     
    for parts in patch:
        parts.move(columns, rows)         


def drawRec(win, columns, rows, patternColour):
    rec = Rectangle(Point(0,0), Point(100,100))
    rec.setFill(patternColour)
    rec.draw(win)
    
    rec.move(columns, rows)
    
def dimensionColour(dimension):
    if dimension == 5:
        final = [1,11,13,19,20]
        penultimate = [2,3,4,5,11,12,14,15,21,22,23,24,25]
        
        colour1 = [1,3,5,11,15,21,23,25]
        colour2 = [2,4,6,10,16,20,22,24]
        colour3 = [7,8,9,12,13,14,17,18,19]
        
    elif dimension ==7:
        final = [1,9,17,25,33,49]
        penultimate = [2,3,4,5,6,7,15,16,18,19,20,21,29,30,31,32,33,35,36,43,44,45,46,47,48]
        
        colour1 = [1,3,5,7,15,21,29,35,43,45,47,49]
        colour2 = [2,4,6,8,14,22,28,26,42,44,46,48]
        colour3 = [9,10,11,12,13,16,17,18,19,20,23,24,25,26,27,30,31,32,33,34,35,38,39,40,41]

        
    else:
        final = [1,11,21,31,41,51,61,71,81]
        penultimate = [2,3,4,5,6,7,8,9,19,20,21,22,23,24,25,26,27,37,38,39,40,42,43,44,45,55,56,57,58,59,60,62,63,73,74,75,76,77,78,79,80]
        
        colour1 = [1,3,5,7,9,19,27,37,45,55,63,73,75,77,79,81]
        colour2 = [2,4,6,8,10,18,28,36,46,54,64,72,74,76,78,80]
        colour3 = [11,12,13,14,15,16,17,20,21,22,23,24,25,26,29,30,31,32,33,34,35,38,39,40,41,42,43,44,47,48,49,50,51,52,53,56,57,58,59,60,61,62,65,66,67,68,6970,71]
        
    return final, penultimate, colour1, colour2, colour3
    
    

def colourSelector(position, colours, colour1, colour2, colour3):
    if position in colour1:
        return colours[0]
    
    elif position in colour2:
        return colours[1]
    
    else:
        return colours[2]
  
  
#Antepenultimate
def antepenultimateDigit(win, dimension, colours):
    size = 100
    position = 0
    
    final, penultimate, colour1, colour2, colour3 = dimensionColour(dimension)
        
    
    
    for rows in range(0, dimension * size, size):
        for columns in range(0, dimension * size, size):
            position += 1
            
            if position in final:
                patternColour = colourSelector(position, colours, colour1, colour2, colour3)
                finalDigit(win, columns, rows, patternColour)
                
            elif position in penultimate:
                patternColour = colourSelector(position, colours, colour1, colour2, colour3)
                penultimateDigit(win, columns, rows, patternColour)
            
            else:
                patternColour = colourSelector(position, colours, colour1, colour2, colour3)
                drawRec(win, columns, rows, patternColour)
    
    

def userInput():
    dimensionOptions = [5, 7, 9]
    colourOptions = ['red', 'green', 'blue', 'magenta', 'orange', 'yellow', 'cyan']
    dimension = 1
    colours = ['']*3
    
    while (dimension not in dimensionOptions):
        dimension = int(input(f"Choose Patch Dimension, Availiable Dimensions {dimensionOptions}: "))
        if dimension not in dimensionOptions:
            print(f"{dimension} is not in the options. Try Again!")
    
  
    for i in range(3):
        while (colours[i] not in colourOptions):
            colours[i] = input(f"Choose Patch Colours, Availiable Colours {colourOptions} : ")
            if colours[i] not in colourOptions:
                print(f"{colours[i]} is not in the options. Try Again!")
    
    return dimension, colours

def main():
     dimension, colours = userInput()
     width = dimension * 100
     height = width
     
     win = GraphWin("", width, height)
     antepenultimateDigit(win, dimension, colours)
    
            
               
   
   
        
main()