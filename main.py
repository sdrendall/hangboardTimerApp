# Main for Hangboard Timer App

#import kivy
#kivy.require("1.7.2")

import math

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, NumericProperty, BooleanProperty


# Timer object, stores value for each timer/counter, can start, stop, increment and decrement.
class timer(Widget):
	active = BooleanProperty(False)
	value = NumericProperty(10)	
	
	def startTimer(self):
		self.active=True
	
	def stopTimer(self):
		self.active=False
		
	def increment(self, delta):
		self.value += delta
		
	def decrement(self, delta):
		self.value -= delta
	
class mainWindow(Widget):
	repCounter = timer()
	holdTimer = timer()
	restTimer = timer()
	pauseTimer = timer()
	
	def refresh(self, dt):
		if self.repCounter.active == True:
			self.repCounter.decrement(dt)
			self.repCounter.displayedValue = math.floor\
			(self.repCounter.value)
		
		if self.holdTimer.active == True:
			self.holdTimer.decrement(dt)
			self.holdTimer.displayedValue = NumericProperty (math.floor(self.repCounter.value))
		
		if self.restTimer.active == True:
			self.restTimer.decrement(dt)
			
		if self.pauseTimer.active == True:
			self.pauseTimer.decrement(dt)
		#print math.floor(self.holdTimer.displayedValue)
	pass
	
# Define App class
class timerApp(App):
	def build(self):
		display = mainWindow()
		display.holdTimer.startTimer()
		Clock.schedule_interval(display.refresh, 1/60)
		return mainWindow()
		
		
if __name__ == '__main__':
	timerApp().run()
	
