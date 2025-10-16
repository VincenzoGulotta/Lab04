from passeggero import Passeggero
from cabina import *
from csv import reader

class Crociera:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self._nome = nome
        self._lista_cabine = []
        self._lista_passeggeri = []

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def __str__(self):
        return f"Nome Crociera: {self._nome}"

    def carica_file_dati(self, file_path):
        """Carica i dati (cabine e passeggeri) dal file"""
        file = open(file_path, "r")
        lettura = reader(file)
        for item in lettura:                            # Leggo una riga come lista
            if len(item) <= 4:                          # Smisto in base alla lunghezza della lista, in questo caso cabina standard o passeggero
                if len(item[0]) == 4:                   # Cabina
                    cabina = Cabina(item[0], item[1], item[2], item[3])
                    self._lista_cabine.append(cabina)
                if len(item[0]) == 2:                   # Passeggero
                    passeggero = Passeggero(item[0], item[1], item[2])
                    self._lista_passeggeri.append(passeggero)
            else:                                       # Sono tra le cabine speciali
                if item[-1].isdigit():           # Se l'ultimo elemento è un numero -> Cabina Animali
                    cabina = Animali(item[0], item[1], item[2], item[3], item[4])
                    self._lista_cabine.append(cabina)
                else:                                   # Altrimenti -> Cabina Deluxe

                    cabina = Deluxe(item[0], item[1], item[2], item[3], item[4])
                    self._lista_cabine.append(cabina)

        for item in self._lista_cabine:
            print(item)
        file.close()


    def assegna_passeggero_a_cabina(self, cod_cabina, cod_passeggero):
        """Associa una cabina a un passeggero"""
        passeggero = None                               # Ricevo come input il codice del passeggero e della cabina quindi non posso fare un confronto
        cabina = None                                   # tra oggetti utilizzando __eq__()

        for item in self._lista_passeggeri:             # Itero nella lista passeggeri
            if item.cod_passeggero == cod_passeggero:   # Verifico che il codice inserito esista
                if item.cabina is None:                 # Verifico che il passeggero non abbia già una cabina
                    passeggero = item                   # Salvo temporaneamente l'oggetto passeggero
                else:
                    raise Exception("Il Passeggero possiede già una cabina")

        for item in self._lista_cabine:                 # Itero nella lista cabine
            if item.cod_cabina == cod_cabina:           # Verifico che il codice inserito esista
                if item.passeggero is None:             # Verifico che alla cabina non sia stato già assegnato un passeggero
                    cabina = item                       # Salvo temporaneamente l'oggetto cabina
                else:
                    raise Exception("Alla cabina è stato già assegnato un passeggero")

        # Se sono qui vuol dire che cabina e passeggero sono liberi
        passeggero.assegna_cabina(cabina)       # Assegno la cabina al passeggero
        cabina.assegna_passeggero(passeggero)   # Assegno il passeggero alla cabina

    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        self._lista_cabine.sort(key=lambda cabina: cabina._prezzo)
        return self._lista_cabine

    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        for item in self._lista_passeggeri:
            if item.cabina is not None:
                print(f"Passeggero: {item._nome} {item._cognome}, cabina: {item.cabina._cod_cabina}")
            else:
                print(f"Passeggero: {item._nome} {item._cognome}, nassuna cabina assegnata")
