# brikker.py
class Skakbrik:
    def __init__(self, farve, navn):
        self.farve = farve
        self.navn = navn
        # Du kan tilføje yderligere egenskaber som position, hvis nødvendigt

# Eksempel på en specifik brik
class Bonde(Skakbrik):
    def __init__(self, farve):
        super().__init__(farve, 'Bonde')
        # Implementer specifikke egenskaber og metoder for bonden her
class Skakbrik:
    def __init__(self, farve, navn):
        self.farve = farve
        self.navn = navn
        # Du kan tilføje yderligere egenskaber som position her

class Bonde(Skakbrik):
    def __init__(self, farve):
        super().__init__(farve, 'Bonde')

class Tårn(Skakbrik):
    def __init__(self, farve):
        super().__init__(farve, 'Tårn')

class Springer(Skakbrik):
    def __init__(self, farve):
        super().__init__(farve, 'Springer')

class Løber(Skakbrik):
    def __init__(self, farve):
        super().__init__(farve, 'Løber')

class Dronning(Skakbrik):
    def __init__(self, farve):
        super().__init__(farve, 'Dronning')

class Konge(Skakbrik):
    def __init__(self, farve):
        super().__init__(farve, 'Konge')
