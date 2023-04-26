import Dancer
LH = "LH"
RH = "RH"
LF = "LF"
RF = "RF"

    
class Group01_Scene():
 


    num_dancers = 0
    r = random(101,161)
    g = random(41,98)
    b = 0
    gray = 40
    graychange = 0.05
    rchange = 0.05
    gchange = 0.05
    myDancer = [None]
    
    def __init__(self, num_d):
        #super.__init__(self)
        self.num_dancers = num_d
        self.myDancer = [None] * self.num_dancers

        
    def start(self):
        noStroke()
        background(120)

                
    def update(self):
        #left hand position update
        self.l_xpos = map(self.myDancer[0].sensors[LH].x1, -4, 4, (width * -0.1), width*1.25)
        self.l_ypos = map(self.myDancer[0].sensors[LH].y1, -4, 4, (height * -0.18), height*1.25)
        self.l_angle = map(self.myDancer[0].sensors[LH].roll, -90,90, 0, TWO_PI)
        '''
        #left foot position update
        self.lf_xpos = map(self.myDancer[0].sensors[LF].x1, -4, 4, 0, width*1.25)
        self.lf_ypos = map(self.myDancer[0].sensors[LF].y1, -4, 4, 0, height*1.25)
        self.lf_angle = map(self.myDancer[0].sensors[LF].roll, -90,90, 0, TWO_PI)
        '''
        #right hand position update
        self.r_xpos = map(self.myDancer[0].sensors[RH].x1, -4, 4, (width * -0.1), width*1.25)
        self.r_ypos = map(self.myDancer[0].sensors[RH].y1, -4, 4, (height * -0.37), height*1.25)
        self.r_angle = map(self.myDancer[0].sensors[RH].roll, -90,90, 0, TWO_PI)
        '''
        #right foot position update
        self.rf_xpos = map(self.myDancer[0].sensors[RF].x1, -4, 4, 0, width*1.25)
        self.rf_ypos = map(self.myDancer[0].sensors[RF].y1, -4, 4, 0, height*1.25)
        self.rf_angle = map(self.myDancer[0].sensors[RF].roll, -90,90, 0, TWO_PI)
        '''
        #color updating
        self.r = self.r + self.rchange
        if (self.r > 162) or (self.r <100) :
            self. rchange = self.rchange * -1
        self.g = self.g + self.gchange
        if (self.g > 99) or (self.g <40) :
            self. gchange = self.gchange * -1
        self.b = 255 - millis()/500
        self.gray = self.gray + self.graychange
        if (self.gray >201) or (self.gray < 29):
            self.graychange = self.graychange * -1

    def draw(self):
        #background(255)
        global brush1
        
        
        #left hand
        noStroke()
        pushMatrix()
        rectMode(CENTER)
        imageMode(CENTER)
        translate(self.l_xpos, self.l_ypos)
        rotate(self.l_angle)
        brush1 = loadImage("brush5.png")
        brush2 = loadImage("brush2.png")
        brush3 = loadImage("brush3.png")
        brush4 = loadImage("brush4.png")
        tint(self.r,self.g,0)
        if (self.myDancer[0].sensors[LH].x1 > -1) and (self.myDancer[0].sensors[LH].x1 < 1):
            image(brush1,0,0)
        if (self.myDancer[0].sensors[LH].x1 < 2) and (self.myDancer[0].sensors[LH].x1 > 1):
            image(brush2,0,0)
        if (self.myDancer[0].sensors[LH].x1 > -2) and (self.myDancer[0].sensors[LH].x1 < -1):
            image(brush2,0,0)
        if (self.myDancer[0].sensors[LH].x1 < 3) and (self.myDancer[0].sensors[LH].x1 > 2):
            image(brush4,0,0)
        if (self.myDancer[0].sensors[LH].x1 > -3) and (self.myDancer[0].sensors[LH].x1 < -2):
            image(brush4,0,0)
        if (self.myDancer[0].sensors[LH].x1 < 4) and (self.myDancer[0].sensors[LH].x1 > 3):
            image(brush4,0,0)
        if (self.myDancer[0].sensors[LH].x1 > -4) and (self.myDancer[0].sensors[LH].x1 < -3):
            image(brush4,0,0)
        popMatrix()
        '''
        #left foot
        noStroke()
        pushMatrix()
        rectMode(CENTER)
        imageMode(CENTER)
        translate(self.lf_xpos, self.lf_ypos)
        rotate(self.lf_angle)
        brush1 = loadImage("brush5.png")
        brush2 = loadImage("brush2.png")
        brush3 = loadImage("brush3.png")
        brush4 = loadImage("brush4.png")
        tint(255)
        if (self.myDancer[0].sensors[LF].x1 > -1) and (self.myDancer[0].sensors[LF].x1 < 1):
            image(brush3,0,0)
        if (self.myDancer[0].sensors[LF].x1 < 2) and (self.myDancer[0].sensors[LF].x1 > 1):
            image(brush2,0,0)
        if (self.myDancer[0].sensors[LF].x1 > -2) and (self.myDancer[0].sensors[LF].x1 < -1):
            image(brush2,0,0)
        if (self.myDancer[0].sensors[LF].x1 < 3) and (self.myDancer[0].sensors[LF].x1 > 2):
            image(brush4,0,0)
        if (self.myDancer[0].sensors[LF].x1 > -3) and (self.myDancer[0].sensors[LF].x1 < -2):
            image(brush4,0,0)
        if (self.myDancer[0].sensors[LF].x1 < 4) and (self.myDancer[0].sensors[LF].x1 > 3):
            image(brush4,0,0)
        if (self.myDancer[0].sensors[LF].x1 > -4) and (self.myDancer[0].sensors[LF].x1 < -3):
            image(brush4,0,0)
        popMatrix()
        '''
        #right hand
        pushMatrix()
        rectMode(CENTER)
        imageMode(CENTER)
        translate(self.r_xpos, self.r_ypos)
        rotate(self.r_angle)
        brush1 = loadImage("brush5.png")
        brush2 = loadImage("brush2.png")
        brush3 = loadImage("brush3.png")
        brush4 = loadImage("brush4.png")
        tint(self.gray,self.gray,self.gray)
        if (self.myDancer[0].sensors[LH].x1 > -1) and (self.myDancer[0].sensors[LH].x1 < 1):
            image(brush1,0,0)
        if (self.myDancer[0].sensors[LH].x1 < 2) and (self.myDancer[0].sensors[LH].x1 > 1):
            image(brush2,0,0)
        if (self.myDancer[0].sensors[LH].x1 > -2) and (self.myDancer[0].sensors[LH].x1 < -1):
            image(brush2,0,0)
        if (self.myDancer[0].sensors[LH].x1 < 3) and (self.myDancer[0].sensors[LH].x1 > 2):
            image(brush4,0,0)
        if (self.myDancer[0].sensors[LH].x1 > -3) and (self.myDancer[0].sensors[LH].x1 < -2):
            image(brush4,0,0)
        if (self.myDancer[0].sensors[LH].x1 < 4) and (self.myDancer[0].sensors[LH].x1 > 3):
            image(brush4,0,0)
        if (self.myDancer[0].sensors[LH].x1 > -4) and (self.myDancer[0].sensors[LH].x1 < -3):
            image(brush4,0,0)   
        popMatrix()
        
        '''
        #right foot
        noStroke()
        pushMatrix()
        rectMode(CENTER)
        imageMode(CENTER)
        translate(self.rf_xpos, self.rf_ypos)
        rotate(self.rf_angle)
        brush1 = loadImage("brush5.png")
        brush2 = loadImage("brush2.png")
        brush3 = loadImage("brush3.png")
        brush4 = loadImage("brush4.png")
        tint(0)
        if (self.myDancer[0].sensors[RF].x1 > -1) and (self.myDancer[0].sensors[RF].x1 < 1):
            image(brush3,0,0)
        if (self.myDancer[0].sensors[RF].x1 < 2) and (self.myDancer[0].sensors[RF].x1 > 1):
            image(brush2,0,0)
        if (self.myDancer[0].sensors[RF].x1 > -2) and (self.myDancer[0].sensors[RF].x1 < -1):
            image(brush2,0,0)
        if (self.myDancer[0].sensors[RF].x1 < 3) and (self.myDancer[0].sensors[RF].x1 > 2):
            image(brush4,0,0)
        if (self.myDancer[0].sensors[RF].x1 > -3) and (self.myDancer[0].sensors[RF].x1 < -2):
            image(brush4,0,0)
        if (self.myDancer[0].sensors[RF].x1 < 4) and (self.myDancer[0].sensors[RF].x1 > 3):
            image(brush4,0,0)
        if (self.myDancer[0].sensors[RF].x1 > -4) and (self.myDancer[0].sensors[RF].x1 < -3):
            image(brush4,0,0)
        popMatrix()
        '''
        
    def addDancer(self, d, index):
        self.myDancer[index] = d
