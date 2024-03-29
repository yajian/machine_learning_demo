# coding=utf-8
import codecs
import regex
from collections import Counter
import os


def make_vocab(fpath, fname):
    with codecs.open(fpath, 'r', 'utf-8') as file:
        text = file.read()
        text = regex.sub('[^\s\p{Latin}]', '', text)
        words = text.split()
        word2cnt = Counter(words)
        if not os.path.exists('preprocessed'):
            os.makedirs('./preprocessed')
        with codecs.open('preprocessed/{}'.format(fname), 'w', 'utf-8') as fout:
            fout.writelines("{}\t1000000000\n".format("<PAD>"))
            fout.writelines("{}\t1000000000\n".format("<UNK>"))
            fout.writelines("{}\t1000000000\n".format("<S>"))
            fout.writelines("{}\t1000000000\n".format("</S>"))
            for word, cnt in word2cnt.most_common(len(word2cnt)):
                fout.writelines('{}\t{}\n'.format(word, cnt))


if __name__ == '__main__':
    make_vocab('./de-en/train.tags.de-en.de', 'de.vocab.tsv')
    make_vocab('./de-en/train.tags.de-en.en', 'en.vocab.tsv')
    print 'Done'
