from enum import Enum

class AtomType(Enum):
    ISOTOPE = "Isotope"
    RADIOACTIVE = "Radiactive"
    ION = "Ion"
    ANTIMATTER = "Antimatter" 
    STABLE = "Stable"

class Atom:
    name : str
    atomic_mass_unit: int
    neutrons_number: int
    protons_number : int 
    electrons_number : int
    atom_tupe : AtomType

    def __init__(self, name = "невідомо", atomic_mass_unit = 1, neutrons_number = 1, protons_number = 1, electrons_number = 1, atom_tupe = AtomType.STABLE):
        self.name = name
        self.atomic_mass_unit = atomic_mass_unit
        self.neytrons_number = neutrons_number
        self.protons_number = protons_number
        self.electrons_number = electrons_number
        self.atom_tupe = atom_tupe

    def is_neutral(self) -> bool:
        return self.neytrons_number == self.electrons_number
        
    def __repr__(self):
        return f"{self.name}(mass: {self.atomic_mass_unit}, neutrons: {self.neutrons_number}, protons: {self.protons_number}, electrons: {self.electrons_number}, type: {self.atom_type.name})"
