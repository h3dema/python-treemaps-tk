import matplotlib.pyplot as plt
import squarify
import seaborn as sns

from texto import MachadoAssis


# define o tamanho da figura gerada pelas funções plot...() deste modulo
FIG_SIZE = (16, 9)


def set_figsize(size: tuple):
    """ altera o tamanho da figura default
    """
    assert len(size) == 2
    global FIG_SIZE
    FIG_SIZE = size


def plot_treemap_letters(texto):
    #
    # plot it
    # - https://github.com/laserson/squarify
    group, frequencies = texto.contaLetras()
    fig, ax = plt.subplots(figsize=FIG_SIZE)
    squarify.plot(sizes=frequencies, label=group, alpha=.8, ax=ax)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    return fig


def plot_frequency(texto, N):
    #
    # frequencia das palavras
    #
    sns.set_style('darkgrid')
    fig, ax = plt.subplots(figsize=FIG_SIZE)
    plt.title(f"Frequencia das {N} top palavras no texto")
    nlp_words = texto.obtemTokens()
    nlp_words.plot(N, figure=fig)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    return fig


def plot_treemap_words(texto, N):
    group, frequencies = texto.contaPalavras(N)
    fig, ax = plt.subplots(figsize=FIG_SIZE)
    squarify.plot(sizes=frequencies, label=group, alpha=.8, ax=ax)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    return fig


if __name__ == "__main__":
    """ le os dados de um texto de Machado de Assis
        e plota treemaps e frequencias
    """
    texto = MachadoAssis()
    N = 20

    fig = plot_treemap_letters(texto)
    plt.show()
    plt.close(fig)

    fig = plot_frequency(texto, N)
    plt.show()
    plt.close(fig)

    fig = plot_treemap_words(texto, N)
    plt.show()
    plt.close(fig)
