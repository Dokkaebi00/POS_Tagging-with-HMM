f = open(r"./train_set.txt",'r')
data_raw = f.readlines()
f.close()

# listSentence = []
doc = ''
for idx,line in enumerate(data_raw): 
    if idx == 1000: 
        break
    try: 
        str,val = line.split()
        doc = doc + ' ' + str
        # listSentence.append(str)
    except ValueError: 
        pass 

# print(listSentence)
print(doc)
