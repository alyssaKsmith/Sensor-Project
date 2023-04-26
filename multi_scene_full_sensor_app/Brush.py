import math 
import Timer

class Brush():
    
    def __init__(self, startx, starty, endx, endy, brush_ID, col, alph, brush_sz):
        self.startx = startx
        self.starty = starty 
        self.endx = endx
        self.endy = endy
        self.brushID = brush_ID
        self.col = col
        self.alph = alph
        self.brush_sz = brush_sz
        self.brush_offset = 0
        self.pingTimer = Timer.Timer(10)
        
        self.density = 0
        self.xoffset = 0
        self.yoffset = 0
        self.xPos = [0] * 2000
        self.yPos = [0] * 2000
        self.index = 0
        
        if(self.brushID == 0):
            self.brush_offset = 3
            
        elif(self.brushID == 1):
            self.brush_offset = 10
            
        elif(self.brushID == 2):
            self.brush_offset = 15
            
        elif(self.brushID == 3):
            self.brush_offset = 10
        

    def brush_shape(self, brushID, x, y):

        # Brush 0
        if(self.brushID == 0):
            noStroke()
            fill(self.col, self.alph)
            ellipse(x,y,(self.brush_sz),(self.brush_sz))
           
        # Brush 1 
        if(self.brushID == 1):
            noStroke()
            fill(self.col, self.alph)
            rectMode(CENTER)
            rect(x,y,(self.brush_sz),(self.brush_sz+15))
            
        #Brush 2 - Random circle "spray"
        if(self.brushID == 2):
            noStroke()
            fill(self.col, self.alph)
            sprayDen = 50
            #calculate random offset 
            for i in range (0,sprayDen):
                circle((x+random(-self.brush_sz,self.brush_sz)),(y+random(-self.brush_sz,self.brush_sz)),(self.brush_sz*random(.05,.25)))
        
        #Brush 3 - Triangle design
        if(self.brushID == 3):
            noStroke()
            fill(self.col, self.alph)
            
            pushMatrix()
            translate(x,y)
            rotate(PI/4)
            #rectMode(CENTER)
            #rect(x,y,self.brush_sz,self.brush_sz)
            #triangle(x, y-self.brush_sz, x-self.brush_sz, y+self.brush_sz, x+self.brush_sz, y+self.brush_sz)
            popMatrix()
        
        #Brush 4 - Image array
        
        
    def calculate_stroke(self):
    #Calculate the slope, length, and density of the stroke
        #Slope

        rise = self.endy - self.starty
        run = self.endx - self.startx

        slope = rise/(run+1)
        
        #print("slope: ", slope)
        
        #Length
        stroke_len = (rise*rise) + (run*run) 
        stroke_len = sqrt(stroke_len) 
        
        #print("Length of line: ", stroke_len, "Brush Spacing: ", self.brush_offset)

        #Density
        self.density = ceil(stroke_len / self.brush_offset)
        
    #Calculate number of points 
        num_interpoints = self.density - 2
        
    #Calculate x and y offset
        self.xoffset = self.brush_offset / (sqrt(slope*slope)+1)
        self.yoffset = sqrt((self.brush_offset*self.brush_offset)-(self.xoffset*self.xoffset))
        
    def brush_stroke(self):

        self.xPos[0] = self.startx
        self.yPos[0] = self.starty
        
        #self.pingTimer.start()
        
        #if(self.pingTimer.isFinished()):
        if(True):
            
            if(self.index == 0):
                for i in range ( 1, self.density):
                    self.xPos[i] = self.xPos[i-1] + self.xoffset
                    self.yPos[i] = self.yPos[i-1] + self.yoffset  
            if(self.index < self.density):
                self.brush_shape(0,(self.xPos[self.index]),self.yPos[self.index])
            self.index = (self.index + 1) #% self.density
            
            self.pingTimer.start()
                    
        

            
        


        
        
        
