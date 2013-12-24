# Main for Hangboard Timer App

#import kivy
#kivy.require("1.7.2")

import math

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, NumericProperty, BooleanProperty

# Workout object, stores workout routine, made an object so that
# it will allow for functions as I find them necessary.  
# May replace these with modules in the future
class Workout(object):
	
	def __init__(self):
		# Each workout has a routine, indexed by a number
		# (typically the repCounter) that corresponds to an
		# event (i.e hold, rest, pause) and a duration, in seconds
		# Workout.routine[repNumber] = ['event', duration]
		self.routine = {
			0: ['hold', 5],
			1: ['rest', 4],
			2: ['hold', 8],
			3: ['rest', 5],
			4: ['hold', 10],
			5: ['pause', 20]
			}
		self.currentRep = 0
		self.currentSet = 0
		self.numberOfSets = 3
	

# Counter class: Definitely dont need this.
class Counter(Widget):
	value = NumericProperty(0)
	
	def increment(self, delta):
		self.value += delta
		
	def decrement(self, delta):
		self.value -= delta
	

# Timer class: Widget that stores value for each timer/counter, can start, stop, increment and decrement.
# This could probably just be an object but kivy was being a prissy bitch (text was not displaying properly)
class Timer(Widget):
	active = BooleanProperty(False)
	value = NumericProperty(0)
		
	def __init__(self):
		self.state = 'off'
		
	def increment(self, delta, *args):
		self.value += delta
		
	def decrement(self, delta, *args):
		if self.value > 0:
			self.value -= delta
		else:
			self.stopTimer
			
	def stopTimer(self):
		if self.state == 'incrementing':
			Clock.unschedule(self.increment())
			self.state = 'off'
		elif self.state == 'decrementing':
			Clock.unschedule(self.decrement())
			self.state = 'off'
		elif self.state == 'off':
			print "WARNING: ATTEMPTED TO STOP TIMER THAT WAS NOT RUNNING"
		else:
			print "INVALID TIMER STATE: EXITING"
			exit(0)
	
	def startTimer(self, direction, startTime, dt):
		self.active = True
		self.value = startTime
		if direction == 'increasing':
			Clock.schedule_interval(self.increment, dt)
		elif direction == 'decreasing':
			Clock.schedule_interval(self.decrement, dt)			
		else:
			print 'Invalid timer mode: specify "increasing" or "decreasing"'
			exit(0)
		
class TimerUI(Widget):
	#repCounter = Counter()
	holdTimer = Timer()
	restTimer = Timer()
	pauseTimer = Timer()
	
	
	# Handle Timer Logic
	def startCorrectTimer(self):
		
	def startWorkout(self):
		self.workout = Workout()
		
	
	#def refresh(self, dt):
	#	if self.repCounter.active == True:
	#		self.repCounter.decrement(dt)
	#		
	#	if self.holdTimer.active == True:
	#		self.holdTimer.decrement(dt)
	#		
	#	if self.restTimer.active == True:
	#		self.restTimer.decrement(dt)
	#		
	#	if self.pauseTimer.active == True:
	#		self.pauseTimer.decrement(dt)
		#print math.floor(self.holdTimer.displayedValue)
	pass
	
# Define App class
class timerApp(App):
	def build(self):
		display = TimerUI()
		ht = display.holdTimer
		display.holdTimer.startTimer('decreasing', 5, 1/60)
		#Clock.schedule_interval(display.refresh, 1/60)
		return display
		
		
if __name__ == '__main__':
	timerApp().run()
	
