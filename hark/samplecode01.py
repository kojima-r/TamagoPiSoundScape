import harkpython.harkbasenode as harkbasenode
import json
import datetime
import RPi.GPIO as GPIO

class HarkNode(harkbasenode.HarkBaseNode):
    def __init__(self):
        # define the output names and types of your node as tuples here.
        self.outputNames=("OUTPUT",)
        self.outputTypes=("prim_bool",)
        now=datetime.datetime.now()
        filename="../data/loc{0:%Y%m%d-%H%M%S}.txt".format(now)
        self.fp=open(filename,"w")
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(6,GPIO.IN)
    def calculate(self):
        # write your code here.
        srcs=self.SOURCES
        self.fp.write(json.dumps(srcs))
        self.fp.write("\n")
        o= int(GPIO.input(6))
        if o==1:
            self.outputValues["OUTPUT"] =True
        else:
            self.outputValues["OUTPUT"] =False
