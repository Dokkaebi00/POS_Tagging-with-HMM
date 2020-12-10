train_set = 'train_set.txt'
f = open(train_set,'r')
data_raw = f.readlines() 
f.close()

def toDoc(): 
    doc = '' 
    for idx,line in enumerate(data_raw): 
        try: 
            str,label = line.split()
            if (str == '.' and label == '.'): 
                doc += str 
                continue
            # else: 

        except ValueError:
            pass 


    return doc 





