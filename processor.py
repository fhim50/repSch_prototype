from twitter.connector import connect

def get_tweet():
	tweets = connect.search.tweets(q = '#repSHS')

def scrap_data():
	pass

def is_new(sch, data):
	return sch in data

def new_entry(sch, data):
	return data[sch] = 1

def plus_one(sch, data):
	try:
		vote = data.get(sch, None) + 1
	except:
		return

def scraper(obj):
	t = get_tweet()
	metadata = t.get('search_metadata',None)
	data = t.get('statuses',None)
	return metadata, data
	






