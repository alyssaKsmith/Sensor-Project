# Learning Processing
# Daniel Shiffman

# Example 10-5: Object-oriented timer

class Timer:

  savedTime = 0 # When Timer started
  totalTime = 0 # How long Timer should last

  def __init__(self, tempTotalTime):
    self.totalTime = tempTotalTime


  # Starting the timer
  def start(self):
    # When the timer starts it stores the current time in milliseconds.
    self.savedTime = millis()


  # The function isFinished() returns true if 5,000 ms have passed. 
  # The work of the timer is farmed out to this method.
  def isFinished(self): 
    # Check how much time has passed
    passedTime = millis()- self.savedTime
    if (passedTime > self.totalTime):
      return True
    else:
      return False
