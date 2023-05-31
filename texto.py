import re

# https://www.nltk.org/howto/portuguese_en.html
import nltk
from nltk.probability import FreqDist
from nltk.corpus import machado


# carrega as stop words
nltk.download('stopwords')

# textos de exemplo de Machado de Assis
# usa PortugueseCategorizedPlaintextCorpusReader() de nltk
# lista de textos em https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/index.xml
# veja comentario em default_download_dir() para localizar o diretório onde os dados são copiados
# em nosso caso: ~/nltk_data/corpora/
nltk.download('machado')


class MachadoAssis():

    def __init__(self) -> None:
        self.stopwords = nltk.corpus.stopwords.words('portuguese')
        self.raw_text = machado.raw('romance/marm05.txt')

    def contaLetras(self):
        """
            conta letras - distribuição de frequencias
        """
        fdist = FreqDist(self.raw_text)  # https://www.nltk.org/api/nltk.probability.FreqDist.html
        _groups = fdist.keys()
        _frequencies = fdist.values()

        return _groups, _frequencies

    def obtemTokens(self):
        """
            obtem as palavras no texto
        """
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
        """
            conta palavras - distribuição de frequencias
        """
        nlp_words = self.obtemTokens()

        _groups = list(nlp_words.keys())
        _frequencies = list(nlp_words.values())
        if N is not None:
            _groups = _groups[:N]
            _frequencies = _frequencies[:N]

        return _groups, _frequencies
