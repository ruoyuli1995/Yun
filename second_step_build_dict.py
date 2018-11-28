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
			if pingze not in temp[u"平仄"]:
				temp[u"平仄"].append(pingze)
			if psqr not in temp[u"平上去入"]:
				temp[u"平上去入"].append(psqr)
			char[i] = temp
		else:
			temp = {}
			temp[u"平水韵部"] = [idx]
			temp[u"词林韵部"] = []
			temp[u"平仄入"] = []
			temp[u"平仄"] = [pingze]
			temp[u"平上去入"] = [psqr]
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
			if pingze not in temp[u"平仄"]:
				print("Error1", i), i
			if pzr not in temp[u"平仄入"]:
				temp[u"平仄入"].append(pzr)
			char[i] = temp
		else:
			print("Error2", i)
