class Spiltilstand:
    def __init__(self):
        self.på_tur = 'Hvid'
        self.spil_slut = False

    def skift_tur(self):
        self.på_tur = 'Sort' if self.på_tur == 'Hvid' else 'Hvid'
