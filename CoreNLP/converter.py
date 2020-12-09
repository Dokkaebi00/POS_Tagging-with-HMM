'''
Below is the example of CoNLL-U format 
# sent_id = 1
# text = They buy and sell books.
1   They     they    PRON    PRP    Case=Nom|Number=Plur               2   nsubj   2:nsubj|4:nsubj   _
2   buy      buy     VERB    VBP    Number=Plur|Person=3|Tense=Pres    0   root    0:root            _
3   and      and     CONJ    CC     _                                  4   cc      4:cc              _
4   sell     sell    VERB    VBP    Number=Plur|Person=3|Tense=Pres    2   conj    0:root|2:conj     _
5   books    book    NOUN    NNS    Number=Plur                        2   obj     2:obj|4:obj       SpaceAfter=No
6   .        .       PUNCT   .      _                                  2   punct   2:punct           _

# sent_id = 2
# text = I have no clue.
1   I       I       PRON    PRP   Case=Nom|Number=Sing|Person=1     2   nsubj   _   _
2   have    have    VERB    VBP   Number=Sing|Person=1|Tense=Pres   0   root    _   _
3   no      no      DET     DT    PronType=Neg                      4   det     _   _
4   clue    clue    NOUN    NN    Number=Sing                       2   obj     _   SpaceAfter=No
5   .       .       PUNCT   .     _                                 2   punct   _   _

'''
import os
# import regex
# from collections import defaultdict
# import stanza
# import conllu

class WordCoNLL: 
    def __init__(self,
        id, 
        word,
        label): 
        self.ID = id
        self.FORM = word 
        self.LEMMA = '_' # Stemming word (original word) 
        self.UPOS = '_' # Also XPOS label  
        self.XPOS = label  
        self.FEATS = '_' 
        self.HEAD = '_' 
        self.DEPREL = '_' 
        self.DEPS = '_' 
        self.MISC = '_' 

    def __str__(self): 
        # Return should be order below
        return ('{}\t'*10).format(self.ID, self.FORM, self.LEMMA,\
                self.UPOS, self.XPOS, self.FEATS, self.HEAD, self.DEPREL,\
                self.DEPS, self.MISC)


def Converter(data_raw): 
    #TODO: re-label ID, for every new sentence, ID = 0
    # This is temporary fix, not sure if correct
    listSentence = []
    id = 0 
    for idx,line in enumerate(data_raw): 
        try: 
            str,label = line.split()
            # TODO: '.' should be label as PUNCT 
            if (str == '.' and label == '.'): 
                id = 0 
                continue
            else: 
                id += 1

            temp = WordCoNLL(id=id, 
                            word=str, 
                            label=label)
            listSentence.append(temp) 
            # Debug purpose
            # if idx <= 100:
            #     print(vars(temp))
        except ValueError:
            id == 0
            pass 

    return listSentence


# Convert train_set.pos & test_set.pos -> CoNLLU format 
f =  open("./train_set.txt","r") 
data_raw = f.readlines()
f.close()
listSentence = Converter(data_raw)

# Convert WordCoNLL (Python object) to dict  




# Import converted dict to test POS Tagging in Stanza 






# for idx in range(100): 
#     print(listSentence[idx])

# myDict = {} 
# listSentence = []

# for idx,line in enumerate(data_raw): 
#     try:
#         str,label = line.split()
#         a = WordCoNLL(id=idx,word=str,label=label)
#         listSentence.append(a)
#         # myDict[idx]=a 
#         # myDict[str] = label
#     except ValueError:
#         continue
#         # pass

# # for idx,val in enumerate(myDict): 
# #     if idx == 5: 
# #         break 
# #     print(idx, val)


# for i in range(5): 
#     print(listSentence[i])

# Train POS Tagging 

# Eval POS on test_set.pos 

