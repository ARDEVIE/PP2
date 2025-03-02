items = ["I", "love", "programming", "principles", "2"]
file = open('sample.txt','w')
for item in items:
	file.write(item + "\n")
file.close()