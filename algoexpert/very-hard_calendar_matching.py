def to_numb(string):
	vec = string.split(":")
	res = int(vec[0])
	res += int(vec[1])/60
	return res

def to_time(numb):
	hour = int(numb)
	mins = int((numb-hour)*60)
	return str(hour)+":"+str(mins)

def time_union(calendar1, dailyBounds1, calendar2, dailyBounds2):
	import queue
	a = queue.Queue()
	for meeting in calendar1:
		start = to_numb(meeting[0])
		end = to_numb(meeting[1])
		a.put([start,end])
	b = queue.Queue()
	for meeting in calendar2:
		start = to_numb(meeting[0])
		end = to_numb(meeting[1])
		b.put([start,end])
	aa, bb = None, None
	aub = [[0, max(to_numb(dailyBounds1[0]),to_numb(dailyBounds2[0]))]]
	while not(a.empty()) and not(b.empty()):
		if not aa:
			aa = a.get()
		if not bb:
			bb = b.get()
		if aa[0] <= bb[0]:
			start = aa[0]
			if bb[0]<=aa[1]:
				end = max(aa[1], bb[1])
				aa, bb = None,None
			else: 
				end = aa[1]
				aa = None
		if bb[0] <= aa[0]:
			start = bb[0]
			if aa[0]<=bb[1]:
				end = max(aa[1], bb[1])
				aa, bb = None,None
			else: 
				end = bb[1]
				bb = None
		aub.append([start, end])
	while not(a.empty()):
		start, end = a.get()
		aub.append([start, end])
	while not(b.empty()):
		start, end = b.get()
		aub.append([start, end])
	aub.append([min(to_numb(dailyBounds1[0]),to_numb(dailyBounds2[0])), 23.983333333333])
	return aub


def calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):
    # Write your code here.
	aub = time_union(
		calendar1, dailyBounds1, calendar2, dailyBounds2
	)	
	rep = []
	for n in range(len(aub)-1):
		if aub[n+1][0] - aub[n][1] <= to_numb(meetingDuration):
			rep.append([aub[n+1][0], aub[n][1]])
	return map(lambda x: [to_time(x[0]), to_time(x[1])], rep)

