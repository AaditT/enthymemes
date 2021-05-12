import csv
import os

super_sources = []
super_targets = []
for filename in os.listdir("corpus/"):
    
    tsv_file = open("corpus/"+filename)
    read_tsv = csv.reader(tsv_file, delimiter="\t")

    counter = 0

    sources = []
    targets = []
    arg_prems = []
    for row in read_tsv:
        missing_info_2 = row[9]
        if missing_info_2 == '':
            # print(row)
            if ":" in row[0]:
                arg_prems.append(row[0].split(":")[1].strip())
                #print(row[0].split(":")[1].strip())
            
            elif "-" in row[0]:
                prem1 = row[0].split("-")[0]
                prem2 = row[0].split("-")[1]
                prem1_num = int(prem1.split("e")[1])
                prem2_num = int(prem2.split("e")[1])
                prem1_str = arg_prems[prem1_num - 1]
                prem2_str = arg_prems[prem2_num - 1]
                implicit_prem = row[6]
                if (implicit_prem != ""):
                    adjacency = row[1]
                    # if (adjacency == "adjacent"):
                    sources.append(prem1_str + " # " + prem2_str)
                    targets.append(prem1_str + " And since " + implicit_prem + " " + prem2_str)
    for source in sources:
        super_sources.append(source)
    for target in targets:
        super_targets.append(target)

print("SOURCES: " + str(len(super_sources)) + " | TARGETS: " + str(len(super_targets)))
with open('ikat.source', 'w') as f:
    for source in super_sources:
        f.write('%s\n' % source)
with open('ikat.target', 'w') as f:
    for target in super_targets:
        f.write('%s\n' % target)
