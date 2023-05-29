import re

# https://www.nltk.org/howto/portuguese_en.html
import nltk
from nltk.probability import FreqDist
from nltk.corpus import machado


nltk.download('stopwords')  # stop words
nltk.download('machado')  # textos de exemplo


class MachadoAssis():

    def __init__(self) -> None:
        self.stopwords = nltk.corpus.stopwords.words('portuguese')
        self.raw_text = machado.raw('romance/marm05.txt')

    def contaLetras(self):
        """
            conta letras

        """
        fdist = FreqDist(self.raw_text)
        _groups = fdist.keys()
        _frequencies = fdist.values()

        return _groups, _frequencies

    def obtemTokens(self):
        #
        # conta palavras
        #
        token = re.findall('\w+', self.raw_text)

        words = []
        for word in token:
            words.append(word.lower())

        # get the list without stop words
        words_ne = []
        for word in words:
            if word in self.stopwords:
                continue
            if word.isnumeric():
                continue
            if len(word) < 3:
                continue
            words_ne.append(word)

        nlp_words = nltk.FreqDist(words_ne)
        return nlp_words

    def contaPalavras(self, N: int = None):
        nlp_words = self.obtemTokens()

        _groups = list(nlp_words.keys())
        _frequencies = list(nlp_words.values())
        if N is not None:
            _groups = _groups[:N]
            _frequencies = _frequencies[:N]

        return _groups, _frequencies

    def plot(self):
        pass
