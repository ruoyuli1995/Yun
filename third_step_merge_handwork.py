#coding=utf-8
import codecs
import json

char = {}
with codecs.open("char_dict.json", "r", "utf-8") as finput:
    for line in finput:
        line = json.loads(line)
        char[line[u"韵"]] = line

#UNK
□



for line in codecs.open("to_edit.char", "r", "utf-8"):
    line = line.strip("\n")
    if line[0] in char:
        print("Error_1", line)
    if len(line) == 1:
        temp = char[u"的"]
    elif len(line) >= 2:
        temp = char[line[1]]
    else:
        print("Error_2". line)
    temp[u"韵"] = line[0]
    for c in line[2 : ]:
        for item in char[c]:
            c_item = char[c][item]
            if isinstance(c_item, list):
                temp[item] = list(set(temp[item] + c_item))
    char[line[0]] = temp

for line in codecs.open("to_replace.char", "r", "utf-8"):
    line = line.strip("\n")
    if line[0] in char:
        print("Attention whether right here", line)
    if len(line) == 1:
        temp = char[u"的"]
    elif len(line) == 2:
        temp = char[line[1]]
    else:
        print("Error_3". line)
    temp[u"韵"] = line[0]
    char[line[0]] = temp

for i in char:
    if len(char[i][u"平水平仄"]) == 2:
        typ_a = 2
    elif char[i][u"平水平仄"] == [0]:
        typ_a = 0
    elif char[i][u"平水平仄"] == [1]:
        typ_a = 1
    else:
        print("Error")

    if len(char[i][u"词林平仄"]) == 2:
        typ_b = 2
    elif char[i][u"词林平仄"] == [0]:
        typ_b = 0
    elif char[i][u"词林平仄"] == [1]:
        typ_b = 1
    else:
        print("Error")

    assert(typ_a == typ_b)
    char[i][u"类型"] = typ_a

to_delete = set()
for line in codecs.open("to_delete.char", "r", "utf-8"):
    line = line.strip("\n")
    if line in to_delete or line in char:
        print("Error", line)
    to_delete.add(line)

to_delete |= set(u"、。，！：；？")

to_remain = set([i for i in char])

all_char = set(codecs.open("actual_characters.list", "r", "utf-8").read())

print(to_delete & to_remain)
print(all_char - to_remain - to_delete)

char = sorted(char.items(), key=lambda c: (c[1][u"平水韵部"], c[1][u"韵"]))
with codecs.open("char_dict_v2.json", "w", "utf-8") as fout:
    for i in char:
        fout.write(json.dumps(i[1], ensure_ascii=False) + "\n")
