import Dancer
import Brush
import Timer
import math

LH = "LH"
RH = "RH"
LF = "LF"
RF = "RF"


class Group02_Scene():
 
    l_angle = 0
    l_xpos = 0
    l_ypos = 0
    l_line_weight = 1
    num_dancers = 0
    r = 0
    g = 0
    b = 0
    
    pingTimer = None
    
    myDancer = [None]
    
    colarray = [color(217,244,248), #index 0-26, 0-2 are near white
                color(218,240,229), 
                color(200,231,245), #light blue
                color(187,237,241), #light blue
                color(246,210,224), #light pink
                color(248,183,205), #pink
                color(190,227,182), #light green
                color(208,232,193), #light green
                color(255,181,216), #pink
                color(255,122,188), #hot pink
                color(143,212,203), #teal
                color(138,226,233), #good cool teal
                color(35,229,231), #hot teal cyan
                color(81,196,228), #ever so slighlty more cyan than twitter blue
                color(101,173,235), #twitter blue
                color(6,113,183), #blue
                color(117,153,243), #another medium purple-blue
                color(121,152,204), #another dark periwinkle
                color(124,129,253), #dark periwinkle
                color(47,132,124), #dark green
                color(85,50,196), #second darkest purple from top
                color(56,109,127), #dark bluegreen
                color(131,104,255), #purple
                color(118,95,176), #purple
                color(136,54,137), #burgundy
                color(68,39,172), #dark purple
                color(64,86,130) #darkest purple
                ]
    
    def __init__(self, num_d):
        #super.__init__(self)
        self.num_dancers = num_d
        self.myDancer = [None] * self.num_dancers
        
        self.pingTimerst1 = Timer.Timer(700)
        self.pingTimerst1.start()
        
        self.pingTimerst2 = Timer.Timer(900)
        self.pingTimerst2.start()
        
        self.pingTimerst3 = Timer.Timer(2000)
        self.pingTimerst3.start()
        
        self.pingTimerst4 = Timer.Timer(600)
        self.pingTimerst4.start()
        
        self.pingTimerst5 = Timer.Timer(600)
        self.pingTimerst5.start()
        
        self.myStroke = None
        self.myStroke2 = None
        self.myStroke3 = None
        self.myStroke4 = None
        self.myStroke5 = None
        
    def start(self):
        noStroke()
        background(224,248,248)
        
    def update(self):
        #left hand position update
        self.lh_xpos = map(self.myDancer[0].sensors[LH].x1, -4, 4, 0, width)
        self.lh_ypos = map(self.myDancer[0].sensors[LH].y1, -4, 4, 0, height)
        self.lh_angle = map(self.myDancer[0].sensors[LH].roll, -90,90, 0, TWO_PI)
        self.lh_pi = map(self.myDancer[0].sensors[LH].pitch, -180, 180, 15, 200)
        
        #right hand position update
        self.rh_xpos = map(self.myDancer[0].sensors[RH].x1, -4, 4, 0, width)
        self.rh_ypos = map(self.myDancer[0].sensors[RH].y1, -4, 4, 0, height)
        self.rh_angle = map(self.myDancer[0].sensors[RH].roll, -90,90, 0, TWO_PI)
        self.rh_pi = map(self.myDancer[0].sensors[RH].pitch, -180, 180, 15, 200)
        
        #left foot position update
        self.lf_xpos = map(self.myDancer[0].sensors[LF].x1, -4, 4, -100, width/2)
        self.lf_ypos = map(self.myDancer[0].sensors[LF].y1, -4, 4, 0, height)
        self.lf_angle = map(self.myDancer[0].sensors[LF].roll, -90,90, 0, TWO_PI)
        self.lf_pi = map(self.myDancer[0].sensors[LF].pitch, -180, 180, 15, 200)
        
        #right foot position update
        self.rf_xpos = map(self.myDancer[0].sensors[RF].x1, -4, 4, width/2, width+200)
        self.rf_ypos = map(self.myDancer[0].sensors[RF].y1, -4, 4, 0, height)
        self.rf_angle = map(self.myDancer[0].sensors[RF].roll, -90,90, 0, TWO_PI)
        self.rf_pi = map(self.myDancer[0].sensors[RF].pitch, -180, 180, 15, 200)
        
        #fun stuff
        self.fun1 = map(self.myDancer[0].sensors[RF].x1, -4, 4, width/2, width+200)
        self.fun2 = map(self.myDancer[0].sensors[LF].head, 0, 360, -100, height+100)
        self.fun3 = map(self.myDancer[0].sensors[RH].pitch, -180, 180, -100, height+100)
        self.fun4 = map(self.myDancer[0].sensors[LH].roll, -90, 90, -100, height+100)
        self.fun5 = map(self.myDancer[0].sensors[RF].z1, -4, 4, 0, 26)
        
        
    def draw(self):

        noStroke()

        # BRUSH ONE
        if(self.pingTimerst1.isFinished()):    
            #self.col = self.colarray[ceil(random(0,21))]
            self.col = self.colarray[ceil(self.fun5)]
            self.myStroke = Brush.Brush(self.lh_xpos, self.lh_ypos, self.rh_xpos, self.rh_ypos, 2, self.col, 25, self.rh_pi)
            
            self.pingTimerst1.start()
            
        if(self.myStroke != None):
                
            self.myStroke.calculate_stroke()
            self.myStroke.brush_stroke()
            
        # BRUSH TWO 
        if(self.pingTimerst2.isFinished()):
            #self.col = self.colarray[ceil(random(0,21))]
            self.col = self.colarray[ceil(self.fun5)]
            self.myStroke2 = Brush.Brush(self.lf_xpos, self.lf_ypos, self.rf_xpos, self.rf_ypos, 2, self.col, 20, self.lh_pi)
            
            self.pingTimerst2.start()
            
        if(self.myStroke2 != None):
            
            self.myStroke2.calculate_stroke()
            self.myStroke2.brush_stroke() 
            
        # BRUSH THREE    
        if(self.pingTimerst3.isFinished()):
            self.col = self.colarray[ceil(random(0,2))]
            self.myStroke3 = Brush.Brush(self.lf_xpos, self.lh_ypos, self.rh_xpos, self.rf_ypos, 2, self.col, 10, 100)
            
            self.pingTimerst3.start()
            
        if(self.myStroke3 != None):
            
            self.myStroke3.calculate_stroke()
            self.myStroke3.brush_stroke() 
            
        # BRUSH FOUR
        if(self.pingTimerst4.isFinished()):    
            #self.col = self.colarray[ceil(random(0,21))]
            self.col = self.colarray[ceil(self.fun5)]
            self.myStroke4 = Brush.Brush(self.fun1, self.fun2, self.fun3, self.fun4, 2, self.col, 60, self.rf_pi)
            
            self.pingTimerst4.start()
            
        if(self.myStroke4 != None):
                
            self.myStroke4.calculate_stroke()
            self.myStroke4.brush_stroke()

        #BRUSH FIVE
        if(self.pingTimerst5.isFinished()):    
            #self.col = self.colarray[ceil(random(0,21))]
            self.col = self.colarray[ceil(self.fun5)]
            self.myStroke5 = Brush.Brush(self.fun1-width, self.fun4, self.fun3-width, self.fun2, 2, self.col, 60, self.lf_pi)
            
            self.pingTimerst5.start()
            
        if(self.myStroke5 != None):
                
            self.myStroke5.calculate_stroke()
            self.myStroke5.brush_stroke()


    def addDancer(self, d, index):
        self.myDancer[index] = d
