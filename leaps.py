import json
import datetime
import dateparser

# Read a Json from the qlscraper, and write it in a more convenient csv form

with open("leaps.json") as fin:
    dat = json.load(fin)

for ep in dat:
    p = dateparser.parse(ep['date'].pop())
    if p is None: # Weird edge case
        p = dateparser.parse("Nov 21, 1963")
    ep['date'] = p

# Sam starts his leaping on 26/2/1995
bootstrap = {'date': datetime.datetime(1995, 2, 26, 0, 0), 'episode':0}
dat.append(bootstrap)
with open("leaps.csv", "w") as fout:
	fout.write("year, month, day, episode\n")
	for ep in dat:
		date = ep['date']
		fout.write("%d, %d, %d, %d\n" % (date.year, date.month, date.day, ep['episode']))

byep = sorted(dat, key=lambda ep: ep['episode'])

dates = [ep['date'] for ep in dat]
dates = sorted(list(set([datetime.date(date.year, date.month, 1) for date in dates])))

# When in doubt, graphviz
graphviz = "digraph G {\n"
new_year = True
for i, date in enumerate(dates):
	#New subgraph for each year
	nodeA = "l_%d_%d" % (date.year, date.month)
	if new_year:
		graphviz += "subgraph cluster_%d {\n" % date.year
		graphviz += "label =\"%d\";\nrankdir=LR;\n" % date.year 
		graphviz += "node [shape=Rect];\nedge [style=invis];\n"
	graphviz += nodeA + "[label=\"%s\"]" % datetime.date(1900, date.month, 1).strftime("%b") + ";\n"
	try:
		new_year = date.year != dates[i+1].year
		nodeB = "l_%d_%d" % (dates[i+1].year, dates[i+1].month)
		# Link months within a year
		if not new_year:
			graphviz += "%s -> %s;\n" % (nodeA, nodeB)
		else:
			graphviz += "}\n"
	except:
		pass
graphviz += "}\n"

years = sorted(list(set([date.year for date in dates])))
for i, year in enumerate(years):
	try:
		graphviz += "cluster_%d -> cluster_%d;\n" % (year, years[i+1])
	except:
		pass

for i, ep in enumerate(byep):
	try:
		nodeA = "l_%d_%d" % (ep['date'].year, ep['date'].month)
		nodeB = "l_%d_%d" % (byep[i+1]['date'].year, byep[i+1]['date'].month)
		graphviz += "%s -> %s;\n" % (nodeA, nodeB)
	except:
		pass

graphviz += "}"
with open("leaps.dot", "w") as fout:
	fout.write(graphviz)



