import sys

import qi

import logging



class RobotController(object):
    
    def __init__(self, ip = '10.30.0.110', port = 9559, useSpanish = True):
        
        self.ip = ip
        self.port = port
        self.useSpanish = useSpanish
        self.session = qi.Session()
        
    
    def connect_to_robot(self):
        
        try:            
            self.session.connect("tcp://" + self.ip + ":" + str(self.port))
            
        except RuntimeError:
            logging.debug("Can't connect to Naoqi at ip \"" + self.ip + "\" on port " + str(self.port) +".\n"
                          "Please check your script arguments. Run with -h option for help.")
            sys.exit(1)
            
        self.animatedSpeechProxy = self.session.service("ALAnimatedSpeech")
    
        self.tts = self.session.service("ALTextToSpeech")
        
        self.configuration = {"bodyLanguageMode":"contextual"}
        
    def say(self):
        self.tts.say('Hello I am Hansel')
        
        
        
    