class Passeggero:
    def __init__(self, cod_passeggero, nome, cognome):
        self._cod_passeggero = cod_passeggero
        self._nome = nome
        self._cognome = cognome
        self.cabina = None

    @property
    def cod_passeggero(self):
        return self._cod_passeggero

    @cod_passeggero.setter
    def cod_passeggero(self, valore):
        if not isinstance(int(valore), int):
            raise ValueError("Inserire un numero")
        self._cod_passeggero = valore

    def __eq__(self, other):
        if isinstance(other, Passeggero):
            return self._cod_passeggero == other._cod_passeggero
        return False

    def assegna_cabina(self, cabina):
        self.cabina = cabina

    def __repr__(self):
        return (f"Codice Passeggero: {self._cod_passeggero}, "
                f"Nome: {self._nome}, "
                f"Cognome: {self._cognome}")

    def __str__(self):
        return (f"Codice Passeggero: {self._cod_passeggero}, "
                f"Nome: {self._nome}, "
                f"Cognome: {self._cognome}")

