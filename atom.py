from enum import Enum

class AtomType(Enum):
    ISOTOPE = 1
    RADIOACTIVE = 2
    ION = 3
    ANTIMATTER = 4 
    STABLE = 5

class Atom:
    def __init__(self, name : str, atomic_mass_unit : int, neutrons_number: int, protons_number : int, electrons_number : int, atom_tupe : AtomType):
        self.name = name
        self.atomic_mass_unit = atomic_mass_unit
        self.neytrons_number = neutrons_number
        self.protons_number = protons_number
        self.electrons_number = electrons_number
        self.atom_tupe = atom_tupe

    def is_neutral(self) -> bool:
        return self.neytrons_number == self.electrons_number
        
    def __repr__(self):
        return f"{self.name}(mass: {self.atomic_mass}, neutrons: {self.neutrons}, protons: {self.protons}, electrons: {self.electrons}, type: {self.atom_type.name})"
