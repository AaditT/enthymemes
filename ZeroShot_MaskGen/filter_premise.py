prems = []
counter = 0
with open('jandata.hypo') as f:
    for line in f:
        counter += 1
        if "And since" not in line:
            prems.append(line)
            continue
        
        sents = line.split(".")
        for sent in sents:
            if "And since" in sent:
                prems.append(sent)


with open('jandata_premises.hypo', 'w') as f:
    for prem in prems:
        f.write("%s\n" % prem)