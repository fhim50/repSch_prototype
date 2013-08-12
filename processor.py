from twitter.connector import connect


def get_tweet():
	tweets = connect.search.tweets(q = '#repSHS')


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
	return t.get('search_metadata',None), t.get('statuses',None)
	






