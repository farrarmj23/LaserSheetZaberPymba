#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.24.1
#  in conjunction with Tcl version 8.6
#    Dec 04, 2019 03:51:01 PM EST  platform: Windows NT

import sys
import zaber.serial as zaber
import numpy as np
import serial.tools.list_ports
import threading

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = StageControl (root)
    root.mainloop()

w = None
def create_StageControl(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = StageControl (w)
    return (w, top)

def destroy_StageControl():
    global w
    w.destroy()
    w = None

class StageControl:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("470x217+0+500")
        top.title("Stage Control")
        top.configure(background="#d9d9d9")
        

        #T-LSM100A Stage Parameters
        self.posConversion = 4.7625e-5 #microstepsize in um
        self.speedConversion = 4.465e-4 #convert speed from mm/s to native
        self.accelConversion = 0.5358 #convert accel from mm/s^2 to native
        self.maxSpeed = 7.00 #max speed in mm/s
        self.minSpeed = 0.000446 #min speed in mm/s
        self.minPos = 0 #minimum position in mm
        self.maxPos = 100 #maximum position in mm
        self.minAccel = 0.54 #minimum acceleration in mm/s^2
        self.maxAccel = 200 #user imposed in mm/s^2
        self.defaultAccel = 60 #default acceleration in mm/s^2

        self.homeButton = tk.Button(top)
        self.homeButton.place(relx=0.745, rely=0.876, height=24, width=44)
        self.homeButton.configure(activebackground="#ececec")
        self.homeButton.configure(activeforeground="#000000")
        self.homeButton.configure(background="#d9d9d9")
        self.homeButton.configure(disabledforeground="#a3a3a3")
        self.homeButton.configure(foreground="#000000")
        self.homeButton.configure(highlightbackground="#d9d9d9")
        self.homeButton.configure(highlightcolor="black")
        self.homeButton.configure(pady="0")
        self.homeButton.configure(text='''Home''')
        self.homeButton.configure(command = self.goHome)

        self.gotoButton = tk.Button(top)
        self.gotoButton.place(relx=0.42, rely=0.876, height=24, width=44)
        self.gotoButton.configure(activebackground="#ececec")
        self.gotoButton.configure(activeforeground="#000000")
        self.gotoButton.configure(background="#d9d9d9")
        self.gotoButton.configure(disabledforeground="#a3a3a3")
        self.gotoButton.configure(foreground="#000000")
        self.gotoButton.configure(highlightbackground="#d9d9d9")
        self.gotoButton.configure(highlightcolor="black")
        self.gotoButton.configure(pady="0")
        self.gotoButton.configure(text='''GoTo''')
        self.gotoButton.configure(command = self.moveAbs)

        self.setKinematics = tk.Button(top)
        self.setKinematics.place(relx=0.106, rely=0.72, height=24, width=27)
        self.setKinematics.configure(activebackground="#ececec")
        self.setKinematics.configure(activeforeground="#000000")
        self.setKinematics.configure(background="#d9d9d9")
        self.setKinematics.configure(disabledforeground="#a3a3a3")
        self.setKinematics.configure(foreground="#000000")
        self.setKinematics.configure(highlightbackground="#d9d9d9")
        self.setKinematics.configure(highlightcolor="black")
        self.setKinematics.configure(pady="0")
        self.setKinematics.configure(text='''Set''')
        self.setKinematics.configure(command = self.setKin)

        self.setSpeedVar = tk.StringVar()
        self.setSpeedVar.set('1.00')
        self.setSpeed = tk.Entry(top)
        self.setSpeed.place(relx=0.064, rely=0.23,height=30, relwidth=0.157)
        self.setSpeed.configure(background="white")
        self.setSpeed.configure(disabledforeground="#a3a3a3")
        self.setSpeed.configure(font="TkFixedFont")
        self.setSpeed.configure(foreground="#000000")
        self.setSpeed.configure(insertbackground="black")
        self.setSpeed.configure(width=74)
        self.setSpeed.configure(justify = 'center')
        self.setSpeed.configure(textvariable = self.setSpeedVar)

        self.setAccelVar = tk.StringVar()
        self.setAccelVar.set('1.00')
        self.setAccel = tk.Entry(top)
        self.setAccel.place(relx=0.064, rely=0.53,height=30, relwidth=0.157)
        self.setAccel.configure(background="white")
        self.setAccel.configure(disabledforeground="#a3a3a3")
        self.setAccel.configure(font="TkFixedFont")
        self.setAccel.configure(foreground="#000000")
        self.setAccel.configure(insertbackground="black")
        self.setAccel.configure(width=74)
        self.setAccel.configure(justify = 'center')
        self.setAccel.configure(textvariable = self.setAccelVar)

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.064, rely=0.092, height=21, width=84)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Speed (mm/s)''')
        self.Label1.configure(width=84)

        self.Label7 = tk.Label(top)
        self.Label7.place(relx=0.034, rely=0.4, height=21, width=124)
        self.Label7.configure(background="#d9d9d9")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(text='''Acceleration (mm/s^2)''')

        self.Label8 = tk.Label(top)
        self.Label8.place(relx=0.064, rely=0.092, height=21, width=84)
        self.Label8.configure(background="#d9d9d9")
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(foreground="#000000")
        self.Label8.configure(text='''Speed (mm/s)''')
        self.Label8.configure(width=84)
        self.Label8 = tk.Label(top)
        self.Label8.place(relx=0.34, rely=0.62, height=21, width=129)
        self.Label8.configure(background="#d9d9d9")
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(foreground="#000000")
        self.Label8.configure(text='''Move Abs. (mm)''')


        self.moveAbsVar = tk.StringVar()
        self.moveAbsVar.set('0.000')
        self.moveAbsVal = tk.Entry(top)
        self.moveAbsVal.place(relx=0.383, rely=0.71,height=30, relwidth=0.157)
        self.moveAbsVal.configure(background="white")
        self.moveAbsVal.configure(disabledforeground="#a3a3a3")
        self.moveAbsVal.configure(font="TkFixedFont")
        self.moveAbsVal.configure(foreground="#000000")
        self.moveAbsVal.configure(insertbackground="black")
        self.moveAbsVal.configure(width=74)
        self.moveAbsVal.configure(justify = 'center')
        self.moveAbsVal.configure(textvariable = self.moveAbsVar)

        self.smallStepSizeVar = tk.StringVar()
        self.smallStepSizeVar.set("1")
        self.smallStepSize = tk.Entry(top)
        self.smallStepSize.place(relx=0.383, rely=0.12, height=30
                , relwidth=0.157)
        self.smallStepSize.configure(background="white")
        self.smallStepSize.configure(disabledforeground="#a3a3a3")
        self.smallStepSize.configure(font="TkFixedFont")
        self.smallStepSize.configure(foreground="#000000")
        self.smallStepSize.configure(insertbackground="black")
        self.smallStepSize.configure(width=74)
        self.smallStepSize.configure(justify = "center")
        self.smallStepSize.configure(textvariable = self.smallStepSizeVar)

        self.largeStepSizeVar = tk.StringVar()
        self.largeStepSizeVar.set("10")
        self.largeStepSize = tk.Entry(top)
        self.largeStepSize.place(relx=0.383, rely=0.35, height=30
                , relwidth=0.157)
        self.largeStepSize.configure(background="white")
        self.largeStepSize.configure(disabledforeground="#a3a3a3")
        self.largeStepSize.configure(font="TkFixedFont")
        self.largeStepSize.configure(foreground="#000000")
        self.largeStepSize.configure(insertbackground="black")
        self.largeStepSize.configure(width=74)
        self.largeStepSize.configure(justify = 'center')
        self.largeStepSize.configure(textvariable = self.largeStepSizeVar)

        self.relPosVar = tk.StringVar()
        self.relPosVar.set('0.000')
        self.relPositionText = tk.Entry(top)
        self.relPositionText.place(relx=0.66, rely=0.23, height=30, relwidth=0.264)
        self.relPositionText.configure(background="white")
        self.relPositionText.configure(disabledforeground="#a3a3a3")
        self.relPositionText.configure(font="TkFixedFont")
        self.relPositionText.configure(foreground="#000000")
        self.relPositionText.configure(insertbackground="black")
        self.relPositionText.configure(state='readonly')
        self.relPositionText.configure(width=124)
        self.relPositionText.configure(textvariable = self.relPosVar)
        self.relPositionText.configure(justify='center')

        self.absPosVar = tk.StringVar()
        self.absPosVar.set('0.000')
        self.positionText = tk.Entry(top)
        self.positionText.place(relx=0.66, rely=0.691, height=30, relwidth=0.264)
        self.positionText.configure(background="white")
        self.positionText.configure(disabledforeground="#a3a3a3")
        self.positionText.configure(font="TkFixedFont")
        self.positionText.configure(foreground="#000000")
        self.positionText.configure(insertbackground="black")
        self.positionText.configure(state='readonly')
        self.positionText.configure(width=124)
        self.positionText.configure(justify = 'center')
        self.positionText.configure(textvariable = self.absPosVar)

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.34, rely=0.025, height=21, width=117)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Small Step Size (mm)''')

        self.Label4 = tk.Label(top)
        self.Label4.place(relx=0.34, rely=0.25, height=21, width=117)
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''Large Step Size (mm)''')

        self.Label5 = tk.Label(top)
        self.Label5.place(relx=0.66, rely=0.553, height=21, width=125)
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text='''Absolute Position (mm)''')

        self.largeRight = tk.Button(top)
        self.largeRight.place(relx=0.54, rely=0.5, height=24, width=27)
        self.largeRight.configure(activebackground="#ececec")
        self.largeRight.configure(activeforeground="#000000")
        self.largeRight.configure(background="#d9d9d9")
        self.largeRight.configure(disabledforeground="#a3a3a3")
        self.largeRight.configure(foreground="#000000")
        self.largeRight.configure(highlightbackground="#d9d9d9")
        self.largeRight.configure(highlightcolor="black")
        self.largeRight.configure(pady="0")
        self.largeRight.configure(text='''>>''')
        self.largeRight.configure(command = lambda stepSize ='large',direction = 'right': self.moveRel(stepSize,direction))


        self.smallRight = tk.Button(top)
        self.smallRight.place(relx=0.48, rely=0.5, height=24, width=29)
        self.smallRight.configure(activebackground="#ececec")
        self.smallRight.configure(activeforeground="#000000")
        self.smallRight.configure(background="#d9d9d9")
        self.smallRight.configure(disabledforeground="#a3a3a3")
        self.smallRight.configure(foreground="#000000")
        self.smallRight.configure(highlightbackground="#d9d9d9")
        self.smallRight.configure(highlightcolor="black")
        self.smallRight.configure(pady="0")
        self.smallRight.configure(text='''>''')
        self.smallRight.configure(width=29)
        self.smallRight.configure(command = lambda stepSize ='small',direction = 'right': self.moveRel(stepSize,direction))


        self.smallLeft = tk.Button(top)
        self.smallLeft.place(relx=0.40, rely=0.5, height=24, width=29)
        self.smallLeft.configure(activebackground="#ececec")
        self.smallLeft.configure(activeforeground="#000000")
        self.smallLeft.configure(background="#d9d9d9")
        self.smallLeft.configure(disabledforeground="#a3a3a3")
        self.smallLeft.configure(foreground="#000000")
        self.smallLeft.configure(highlightbackground="#d9d9d9")
        self.smallLeft.configure(highlightcolor="black")
        self.smallLeft.configure(pady="0")
        self.smallLeft.configure(text='''<''')
        self.smallLeft.configure(width=29)
        self.smallLeft.configure(command = lambda stepSize ='small',direction = 'left': self.moveRel(stepSize,direction))


        self.largeLeft = tk.Button(top)
        self.largeLeft.place(relx=0.33, rely=0.5, height=24, width=37)
        self.largeLeft.configure(activebackground="#ececec")
        self.largeLeft.configure(activeforeground="#000000")
        self.largeLeft.configure(background="#d9d9d9")
        self.largeLeft.configure(disabledforeground="#a3a3a3")
        self.largeLeft.configure(foreground="#000000")
        self.largeLeft.configure(highlightbackground="#d9d9d9")
        self.largeLeft.configure(highlightcolor="black")
        self.largeLeft.configure(pady="0")
        self.largeLeft.configure(text='''<<''')
        self.largeLeft.configure(width=37)
        self.largeLeft.configure(command = lambda stepSize ='large',direction = 'left': self.moveRel(stepSize,direction))

        self.setZero = tk.Button(top)
        self.setZero.place(relx=0.74, rely=0.42, height=24, width=50)
        self.setZero.configure(activebackground="#ececec")
        self.setZero.configure(activeforeground="#000000")
        self.setZero.configure(background="#d9d9d9")
        self.setZero.configure(disabledforeground="#a3a3a3")
        self.setZero.configure(foreground="#000000")
        self.setZero.configure(highlightbackground="#d9d9d9")
        self.setZero.configure(highlightcolor="black")
        self.setZero.configure(pady="0")
        self.setZero.configure(text='''Set Zero''')
        self.setZero.configure(command = self.setRelZero)

        self.Label6 = tk.Label(top)
        self.Label6.place(relx=0.66, rely=0.092, height=21, width=125)
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(text='''Relative Position (mm)''')

        #Connect to Stage and Read Current Parameters
        self.device = self.connectToStage()
        self.setAbsPos()
        speed = self.getCurrentSpeed()
        self.setSpeedVar.set('%.3f' % speed)
        accel = self.accelConversion*(self.device.send(43,np.int32(self.defaultAccel/self.accelConversion))).data 
        self.setAccelVar.set('%.3f' % accel)

    def getMaxSpeed(self):
        maxSpeed = self.device.send(53,29)
        maxSpeed = float(maxSpeed)*self.speedConversion
        return(maxSpeed)

    def stopStage(self):
        self.device.send(23)

    def moveAtSpeed(self,speed = 7,sgn = 1):
        self.setSpeedVar.set(speed)
        self.setKin()
        self.device.move_vel(sgn*np.uint32(speed/self.speedConversion))

    
    def goHome(self):
        oldPos = self.device.get_position()*self.posConversion #position in mm
        self.device.home()#send device to home position, waits until complete
        self.setAbsPos()
        newPos = self.device.get_position()*self.posConversion #position in mm
        displacement = newPos-oldPos
        relPos = float(self.relPosVar.get())+displacement 
        self.relPosVar.set('%.3f' % relPos)

    def moveRel(self,stepSize,direction,threaded = True):

        #determine which step size to use
        if stepSize == 'small':
            stepString = self.smallStepSizeVar.get()
        elif stepSize == 'large':
            stepString = self.largeStepSizeVar.get() 
        else:
            stepString = stepSize #use input value

        #determine which direction to move in
        if direction == 'left':
            sgn = 1
        elif direction == 'right':
            sgn = -1
        else:
            sgn = direction #use input value, given as a number
        
        if self.checkIsNum(stepString):
            if threaded:#non-blocking
                v = threading.Thread(target = self.moveRelUpdate,args = (sgn,stepString))
                v.start()
            else:#blocking
                self.moveRelUpdate(sgn,stepString) 
        else:
            print('Not a valid step size')


    def moveRelUpdate(self,sgn,stepString):
        stepSize = sgn*float(stepString) #step in mm with +/- direction
        delta = np.int32(stepSize/self.posConversion) #convert to microsteps
        self.device.move_rel(delta)   #move; waits until complete
        relPos = float(self.relPosVar.get())+stepSize
        self.relPosVar.set(str(relPos))
        self.setAbsPos()

    def moveAbs(self,threaded = True):
        if self.checkIsNum(self.moveAbsVar.get()):
            if (float(self.moveAbsVar.get())<=self.maxPos) & (float(self.moveAbsVar.get())>=self.minPos):
                if threaded:
                    v = threading.Thread(target = self.movePosUpdate)
                    v.start()
                else: #Waits for stage to move (i.e. is blocking)
                    self.movePosUpdate()
            else:
                print('Requested position is outside of bounds')
        else:
            print("Invalid Entry")

    def movePosUpdate(self):
        oldPos = self.device.get_position()*self.posConversion #position in mm
        requestedPos = float(self.moveAbsVar.get())/self.posConversion #position in microsteps
        self.device.move_abs(np.int32(requestedPos))
        newPos = self.device.get_position()*self.posConversion #position in mm
        self.setAbsPos()
        displacement = newPos-oldPos
        relPos = float(self.relPosVar.get())+displacement 
        self.relPosVar.set('%.3f' % relPos)
        
    def setAbsPos(self):
        absPos = np.float(self.device.get_position())*self.posConversion
        self.absPosVar.set('%.3f' % absPos)
    
    def setRelZero(self):
        self.relPosVar.set('0.000')
        
    def checkIsNum(self,inString):
        return(inString.replace('.','',1).isnumeric()) #true if a valid decimal number, false otherwise

    def setKin(self):

        #Set Speed
        if self.checkIsNum(self.setSpeedVar.get()):
            requestedSpeed = float(self.setSpeedVar.get())
            if (requestedSpeed< self.maxSpeed) & (requestedSpeed> self.minSpeed):
                speedInNative = requestedSpeed/self.speedConversion
                speedInNative = self.device.send(42,np.int32(speedInNative))
                speedInmms = float(speedInNative.data)*self.speedConversion
                self.setSpeedVar.set('%.3f' % speedInmms)
                
            else:
                speedInNative = 5.00/self.speedConversion
                speedInNative = self.device.send(42,np.int32(speedInNative))
                speedInmms = float(speedInNative.data)*self.speedConversion
                self.setSpeedVar.set('%.3f' % speedInmms)
                print("Speed out of bounds, setting to 5 mm/s")
        else:
            print("Invalid entry: speed is not changed")

        #Set Acceleration
        if self.checkIsNum(self.setAccelVar.get()):
            requestedAccel = float(self.setAccelVar.get())
            if (requestedAccel< self.maxAccel) & (requestedAccel> self.minAccel):
                accelInNative = requestedAccel/self.accelConversion
                accelInNative = self.device.send(43,np.int32(accelInNative))
                accelInmms2 = float(accelInNative.data)*self.accelConversion
                self.setAccelVar.set('%.3f' % accelInmms2)
            else:
                accelInNative = self.defaultAccel/self.accelConversion
                accelInNative = self.device.send(43,np.int32(accelInNative))
                accelInmms2 = float(accelInNative.data)*self.accelConversion
                self.setAccelVar.set('%.3f' % accelInmms2)
                print("Acceleration out of bounds, setting to 60 mm/s^2")
        else:
            print("Invalid Entry: acceleration is not changed")

    def setCurrentSpeed(self,requestedSpeed):
        if (requestedSpeed< self.maxSpeed) & (requestedSpeed> self.minSpeed):
            speedInNative = requestedSpeed/self.speedConversion
            speedInNative = self.device.send(42,np.int32(speedInNative))
            speedInmms = float(speedInNative.data)*self.speedConversion
            self.setSpeedVar.set('%.3f' % speedInmms)
        else:
            speedInNative = 5.00/self.speedConversion
            speedInNative = self.device.send(42,np.int32(speedInNative))
            speedInmms = float(speedInNative.data)*self.speedConversion
            self.setSpeedVar.set('%.3f' % speedInmms)
            print("Speed out of bounds, setting to 5 mm/s")
        return(speedInmms)
                
    def getCurrentPosition(self):
        absPos = np.float(self.device.get_position())*self.posConversion
        return(absPos)

    def getCurrentSpeed(self):
        speed = self.speedConversion*(self.device.send(53,42)).data
        return(speed)

    def getCurrentAccel(self):
        accel = self.accelConversion*(self.device.send(53,43)).data
        return(accel)

    def connectToStage(self):
        ports = list(serial.tools.list_ports.comports())
        comport = 0
        for p in ports:
            if (p.vid ==1659) & (p.pid==8963):
                comport = p.device

        if comport:
            zaberPort = zaber.BinarySerial(comport,baud=9600,timeout=30)
            zaberStage = zaber.BinaryDevice(zaberPort,1)
        else:
            zaberStage = 0
        return(zaberStage)
    

if __name__ == '__main__':
    vp_start_gui()





