add_library ('net')

live = False

import Group01_Scene
import Group02_Scene
import Group03_Scene

import Dancer

server = None

ips = ["192.168.0.200", "192.168.0.201", "192.168.0.202", "192.168.0.203"]
#ips = ["10.200.1.144", "ip1", "ip2", "ip3", "ip4"]
port = 12345

num_scenes = 3
num_dancers = 1
myScenes = [None] * num_scenes
myDancers = [None] * num_dancers
xres = 960
yres = 540
g_client = None

current_scene = 0
def setup():
    global myScenes
    global myDancers
    global server
    global ips
    global live
    global g_client
    
    print "i'm in setup"
    
    g_client = [None]* num_dancers
    for i in range(num_dancers):
        #myDancers[i] = Dancer.Dancer(ips[i])
        if live:
            g_client[i] = Client(this, ips[i], port)
            print ("g_client[", i, "]: ", g_client[i].host)
        else: 
            g_client[i] = None
        myDancers[i] = Dancer.Dancer(g_client[i], i, live)

    size(xres, yres, P2D)
    hint(DISABLE_DEPTH_MASK)
    myScenes[0] = Group01_Scene.Group01_Scene(num_dancers)
    myScenes[1] = Group02_Scene.Group02_Scene(num_dancers)
    myScenes[2] = Group03_Scene.Group03_Scene(num_dancers)
    for scene in range(num_scenes):
        for d in range(num_dancers):
            myScenes[scene].addDancer(myDancers[d], d)
            
    background(255)
    
    server = Server(this, 5200)
    print "Done with setup, let's roll"
    
    
def draw():
    global myScenes, current_scene
    global myDancers
    global server
    
    client = server.available()
    if (client != None):
        message = client.readString()
        print "message: " , message
        current_scene = int(message)% num_scenes
        print "current_scene: ", current_scene
        myScenes[current_scene].start()
    
    for i in range(num_dancers):
        myDancers[i].update()
        
    myScenes[current_scene].update()
    myScenes[current_scene].draw()
    
def mousePressed():
    global current_scene, num_scenes
    global myScenes
    current_scene = (current_scene +1) % num_scenes
    myScenes[current_scene].start()

def keyPressed():
    if key == 'Q':
        print("let's quit")
        for i in range(num_dancers):
            myDancers[i].disconnect()
            
def serverEvent(server, client):
  incomingMessage = "A new client has connected: " + client.ip();
  print(incomingMessage)
  
    
