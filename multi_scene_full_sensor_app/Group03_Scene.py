import Dancer

LH = "LH"
RH = "RH"
LF = "LF"
RF = "RF"
    
class Group03_Scene():
    
    num_dancers = 0
    myDancer = [None]
    angle = 0
    num_positions = 105
    end_index = 0 
    xpos = ypos = 0
    
    def __init__(self, num_d):
        #super.__init__(self)
        self.num_dancers = num_d
        self.myDancer = [None] * self.num_dancers
        self.xRHpos = [0] * self.num_positions
        self.yRHpos = [0] * self.num_positions 
        self.xLHpos = [0] * self.num_positions
        self.yLHpos = [0] * self.num_positions 
        self.xRFpos = [0] * self.num_positions 
        self.yRFpos = [0] * self.num_positions 
        self.xLFpos = [0] * self.num_positions
        self.yLFpos = [0] * self.num_positions 
        self.red = int(random(210,250))
        self.green = int(random(160,200))
        self.blue = int(random(100, 150))
        self.color = color(self.red, self.green, self.blue)
        #self.r = 255 - millis()/500
        #self.g = 255 - millis()/500
        #self.b = 255 - millis()/500
        self.cur_index = (self.end_index + 1) % self.num_positions
        
    def start(self):
        noStroke()
        background(0)
        
    def update(self):    
        background(215)
        
        self.xLH = map(self.myDancer[0].sensors[LH].x1, -4, 4, 200, width)
        self.yLH = map(self.myDancer[0].sensors[LH].y1, -4, 4, -100, height)
            
        self.xRH = map(self.myDancer[0].sensors[RH].x1, -4, 4, -100, width)
        self.yRH = map(self.myDancer[0].sensors[RH].y1, -4, 4, -200, height)
        
        self.xLF = map(self.myDancer[0].sensors[LF].x1, -4, 4, -150, width)
        self.yLF = map(self.myDancer[0].sensors[LF].y1, -4, 4, 300, height)
            
        self.xRF = map(self.myDancer[0].sensors[RF].x1, -4, 4, 300, width)
        self.yRF = map(self.myDancer[0].sensors[RF].y1, -4, 4, -100, height)
            
    def draw(self):
        # Right hand position
        pushMatrix()
        # Update the last spot in the array with the sensor location
        self.xRHpos[self.end_index] = self.xRH
        self.yRHpos[self.end_index] = self.yRH
    
        # Draw everything
        for i in range(len(self.xRHpos)):
            # Draw an ellipse for each element in the arrays
            # Size are tied to the loop's counter(i)
            noStroke()
            fill(self.color)
            #fill(self.r, self.g, self.b)
            ellipse(self.xRHpos[self.cur_index],self.yRHpos[self.cur_index],i,i)
            self.cur_index = (self.cur_index + 1) % self.num_positions

        self.end_index = (self.end_index + 1) % self.num_positions
        popMatrix()
        
        # Left hand position
        pushMatrix()
        # Update the last spot in the array with the sensor location
        self.xLHpos[self.end_index] = self.xLH
        self.yLHpos[self.end_index] = self.yLH
        
        # Draw everything
        for i in range(len(self.xLHpos)):
            # Draw an ellipse for each element in the arrays
            # Size are tied to the loop's counter: i
            noStroke()
            fill(210, 100, 110)
            ellipse(self.xLHpos[self.cur_index],self.yLHpos[self.cur_index],i,i)
            self.cur_index = (self.cur_index + 1) % self.num_positions
   
        self.end_index = (self.end_index + 1) % self.num_positions
        popMatrix()
        
        # Left foot position
        pushMatrix()
        # Update the last spot in the array with the sensor location
        self.xLFpos[self.end_index] = self.xLF
        self.yLFpos[self.end_index] = self.yLF
        
        # Draw everything
        for i in range(len(self.xLFpos)):
            # Draw an ellipse for each element in the arrays
            # Size are tied to the loop's counter: i
            noStroke()
            fill(255, 245, 235)
            ellipse(self.xLFpos[self.cur_index],self.yLFpos[self.cur_index],i,i)
            self.cur_index = (self.cur_index + 1) % self.num_positions
   
        self.end_index = (self.end_index + 1) % self.num_positions
        popMatrix()
        
        # Right foot position
        pushMatrix()
        # Update the last spot in the array with the sensor location
        self.xRFpos[self.end_index] = self.xRF
        self.yRFpos[self.end_index] = self.yRF
        
        # Draw everything
        for i in range(len(self.xRFpos)):
            # Draw an ellipse for each element in the arrays
            # Size are tied to the loop's counter: i
            noStroke()
            fill(120, 90, 115)
            ellipse(self.xRFpos[self.cur_index],self.yRFpos[self.cur_index],i,i)
            self.cur_index = (self.cur_index + 1) % self.num_positions
   
        self.end_index = (self.end_index + 1) % self.num_positions
        popMatrix()
        
    def addDancer(self, d, index):
        self.myDancer[index] = d
