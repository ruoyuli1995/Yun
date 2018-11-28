#coding=utf-8
import codecs
import json

char = {}
for idx, line in enumerate(codecs.open("pingshuiyun.list", "r", "utf-8")):
	if idx < 30:
		pingze = 0
		psqr = 0
	else:
		pingze = 1
		if idx < 59:
			psqr = 1
		elif idx < 89:
			psqr = 2
		else:
			psqr = 3
	for i in line.strip():
		if i in char:
			temp = char[i]
			if idx not in temp[u"平水韵部"]:
				temp[u"平水韵部"].append(idx)
			if pingze not in temp[u"平水平仄"]:
				temp[u"平水平仄"].append(pingze)
			if psqr not in temp[u"平上去入"]:
				temp[u"平上去入"].append(psqr)
			char[i] = temp
		else:
			temp = {}
			temp[u"平水韵部"] = [idx]
			temp[u"平水平仄"] = [pingze]
			temp[u"平上去入"] = [psqr]
			temp[u"词林韵部"] = []
			temp[u"词林平仄"] = [pingze]
			temp[u"平仄入"] = []
			char[i] = temp

for idx, line in enumerate(codecs.open("cilinzhengyun.list", "r", "utf-8")):
	if idx < 14:
		pingze = 0
		pzr = 0
	else:
		pingze = 1
		if idx < 28:
			pzr = 1
		else:
			pzr = 2
	for i in line.strip():
		if i in char:
			temp = char[i]
			if idx not in temp[u"词林韵部"]:
				temp[u"词林韵部"].append(idx)
			if pingze not in temp[u"词林平仄"]:
				temp[u"词林平仄"].append(pingze)
			if pzr not in temp[u"平仄入"]:
				temp[u"平仄入"].append(pzr)
			char[i] = temp
		else:
			print("Error", i)

for i in char:
	if len(i[u"平水平仄"]) == 2:
		typ_a = 2
	elif i[u"平水平仄"] == [0]:
		typ_a = 0
	elif i[u"平水平仄"] == [1]:
		typ_a = 1
	else:
		print("Error")

	if len(i[u"词林平仄"]) == 2:
		typ_b = 2
	elif i[u"词林平仄"] == [0]:
		typ_b = 0
	elif i[u"词林平仄"] == [1]:
		typ_b = 1
	else:
		print("Error")

	assert(typ_a == typ_b)
	char[i][u"类型"] = typ_a

char = sorted(char.items(), key=lambda c: c[u"平水韵部"])
with codecs.open("char_dict.json", "w", "utf-8") as fout:
	for i in char:
		fout.write(json.dumps(char[i], ensure_ascii=False) + "\n")
