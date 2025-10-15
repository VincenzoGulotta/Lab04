class Cabina:
    def __init__(self, cod_cabina, num_letti, ponte, prezzo):
        self._cod_cabina = cod_cabina
        self._num_letti = num_letti
        self._ponte = ponte
        self._prezzo = prezzo
        self.passeggero = None

    @property
    def cod_cabina(self):
        return self._cod_cabina

    @property
    def num_letti(self):
        return self._num_letti

    @property
    def ponte(self):
        return self._ponte

    @property
    def prezzo(self):
        return self._prezzo

    @cod_cabina.setter
    def cod_cabina(self, valore):
        if len(valore) != 4:
            raise ValueError("Codice cabina non valido")
        self._cod_cabina = valore

    @num_letti.setter
    def num_letti(self, valore):
        if not isinstance(int(valore), int):
            raise ValueError("Inserire un numero")
        self._num_letti = valore

    @ponte.setter
    def ponte(self, valore):
        if not isinstance(int(valore), int):
            raise ValueError("Inserire un numero")
        self._ponte = valore

    @prezzo.setter
    def prezzo(self, valore):
        if not isinstance(int(valore), int):
            raise ValueError("Inserire un numero")
        self._prezzo = valore

    def __eq__(self, other):
        if isinstance(other, Cabina):
            return self._cod_cabina == other._cod_cabina
        return False

    def assegna_passeggero(self, passeggero):
        self.passeggero = passeggero

    def __repr__(self):
        return (f"Codice Cabina Standard: {self._cod_cabina}, "
                f"Numero letti: {self._num_letti}, "
                f"Ponte: {self._ponte}, "
                f"Prezzo: {self._prezzo}")

    def __str__(self):
        return (f"Codice Cabina Standard: {self._cod_cabina}, "
                f"Numero letti: {self._num_letti}, "
                f"Ponte: {self._ponte}, "
                f"Prezzo: {self._prezzo}")


class Deluxe(Cabina):
    def __init__(self, cod_cabina, num_letti, ponte, prezzo, tipologia):
        super().__init__(cod_cabina, num_letti, ponte, prezzo)
        self._tipologia = tipologia

    @property
    def prezzo(self):
        return self._prezzo

    @prezzo.setter
    def prezzo(self, valore):
        self._prezzo = self.prezzo * 1, 2

    def __repr__(self):
        return (f"Codice Cabina Deluxe: {self.cod_cabina}, "
                f"Numero letti: {self.num_letti}, "
                f"Ponte: {self.ponte}, "
                f"Prezzo: {self.prezzo}, "
                f"Tipologia: {self._tipologia}")

    def __str__(self):
        return (f"Codice Cabina Deluxe: {self.cod_cabina}, "
                f"Numero letti: {self.num_letti}, "
                f"Ponte: {self.ponte}, "
                f"Prezzo: {self.prezzo}, "
                f"Tipologia: {self._tipologia}")


class Animali(Cabina):
    def __init__(self, cod_cabina, num_letti, ponte, prezzo, max_animali):
        super().__init__(cod_cabina, num_letti, ponte, prezzo)
        self._max_animali = max_animali

    @property
    def prezzo(self):
        return self._prezzo

    @prezzo.setter
    def prezzo(self, valore):
        self.prezzo = self.prezzo * (1 + 0, 1 * self._max_animali)

    def __repr__(self):
        return (f"Codice Cabina Animali: {self.cod_cabina}, "
                f"Numero letti: {self.num_letti}, "
                f"Ponte: {self.ponte}, "
                f"Prezzo: {self.prezzo}, "
                f"Massimo animali ammessi: {self._max_animali}")

    def __str__(self):
        return (f"Codice Cabina Animali: {self.cod_cabina}, "
                f"Numero letti: {self.num_letti}, "
                f"Ponte: {self.ponte}, "
                f"Prezzo: {self.prezzo}, "
                f"Massimo animali ammessi: {self._max_animali}")

