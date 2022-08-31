class Covid():
    def posicao(self):
        print ('-------')
    def nome(self):
        print ('-------')
    def casos(self):
        print ('-------')
    def mortes(self):
        print ('-------')

class Brasil(Covid):
    def posicao(self):
        print('3º lugar')
    def nome(self):
        print('-> Brasil - América do Sul')
    def casos(self):
        print('29.000.000 casos por covid-19')
    def mortes(self):
        print('658.000 mortes confirmadas por Covid-19')

class main():
    bra = Brasil()
    print('Brasil: ')
    bra.posicao()
    bra.nome()
    bra.casos()
    bra.mortes()

if __name__ == "__main__": main()
