import requests
import json
from assignments import Courses

class Grades(object):
	def __init__(self, url, apiKey):
		self.url = url
		self.apiKey = apiKey


	#returns full data set of current classes
	def gradeData(self):
		
		headers = { "Authorization":"Bearer "+self.apiKey}

		r = requests.get(self.url+"courses", headers = headers)