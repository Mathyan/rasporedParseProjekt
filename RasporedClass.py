
class RasporedClass:
    prezime_ime = ""
    dani = ["Ponedjeljak:", "Utorak:", "Srijeda:", "Cetvrtak:", "Petak:", "Subota:", "Nedjelja:"]
    sati_po_danima = {}

    for item in dani:
        key = item[:-1]  # Remove the colon at the end of each item
        sati_po_danima[key] = ""

    def __init__(self, prezime_ime, lista_sati):
        self.prezime_ime = prezime_ime