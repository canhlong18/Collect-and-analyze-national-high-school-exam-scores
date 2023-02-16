rawData = "<td>CanhLong7.20</td>"
tags = []

for j in range(len(rawData)):
	if rawData[j] == "<":
		begin = j
	if rawData[j] == ">":
		end = j
		tags.append(rawData[begin:end+1])

for tag in tags:
	rawData = rawData.replace(tag, "")

print(rawData)