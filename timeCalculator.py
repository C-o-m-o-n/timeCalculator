class Time():

	def __init__(self, hours, mins):
		self.hours = hours
		self.mins = mins

	def addTime(time1, time2):
		time3 = Time(0,0)

		if time1.mins+time2.mins > 60:
			time3.hours = (time1.mins+time2.mins)/60
			time3.hours = time3.hours+time1.hours+time2.hours
			time3.mins = (time1.mins+time2.mins)-(((time1.mins+time2.mins)/60)*60)
			return time3

	def displayTime(self):
		print ("new time is ",self.hours," hours and ",self.mins," minutes.")

	def displayMinute(self):
		print ((self.hours*60)+self.mins, " minutes")



one = input("hours: ")
two = input("minutes: ")
print("  ")

three = input("second hours: ")
four = input("second mininutes: ")

a = Time(int(one), int(two))
b = Time(int(three), int(four))
c = Time.addTime(a,b)
c.displayTime()
c.displayMinute()
