from leitorarquivo import LeitorArquivo

import os
import numpy as np
import matplotlib.pyplot as plt


def main():
    leitor = LeitorArquivo('data.txt')
    valores = leitor.getValores()
    os.system("cls")
    print(valores)

    plt.plot(valores)
    plt.show()


main()

