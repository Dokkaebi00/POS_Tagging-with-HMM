import stanza
from spacy import StanzaLanguage

snlp = stanza.Pipeline(lang="en")
nlp = StanzaLanguage(snlp)

doc = nlp("Barack Obama was born in Hawaii. He was elected president in 2008.")
for token in doc:
    print(token.text, token.lemma_, token.pos_, token.dep_, token.ent_type_)
print(doc.ents)