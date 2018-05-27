#!/usr/bin/env python
# coding: utf8
"""Load vectors for a language trained using fastText
https://github.com/facebookresearch/fastText/blob/master/pretrained-vectors.md
Compatible with: spaCy v2.0.0+
"""
from __future__ import unicode_literals
import plac
import numpy

import spacy
import random
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


def main(vectors_loc=None, lang=None):
    
    if lang is None:
        nlp = spacy.blank('nl')
    else:
        # create empty language class – this is required if you're planning to
        # save the model to disk and load it back later (models always need a
        # "lang" setting). Use 'xx' for blank multi-language class.
        nlp = spacy.blank('nl')
    with open('vector/wiki.nl.vec', 'rb') as file_:
        header = file_.readline()
        nr_row, nr_dim = header.split()
        nlp.vocab.reset_vectors(width=int(nr_dim))
        for line in file_:
            line = line.rstrip().decode('utf8')
            pieces = line.rsplit(' ', int(nr_dim))
            word = pieces[0]
            vector = numpy.asarray([float(v) for v in pieces[1:]], dtype='f')
            nlp.vocab.set_vector(word, vector)  # add the vectors to the vocab
    
    
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

    print("Saved model to", 'nl_model_tagger')

    nlp.to_disk('/app/model')

if __name__ == '__main__':
    
    main()