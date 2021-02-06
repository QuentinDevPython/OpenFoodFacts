import sys
import os
import dotenv
import peewee 
import requests
import tables

class AllData:

	dotenv.load_dotenv()
	self.data = list()
	index = 1

	self.request_url = "https://fr.openfoodfacts.org/cgi/search.pl"
	max_pages = int(os.getenv("P_MAX_PAGES"))

	try :
		for index in range(max_pages):
			self.request_params = {
				"action" : "process",
				"sort_by" : "unique_sacans_n",
				"page_size" : os.gentenv("P_PAGE_SIZE"),
				"page" : index+1,
				"json" : 1
			}
			response = r.get(self.request_url, self.request_params)
			if response.status_code == 200:
				self.data.extend(response.json()['products'])
				print("Dowloading: {0}%".format(index*(100//max_pages)))
				sys.stdout.write("\033[F")

	except r.ConnectionError:
		print("Unable to connect to {0}".format(url))