"""
--------------------------------------------------------------------------
Medication Dispenser
--------------------------------------------------------------------------
License:   
Copyright 2022 Sara Barker

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this 
list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE 
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, 
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

The display code borrows from code written by Angelica Torres.
(https://github.com/alt7rice/ENGI301/blob/main/project_01/rgb_lcd/rgb_lcd_test.py)
Their licensing information is: 
  - SPDX-FileCopyrightText: Copyright 2021 Angelica Torres
  - SPDX-License-Identifier: MIT
  
The IR code borrows from code written by Adafruit.
(https://learn.adafruit.com/ir-breakbeam-sensors/circuitpython)


--------------------------------------------------------------------------

This program operates a conveyor belt, driven by a servo motor, that drops medication into
a user's hand when they place their hand under the dispensing area and block an IR beam.

Requirements:
  - If the dispenser has not been used today, and a hand blocks the IR beam, move the conveyor
    belt forward to dispense pills.
  - If the IR beam is blocked and pills have already been taken for the day, do nothing.
  - Display messages on a digital display whether pills have been taken for the day or not.
  - Display message every 7 days to remind users to refill pills.

Uses:
  - time
  - Adafruit BBIO
  - board
  - digitalio
  - Adafruit character lcd

"""
import time
import Adafruit_BBIO.PWM as PWM


#needed for display
import board
import digitalio
import adafruit_character_lcd.character_lcd as charlcd


# ------------------------------------------------------------------------
# Constants
# ------------------------------------------------------------------------

#constants for servo
SG90_FREQ   = 333                  # 20ms period (50Hz)
SG90_POL    = 0                   # Rising Edge polarity
SG90_OFF    = 50                   # 0ms pulse -- Servo is inactive
SG90_RIGHT  = 15                   # 1ms pulse (15% duty cycle)  -- All the way right
SG90_LEFT   = 80                 # 2ms pulse (80% duty cycle) -- All the way Left


# ------------------------------------------------------------------------
# Functions / Classes
# ------------------------------------------------------------------------

class Servo():
    servo      = None
    
    def __init__(self, servo="P1_36"):
        """ Initialize variables and set up display """
        self.servo      = servo
        
        self._setup()
    
    # End def
    
    
    def _setup(self):
        """Setup the hardware components."""
        # Initialize Servo; Servo should be "off"
        PWM.start(self.servo, SG90_OFF, SG90_FREQ, SG90_POL)

    # End def


    def moveBack(self):
        #move servo counterclockwise to move conveyor belt back
        PWM.set_duty_cycle(self.servo, SG90_LEFT)

    # End def


    def moveFwd(self):
        #move servo clockwise to advance conveyor belt to next day
        PWM.set_duty_cycle(self.servo, SG90_RIGHT)

    # End def
    
    def zero(self):
        PWM.set_duty_cycle(self.servo, SG90_OFF)
    # End def

    def cleanup(self):
        """Cleanup the hardware components."""
        
        # Stop servo
        PWM.set_duty_cycle(self.servo, SG90_OFF)
        
    # End def

        

# End class

class Display():
    lcd     = None
    rows    = None
    columns = None
    
    
    def __init__(self, rs=board.P1_2, en=board.P1_4, d7=board.P2_24, d6=board.P2_22, d5=board.P2_20, d4=board.P2_18):
        self.rows    = 2
        self.columns = 16
        
        lcd_rs = digitalio.DigitalInOut(rs)
        lcd_en = digitalio.DigitalInOut(en)
        lcd_d7 = digitalio.DigitalInOut(d7)
        lcd_d6 = digitalio.DigitalInOut(d6)
        lcd_d5 = digitalio.DigitalInOut(d5)
        lcd_d4 = digitalio.DigitalInOut(d4)
        
        self.lcd = charlcd.Character_LCD_Mono(
            lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, self.columns, self.rows
        )
        
        self._setup()
    #end def
    
    def _setup(self):
        self.blank()
    #end def
    
    def blank(self):
        self.lcd.message = "                \n                "
        time.sleep(0.5)
    # End def
        
    def write(self, message):
        self.lcd.message = message
        time.sleep(0.5)
    
    #def refill(self, dayCounter)
        #if dayCounter = 6
            #lcd.message("Time to refill!")
            #dayCounter = 0
            #move servo backwards until back to 1st position
        #else
            #do nothing
            
            
    #end def
    
    
#End class

class IR():
    break_beam = None
    
    def __init__(self, break_beam = "P2_2"):
        self.break_beam = break_beam
        self._setup()
        
    def _setup(self):
        break_beam = digitalio.DigitalInOut(board.P2_2)
        break_beam.direction = digitalio.Direction.INPUT
        break_beam.pull = digitalio.Pull.UP
        
    def getValue(self):
        return break_beam.value
    
    
#end class

    


# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------

if __name__ == '__main__':
    startTime = time.time()
    
    
    dayCounter = 0
    takenToday = 0
    
    #instantiate instances of classes
    IRvalue = IR()
    servo = Servo()
    display = Display()
    
    display.write("You already took\ntoday's dose.")
    display.blank()
    
    
    #while(dayCounter < 6):
        #while(takenToday == 0):
            #if IRvalue.getValue == 0:
                
                #currentTime = time.time()
                #if currentTime-startTime < 1 min (note that this would change to a day)
                    #servo.moveFwd()
                    #time.pause() ---- need to figure out how long to run it
                #takenToday = 1
                #daycounter=daycounter+1
            #else
                #pass
        #while takenToday = 1
            #display.write("You already took\ntoday's dose.")

    dayCounter = 0
    print("Working")

    
