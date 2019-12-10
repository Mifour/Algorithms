def angle_minutes(minutes):
	return (minutes%60) *360

def angle_hour(hour, minutes):
	return (hour%12)*360 + (minutes%60) * 360/12

def angle_on_a_clock(string):
	tmp = string.split(':')
	hour = tmp[0]
	minutes = tmp[-1]

	hour = angle_hour(hour, minutes)
	minutes = angle_minutes(minutes)

	return max(hour, minutes) - min(hour, minutes)