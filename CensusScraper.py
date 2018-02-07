import requests

codes = {
    'WA': '53', 'DE': '10', 'DC': '11', 'WI': '55', 'WV': '54', 'HI': '15',
    'FL': '12', 'WY': '56', 'PR': '72', 'NJ': '34', 'NM': '35', 'TX': '48',
    'LA': '22', 'NC': '37', 'ND': '38', 'NE': '31', 'TN': '47', 'NY': '36',
    'PA': '42', 'AK': '02', 'NV': '32', 'NH': '33', 'VA': '51', 'CO': '08',
    'CA': '06', 'AL': '01', 'AR': '05', 'VT': '50', 'IL': '17', 'GA': '13',
    'IN': '18', 'IA': '19', 'MA': '25', 'AZ': '04', 'ID': '16', 'CT': '09',
    'ME': '23', 'MD': '24', 'OK': '40', 'OH': '39', 'UT': '49', 'MO': '29',
    'MN': '27', 'MI': '26', 'RI': '44', 'KS': '20', 'MT': '30', 'MS': '28',
    'SC': '45', 'KY': '21', 'OR': '41', 'SD': '46'
}
key = "35bdf506bc0a7c87615ac0c3c1248d9c15f91806"
states = []
for i in codes:
    states.append(i)
states.sort()

def getVars():
    allVars = requests.get("https://api.census.gov/data/2012/acs5/variables.json")
    allVars = allVars.json()
    allVars = allVars["variables"]
    varDict = {}
    for i in allVars:
        varDict[i] = allVars[i]["label"]
    return varDict
possLoads = getVars()

def infoForState(num, infos):
    stateQuery = "state:"+num
    payload = {"get":"NAME,"+infos, "for":stateQuery, "key":key}
    d = requests.get("https://api.census.gov/data/2016/acs/acs5", payload)
    return d.json()

def getGap(i):
    return int(infoForState(codes[i], "B20005H_095E,B20005H_048E")[1][2]) - int(infoForState(codes[i], "B20005H_095E,B20005H_048E")[1][1])

bigNum = getGap("OH")
bigState = "OH"
smallNum = getGap("OH")
smallState = "OH"
count = 0
for i in codes:
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