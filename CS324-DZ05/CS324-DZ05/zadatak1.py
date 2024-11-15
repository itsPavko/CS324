class Dokument:
    def __init__(self, ime, broj_reci):
        self.ime = ime
        self.broj_reci = broj_reci

class Knjiga(Dokument):
    def __init__(self, ime, broj_reci, autor, zanr, godina_izdavanja):
        super().__init__(ime, broj_reci)
        self.autor = autor
        self.zanr = zanr
        self.godina_izdavanja = godina_izdavanja


knjiga1 = Knjiga("Na Drini cuprija", 1200, "Ivo Andric", "Drama", 1945)
knjiga2 = Knjiga("Roman o Londonu", 1700, "Miloš Crnjanski", "Drama", 1946)
knjiga3 = Knjiga("Fama o biciklistima", 1150, "Svetislav Basara ", "Drama", 1977)


imenik_knjiga = {
    f"lib{i + 1:03d}": knjiga
    for i, knjiga in enumerate([knjiga1, knjiga2, knjiga3], start=1)
}

# Štampanje knjiga
for broj_knjige, knjiga in imenik_knjiga.items():
    print(f"<{broj_knjige}: {knjiga.zanr}, {knjiga.autor}, {knjiga.ime}>")