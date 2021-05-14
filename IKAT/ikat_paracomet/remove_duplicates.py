
ikatdata = []
ikatdata_paracomet = []

with open("ikatdata.hypo") as f:
    #Content_list is the list that contains the read lines.     
    for line in f:
        ikatdata.append(line.strip())

with open("ikatdataparacomet.hypo") as f:
    #Content_list is the list that contains the read lines.     
    for line in f:
        ikatdata_paracomet.append(line.strip())

total_len = len(ikatdata)

new_ikatdata = []
new_ikatdata_paracomet = []


for i in range(total_len):
    if (ikatdata[i] != ikatdata_paracomet[i]):
        new_ikatdata.append(ikatdata[i])
        new_ikatdata_paracomet.append(ikatdata_paracomet[i])

print(len(new_ikatdata))
print(len(new_ikatdata_paracomet))

with open('new_ikatdata.hypo', 'w') as f:
    for line in new_ikatdata:
        f.write("%s\n" % line)

with open('new_ikatdataparacomet.hypo', 'w') as f:
    for line in new_ikatdata_paracomet:
        f.write("%s\n" % line)

