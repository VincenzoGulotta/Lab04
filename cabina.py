class Cabina:
    def __init__(self, cod_cabina, num_letti, ponte, prezzo):
        self._cod_cabina = cod_cabina
        self._num_letti = num_letti
        self._ponte = ponte
        self._prezzo = int(prezzo)
        self.passeggero = None


    def __eq__(self, other):
        if isinstance(other, Cabina):
            return self._cod_cabina == other._cod_cabina
        return False

    def assegna_passeggero(self, passeggero):
        self.passeggero = passeggero

    def __repr__(self):
        disponibilità = "Disponibile"
        if self.passeggero is not None:
            disponibilità = "Non disponibile"

        return (f"{self._cod_cabina} | "
                f"{self._num_letti} letti - "
                f"Ponte {self._ponte} - "
                f"Prezzo {self._prezzo}$ - "
                f"{disponibilità}")

    def __str__(self):
        disponibilità = "Disponibile"
        if self.passeggero is not None:
            disponibilità = "Non disponibile"

        return (f"{self._cod_cabina} | "
                f"{self._num_letti} letti - "
                f"Ponte {self._ponte} - "
                f"Prezzo {self._prezzo}$ - "
                f"{disponibilità}")


class Deluxe(Cabina):
    def __init__(self, cod_cabina, num_letti, ponte, prezzo, tipologia):
        super().__init__(cod_cabina, num_letti, ponte, prezzo)
        self._tipologia = tipologia
        self._prezzo = int(prezzo) * 1.2


    def __repr__(self):
        disponibilità = "Disponibile"
        if self.passeggero is not None:
            disponibilità = "Non disponibile"

        return (f"{self._cod_cabina} - Deluxe | "
                f"{self._num_letti} letti - "
                f"Ponte {self._ponte} - "
                f"Prezzo {self._prezzo}$ - "
                f"Tipologia: {self._tipologia} - "
                f"{disponibilità}")

    def __str__(self):
        disponibilità = "Disponibile"
        if self.passeggero is not None:
            disponibilità = "Non disponibile"

        return (f"{self._cod_cabina} - Deluxe | "
                f"{self._num_letti} letti - "
                f"Ponte {self._ponte} - "
                f"Prezzo {self._prezzo}$ - "
                f"Tipologia: {self._tipologia} - "
                f"{disponibilità}")


class Animali(Cabina):
    def __init__(self, cod_cabina, num_letti, ponte, prezzo, max_animali):
        super().__init__(cod_cabina, num_letti, ponte, prezzo)
        self._max_animali = max_animali
        self._prezzo = int(prezzo) * (1 + (0.1 * int(self._max_animali)))

    def __repr__(self):
        disponibilità = "Disponibile"
        if self.passeggero is not None:
            disponibilità = "Non disponibile"
        return (f"{self._cod_cabina} - Animali | "
                f"{self._num_letti} letti - "
                f"Ponte {self._ponte} - "
                f"Prezzo {self._prezzo}$ -"
                f"Max animali: {self._max_animali}"
                f"{disponibilità}")

    def __str__(self):
        disponibilità = "Disponibile"
        if self.passeggero is not None:
            disponibilità = "Non disponibile"

        return (f"{self._cod_cabina} - Animali | "
                f"{self._num_letti} letti - "
                f"Ponte {self._ponte} - "
                f"Prezzo {self._prezzo}$ - "
                f"Max animali: {self._max_animali} - "
                f"{disponibilità}")

