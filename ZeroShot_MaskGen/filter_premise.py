prems = []
counter = 0
with open('jandata.hypo') as f:
    for line in f.readlines():
        counter += 1

        and_since = False
        
        sents = line.split(".")
        for sent in sents:
            if "And since" in sent:
                and_since = True
                prems.append(sent)
                
        if and_since == False:
            prems.append("And since empty")
            


with open('jandata_premises.hypo', 'w') as f:
    for prem in prems:
        f.write("%s\n" % prem)