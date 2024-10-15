from atom import Atom
import periodic_system

class Molecule:
    def __init__(self, name: str, atoms: list[Atom]):
        self.name = name
        self.atoms = atoms
    
    def sort_atoms(self):
        self.atoms.sort(key=lambda atom: atom.atomic_mass_unit)

    def __str__(self):
        atoms = []
        for el in self.atoms:
            atoms.append(el.name)
        return f"Molecule: (name = {self.name}, atoms = {atoms})"

def find_average_mass(atoms: list[Atom]):
    if not atoms: 
        return 0
    total_mass = 0
    for atom in atoms:
        total_mass += atom.atomic_mass_unit
    return total_mass / len(atoms)      

name = str(input("Введіть назву молекули: ")) 
atoms_names = input("Введіть атоми через кому: ").split(',')
atoms = [getattr(periodic_system, name.strip()) for name in atoms_names]
molecule = Molecule(name, atoms)

print(molecule)
molecule.sort_atoms()
print(molecule)

print(periodic_system.B_ISO.is_neutral())
print(periodic_system.AR_STA.is_neutral())

atoms_names_2 = input("Введіть атоми через кому: ").split(',')
atoms_2 = [getattr(periodic_system, name.strip()) for name in atoms_names_2]

print(find_average_mass(atoms_2))