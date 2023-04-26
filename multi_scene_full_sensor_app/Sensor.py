class Sensor:
    
    # Linear Acceleration, -4 to 4
    x1 = y1 = z1 = 0
    
    x2 = y2 = z2 = 0
    
    head = 0  # heading, range: 0 to 360
    pitch = 0 # range: -180 to 180
    roll = 0  # range: -90 to 90
    
    
    def __init__(self):
        self.x1 = self.y1 = self.z1 = 0
        self.x2 = self.y2 = self.z2 = 0 
        self.head = self.pitch = self.roll = 0   
        
    def update(self, h, p, r, x1, y1, z1):     #, x2, y2, z2):
        
        self.head = float(h)
        self.pitch = float(p)
        self.roll = float(r)
        
        
        self.x1 = float(x1)
        self.y1 = float(y1)
        self.z1 = float(z1)
        
        '''
        self.x2 = float(x2)
        self.y2 = float(y2)
        self.z2 = float(z2)
        '''
