import requests

exec(open("./census.py").read())
cen = Census()
possLoads = cen.getVars(5)

def getGap(i):
	return int(cen.infoForState(cen.codes[i], "B20005H_095E,B20005H_048E", 5)[1][2]) - int(cen.infoForState(cen.codes[i], "B20005H_095E,B20005H_048E", 5)[1][1])

bigNum = getGap("OH")
bigState = "OH"
smallNum = getGap("OH")
smallState = "OH"
count = 0
for i in cen.codes:
	count+=1
	if(getGap(i) > bigNum):
		bigNum = getGap(i)
		bigState = i
	if(getGap(i) < smallNum):
		smallNum = getGap(i)
		smallState = i
	print(str(int((count/55)*100))+"%")
print([bigState,bigNum])
print([smallState,smallNum])
