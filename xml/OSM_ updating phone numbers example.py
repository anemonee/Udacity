
import xml.etree.ElementTree as ET
import re

name_file = "blore_select"
tree = ET.parse(name_file)
root = tree.getroot()

itg = 0
ftg = 0
count_phone = 0
count_8 = 0
count_9 = 0
count_7 = 0
wp = []
regex1 = re.compile('(8)|(08)')
regex2 = re.compile('(9)|(09)')
regex3 = re.compile('(7)|(07)|(1800)|(3)|(4)')


for node in root.findall('node'):
    for tag in node.iter('tag'):
        itg = itg +1
        k1 = tag.get("k")
        if k1 == "phone":
            count_phone = count_phone + 1
            v1 = tag.get("v")
            v1 = v1.replace(" ","")
            v1 = v1.replace("  ","")
            v1 = v1.replace("-","")
            v1 = v1.replace('+',"")
            v1 = v1.replace("(91)", "91")
            v1 = v1.replace("0091", "91")
            v1 = v1.replace("O", "0")
            v1 = v1.replace('"', "")
            v1 = v1.replace('01800', "1800")
            v1 = v1.replace('0099', "99")
            v1 = v1.replace('9180', "80")
            v1 = v1.replace('91080', "80")
            m1 = regex1.match(v1)
            m2 = regex2.match(v1)
            m3 = regex3.match(v1)
            if m1:
                count_8 = count_8 + 1
                if len(v1) <= 9:
                    print v1
                elif len(v1) >= 12:
                    if v1.find(',') == -1:
                        v1 = v1[:11]+", "+v1[11:]
                        if len(v1) < 20:
                            print v1
            elif m2:
                count_9 = count_9 + 1
                if v1[:2] == "91" and len(v1) <> 12:
                    if len(v1) <> 25 or len(v1) <> 38 or len(v1) <> 51:
                       node.remove(tag)
            elif m3:
                count_7 = count_7 + 1
                if len(v1) == 8:
                    v1 = '80'+ v1
            else:
                print v1

print count_phone
print count_8
print count_9
print count_7
