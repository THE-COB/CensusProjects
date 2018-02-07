class Census:
	def __init__(self):
		self.codes = {
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
		self.key = "35bdf506bc0a7c87615ac0c3c1248d9c15f91806"
		self.states = []
		for i in self.codes:
			self.states.append(i)
		self.states.sort()

	def __getStr(self, acsNum):
		url = "https://api.census.gov/data"
		if(acsNum is 5):
			url+="/2015/acs5"
		else:
			url+="/2016/acs1"
		return url
	def getVars(self, acsNum):
		allVars = requests.get(self.__getStr(5)+"/variables.json")
		allVars = allVars.json()
		allVars = allVars["variables"]
		varDict = {}
		for i in allVars:
			varDict[i] = allVars[i]["label"]
		return varDict

	def infoForState(self, num, infos, acsNum):
		stateQuery = "state:"+num
		payload = {"get":"NAME,"+infos, "for":stateQuery, "key":cen.key}
		d = requests.get(self.__getStr(acsNum), payload)
		return d.json()