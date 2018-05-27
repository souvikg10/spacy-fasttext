from __future__ import unicode_literals
import plac
import numpy
import random
import spacy
from spacy.language import Language

TAG_MAP = {
    'N': {'pos': 'NOUN'},
    'V': {'pos': 'VERB'},
    'J': {'pos': 'ADJ'}
}

TRAIN_DATA = [
    ("Ik zie mooie dingen", {'tags': ['N', 'V', 'J', 'N']}),
    ("Hij maakt goede muziek", {'tags': ['N','V', 'J', 'N']})
]

def main():
    nlp = spacy.load('nl_model-0.0.0')
    tagger = nlp.create_pipe('tagger')
    # Add the tags. This needs to be done before you start training.
    for tag, values in TAG_MAP.items():
        tagger.add_label(tag, values)
    nlp.add_pipe(tagger)
    optimizer = nlp.begin_training()
    for i in range(20):
        random.shuffle(TRAIN_DATA)
        losses = {}
        for text, annotations in TRAIN_DATA:
            nlp.update([text], [annotations], sgd=optimizer, losses=losses)
        print(losses)

    # test the trained model
    test_text = "ik wil mooie vrouwen"
    doc = nlp(test_text)
    print('Tags', [(t.text, t.tag_, t.pos_) for t in doc])

    nlp.to_disk('nl_model_tagger')
    print("Saved model to", 'nl_model_tagger')

if __name__ == '__main__':
    main()