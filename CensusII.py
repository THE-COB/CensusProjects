import requests
import re

exec(open("./census.py").read())
cen = Census()
possLoads = cen.getVars(1)

exclude = "Margin"
options = []
for i in possLoads:
	if(re.search(exclude, possLoads[i]) is None):
		options.append(i)

for i in options:
	if(re.search("language", possLoads[i]) is not None):
		print(possLoads[i])
# payload = {"get":"NAME,B01001_001E", "for":"state:*", "key": key}
# r = requests.get("api.census.gov/data/2016/acs/acs1", payload)
# print(r.json())