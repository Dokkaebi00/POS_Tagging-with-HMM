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
# import os
# import stanza
# import conllu
# import attr

class WordCoNLL: 
    def __init__(self,
        id, 
        word,
        label,
        lemma='_'): 
        self.ID = id 
        self.FORM = word 
        self.LEMMA = lemma # TODO: Stemming word (original word) 
        self.UPOS = '_' # Also XPOS label  
        self.XPOS = label  
        self.FEATS = '_' 
        self.HEAD = '_' 
        self.DEPREL = '_' 
        self.DEPS = '_' 
        self.MISC = '_' 

    def __str__(self): 
        '''
            Just return as string presentation with format like CoNLL-U 
            so you must convert object to dict to use in Stanza
        '''
        # Return should be order below
        return ('{}\t'*10).format(self.ID, self.FORM, self.LEMMA,\
                self.UPOS, self.XPOS, self.FEATS, self.HEAD, self.DEPREL,\
                self.DEPS, self.MISC)

    def asdict(self): 
        return {'id': int(self.ID), # ERROR 
                'form': self.FORM,  
                'lemma': self.LEMMA, 
                'upos': self.UPOS,         
                'xpos': self.XPOS,         
                'feats': self.FEATS,         
                'misc': self.MISC,         
        }

def Converter(data_raw): 
    # This is temporary fix, not sure if correct
    listSentence = []
    id = 0 
    for idx,line in enumerate(data_raw): 
        try: 
            str,label = line.split()
            if (str == '.' and label == '.'): 
                # How I label '.' with PUNCT is not a very good example 
                id += 1
                temp = WordCoNLL(id=id, 
                        word=str, # receive '.' 
                        lemma=str, # receive '.'  
                        label='PUNCT')
                listSentence.append(temp.asdict()) 
                # listSentence.append(temp) 
                id = 0 
                continue
            else: 
                id += 1
            temp = WordCoNLL(id=id, 
                            word=str, 
                            label=label)
            listSentence.append(temp.asdict()) 

            ############################
            # # Debug purpose
            # if idx <= 100:
            #     print(vars(temp))

        except ValueError:
            id == 0
            pass 

    return listSentence


# def exportCoNLLU(filepath, data): 
#     ''' 
#         filepath: a
#         data: a
#     '''
#     try: 
#         f = open(filepath,'w+') # write, both read and write  
#         #  Initial stage to get program running purpose


#         f.close()
#     except FileExistsError: 
#         print('File {} not found!'.format(filepath))

# Convert train_set.pos & test_set.pos -> CoNLLU format 
f =  open("./train_set.txt","r") 
data_raw = f.readlines()
f.close()
# listSentence = Converter(data_raw)

# for idx in range(100): 
#     print(listSentence[idx])


from stanza.utils.conll import CoNLL
dicts = [Converter(data_raw)] 
conll = CoNLL.convert_dict(dicts) # conll is List[List[List]], representing each token / word in each sentence in the document

# print(len(conll[0]))


