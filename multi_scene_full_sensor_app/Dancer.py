add_library ('net')

import Sensor
import Timer

LH = "LH"
RH = "RH"
LF = "LF"
RF = "RF"

port = 12345



class Dancer:
    live = True
    rec_data = None
    myId = 0
    ip = 0
    client = None
    pingTimer = None
    
    counter = 0
    
    #def __init__(self, ip):
    def __init__(self, t_client, id, live):
        #self.ip = ip
        self.sensors = {}
        self.myId = id
        self.sensors[LH] = Sensor.Sensor()
        self.sensors[RH] = Sensor.Sensor()
        self.sensors[LF] = Sensor.Sensor()
        self.sensors[RF] = Sensor.Sensor()
        self.live = live
        
        #self.client = Client(this, self.ip, port)
        self.client = t_client
        
        self.pingTimer = Timer.Timer(1000)
        self.pingTimer.start()
        
        if not self.live:
            filename = ("dancer_data_%02d.txt" % self.myId)
            self.rec_data = loadStrings(filename)
            
        
    def update(self):
        # messages will look something like:
        #   1:LH,head,pitch,roll,xval,yval,zval;1:RH,head,pitch,roll,xval,yval,zval;1:LF,head,pitch,roll,xval,yval,zval;1:RF,head,pitch,roll,xval,yval,zval
        message = None
        
        if self.live:
            if self.client.available() > 0:
                #self.counter += 1
                message = self.client.readString()
            if(self.pingTimer.isFinished()):
                #print("send ping message")
                self.client.write("C")
                self.counter = 0
                self.pingTimer.start()
        else:
            message = self.rec_data[self.counter]
            self.counter = (self.counter +1) % len(self.rec_data)
            if(self.counter == 0):
                print("Rewinding rec_data")
                
        #print("message: ", message)    
        if message != None:
            sensor_messages = message.split(';')
            for i in range(4):
                if len(sensor_messages[i]):
                    data = sensor_messages[i].split(',')
                    id = data[0].split(':')
                    #print("id: ", id, " : id[0]: ", id[0])
                    self.sensors[id[1]].update(data[1], data[2], data[3], data[4], data[5], data[6])
              
    def disconnect(self):  
              self.client.write("Q")
              print("Dancer.disconnect(): wrote to client")
