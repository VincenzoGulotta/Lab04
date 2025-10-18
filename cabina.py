class Cabina:
    def __init__(self, cod_cabina, num_letti, ponte, prezzo):
        self._cod_cabina = cod_cabina
        self._num_letti = num_letti
        self._ponte = ponte
        self._prezzo = int(prezzo)
        self.passeggero = None
        self.disponibilita = "Disponibile"
        if self.passeggero is not None:                 # Verifico che alla cabina non sia stato già assegnato un passeggero
            self.disponibilita = "Non disponibile"

    def __eq__(self, other):
        if isinstance(other, Cabina):
            return self._cod_cabina == other._cod_cabina
        return False

    def assegna_passeggero(self, passeggero):
        self.passeggero = passeggero

    def main_print(self):                      # Ritorna i dati presenti in tutte le cabine per facilitare la stampa
        return (f"{self._num_letti} letti - "
                f"Ponte {self._ponte} - "
                f"Prezzo {self._prezzo}$ - "
                f"{self.disponibilita}")

    def __repr__(self):
        return (f"{self._cod_cabina} | "
                f"{self.main_print()}")

    def __str__(self):
        return (f"{self._cod_cabina} | "
                f"{self.main_print()}")


class Deluxe(Cabina):
    def __init__(self, cod_cabina, num_letti, ponte, prezzo, tipologia):
        super().__init__(cod_cabina, num_letti, ponte, prezzo)
        self._tipologia = tipologia
        self._prezzo = int(prezzo) * 1.2

    def __repr__(self):
        return (f"{self._cod_cabina} - Deluxe | "
                f"{self.main_print()}")

    def __str__(self):
        return (f"{self._cod_cabina} - Deluxe | "
                f"{self.main_print()}")


class Animali(Cabina):
    def __init__(self, cod_cabina, num_letti, ponte, prezzo, max_animali):
        super().__init__(cod_cabina, num_letti, ponte, prezzo)
        self._max_animali = max_animali
        self._prezzo = int(prezzo) * (1 + (0.1 * int(self._max_animali)))

    def __repr__(self):
        return (f"{self._cod_cabina} - Animali | "
                f"{self.main_print()}")

    def __str__(self):
        return (f"{self._cod_cabina} - Animali | "
                f"{self.main_print()}")
