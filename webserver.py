import os
import bottle
import RPi.GPIO as GPIO
import time
import threading
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT,initial=False)
GPIO.setup(17,GPIO.OUT,initial=False)
GPIO.setup(27,GPIO.OUT,initial=False)
GPIO.setup(22,GPIO.OUT,initial=False)
HEAD = GPIO.PWM(22,50)
BOT = GPIO.PWM(4,50)
LEFT = GPIO.PWM(17,50)
RIGHT = GPIO.PWM(27,50)
trig = 18
echo = 23
GPIO.setup(trig,GPIO.OUT,initial = GPIO.LOW)
GPIO.setup(echo,GPIO.IN)

HEAD.start(8)
BOT.start(7.5)
LEFT.start(7.5)
RIGHT.start(7.5)
time.sleep(1)

import robot

directory = os.getcwd()
app = bottle.Bottle()

app.config.update({
    'autojson':False,
    'sqlite.db': 'memory:',
    'myapp.param':'value',
    'app.host':'0.0.0.0',
    'app.port':10004
    })

@app.route('/')
def index():
    return bottle.static_file('./template/bugthing.html', root=directory)

@app.route('/direction', method="POST")
def query():
    global dir
    dir = bottle.request.POST.get("direction")
    print(dir)
    print("hello1")
    return

@app.route('/mode', method="POST")
def query():
    global m
    m = bottle.request.POST.get("mode")
    print(m)
    print("hello")
    return

@app.hook('after_request')
def enable_cors():
    bottle.response.headers['Access-Control-Allow-Origin'] = '*'
    bottle.response.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS, GET'
    bottle.response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

@app.get('/<filename:path>', method="GET")
def server_static(filename):
    return bottle.static_file(filename, root=directory)

m = 'm'
dir = 's'

def t1():
    app.config.load_config('conf.ini')
    bottle.run(app, host='0.0.0.0', port=10004, debug=True)
    

if __name__ == '__main__':
    
    x = threading.Thread(target=t1, args=())
    x.start()
    print('thread done')
    while(True):
        robot.movement(m, dir)
        #time.sleep(1)
        #print(m)
        #print(dir)
        