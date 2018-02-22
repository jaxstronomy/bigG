import numpy as np
import matplotlib.pyplot as plt
import math

# w = speed
# i = angle_incidence
# a = appature
d = 3.2 #min_distance_from_silicon
# reflect = percent_of_reflection
# t = transparancy
# absorb = absorbtion #to do math if necessary (r*r+t*t+a*a=1)
# max_d = maximum_distance_for_accurate_reading
# side = math.sqrt(d*d+d*d-2*d*d*cos(2i)) #law of cosines
# time = time_to_bounce_back
# accurate_reading = time_to_take_accurate_reading

rsi = 3.5 #radius
R = 7.8 #radius_of_center
#extra_dist = r-(R+rsi+d)
pipi = math.pi
r_Values = []
theta_Values = np.arange(0.0, 360.0, 1.0)

for degrees in xrange(360):
	radians = (degrees*pipi)/180
	r = R*math.cos(radians)+math.sqrt(math.pow(R, 2)*(1-math.pow(math.cos(radians), 2))+math.pow(rsi, 2)) #total_radius
	r_Values.append(r)
	#print "degrees: %d and r: %f" % (degrees, r) #debug only

max_r = max(r_Values)
min_r = min(r_Values)
min_y = int(min_r) - 1
max_y = int(max_r) + 1

#rCount = len(r_Values) #debug only
#print r_Values #debug only
#print rCount #debug only
plt.axis([0, 360, min_y, max_y])
plt.plot(theta_Values, r_Values, linewidth=2.0)
plt.show()

"""
if side < a :
	if d <= max_d:
		if time <= accurate_reading:
			print("Will Work")
		else:
			print("Won't work - too fast")
	else:
		print("Won't work - distance won't be accurate")
else:
	print("No reading angle too great/no silicon")
"""


