
class Raspored:
    __prezime_ime = ""
    __dani = ["Ponedjeljak:", "Utorak:", "Srijeda:", "Cetvrtak:", "Petak:", "Subota:", "Nedjelja:"]
    __sati_po_danima = {}

    for item in __dani:
        key = item[:-1]  # Remove the colon at the end of each item
        __sati_po_danima[key] = ""

    def __init__(self, prezime_ime, lista_sati: list):
        self.__prezime_ime = prezime_ime
        for i in range(len(lista_sati)):
            self.__sati_po_danima[self.__dani[i]] = lista_sati[i]

    def get_prezime_ime(self):
        return self.__prezime_ime

    def get_raspored(self):
        return self.__sati_po_danima
