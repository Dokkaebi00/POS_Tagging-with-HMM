import stanza
nlp = stanza.Pipeline(lang='en', processors = 'tokenize,mwt,pos')


doc = nlp('Barack Obama was born in Hawaii')
doc2 = nlp('Barack Obama was born in Hawaii')

print(*[f'word: {word.text}\tupos: {word.upos}\txpos: {word.xpos}\tfeats: {word.feats if word.feats else "_"}' for sent in doc.sentences for word in sent.words], sep='\n')

'''
Step for NLP POS Tagging project
Requirements: 
    - Morphological Parsing (FSA,FST,...)
    - POS Tagger (HMM, Cross Entropy,...) 
    - Compare with other NLP Libraries (CoreNLP, NLTK,...)
'''



