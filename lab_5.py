from atom import Atom
import periodic_system

class Molecule:
    __name : str
    __atoms : list
    def __init__(self, name = "Невідомо", atoms = []):
        self.__name = name
        self.__atoms = atoms
    
    def sort_atoms(self):
        self.__atoms.sort(key=lambda atom: atom.atomic_mass_unit)

    def __str__(self):
        atoms = []
        for el in self.__atoms:
            atoms.append(el.name)
        return f"Molecule: (name = {self.__name}, atoms = {atoms})"
    
    def formula(self, sort = True):
        if sort == True:
            self.sort_atoms()
        else: 
            pass
        previous_atom = ""
        quantity = 0
        current_formul = ""
        final_formul = ""
        for atom in self.__atoms:
            if atom.chemical_record == previous_atom:
                previous_atom = atom.chemical_record
                quantity += 1
                current_formul = atom.chemical_record + f"{quantity}" 
            else:
                if quantity == 0:
                    previous_atom = atom.chemical_record
                    quantity += 1
                else:
                    final_formul += current_formul
                    current_formul = ""
                    previous_atom = atom.chemical_record
                    quantity = 1
                    current_formul += atom.chemical_record + (f"{quantity}" if quantity > 1 else "")
        final_formul += current_formul
        return final_formul

    def find_mass(self):
        if not atoms: 
            return 0
        total_mass = 0
        for atom in self.__atoms:
            total_mass += atom.atomic_mass_unit
        return total_mass
    

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
print(molecule.formula(sort=False))
molecule.sort_atoms()
print(molecule)
print(molecule.find_mass())


print(periodic_system.B_ISO.is_neutral())
print(periodic_system.AR_STA.is_neutral())

atoms_names_2 = input("Введіть атоми через кому: ").split(',')
atoms_2 = [getattr(periodic_system, name.strip()) for name in atoms_names_2]

print(find_average_mass(atoms_2))