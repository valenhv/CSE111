# Student: Valentina Hernandez Vera
# Exceeding Requirements: Added a feature that checks if the formula entered by the user matches any known compounds stored in known_molecules_dict. If it finds a match, it prints the name of that compound; otherwise, it says the compound is unknown. This makes the program more informative by identifying recognized chemical formulas.

from formula import parse_formula

# Indexes for inner lists in the periodic table
NAME_INDEX = 0
ATOMIC_MASS_INDEX = 1

# Indexes for inner lists in a symbol_quantity_list
SYMBOL_INDEX = 0
QUANTITY_INDEX = 1

# Define known_molecules_dict with chemical formulas and names
known_molecules_dict = {
    "Al2O3": "aluminum oxide",
    "CH3OH": "methanol",
    "C2H6O": "ethanol",
    "C2H5OH": "ethanol",
    "C3H8O": "isopropyl alcohol",
    "C3H8": "propane",
    "C4H10": "butane",
    "C6H6": "benzene",
    "C6H14": "hexane",
    "C8H18": "octane",
    "CH3(CH2)6CH3": "octane",
    "C13H18O2": "ibuprofen",
    "C13H16N2O2": "melatonin",
    "Fe2O3": "iron oxide",
    "FeS2": "iron pyrite",
    "H2O": "water"
}

def make_periodic_table():
    # Returns a dictionary representing the periodic table with symbol as the key and [name, atomic_mass] as the value.
    return {
        "H": ["Hydrogen", 1.00794],
        "He": ["Helium", 4.002602],
        "Li": ["Lithium", 6.941],
        "Be": ["Beryllium", 9.012182],
        "B": ["Boron", 10.811],
        "C": ["Carbon", 12.0107],
        "N": ["Nitrogen", 14.0067],
        "O": ["Oxygen", 15.9994],
        "F": ["Fluorine", 18.9984032],
        "Ne": ["Neon", 20.1797],
        "Na": ["Sodium", 22.98976928],
        "Mg": ["Magnesium", 24.305],
        "Al": ["Aluminum", 26.9815386],
        "Si": ["Silicon", 28.0855],
        "P": ["Phosphorus", 30.973762],
        "S": ["Sulfur", 32.065],
        "Cl": ["Chlorine", 35.453],
        "K": ["Potassium", 39.0983],
        "Ar": ["Argon", 39.948],
        "Ca": ["Calcium", 40.078],
        "Sc": ["Scandium", 44.955912],
        "Ti": ["Titanium", 47.867],
        "V": ["Vanadium", 50.9415],
        "Cr": ["Chromium", 51.9961],
        "Mn": ["Manganese", 54.938045],
        "Fe": ["Iron", 55.845],
        "Ni": ["Nickel", 58.6934],
        "Co": ["Cobalt", 58.933195],
        "Cu": ["Copper", 63.546],
        "Zn": ["Zinc", 65.38],
        "Ga": ["Gallium", 69.723],
        "Ge": ["Germanium", 72.63],
        "As": ["Arsenic", 74.9216],
        "Se": ["Selenium", 78.96],
        "Br": ["Bromine", 79.904],
        "Kr": ["Krypton", 83.798],
        "Rb": ["Rubidium", 85.4678],
        "Sr": ["Strontium", 87.62],
        "Y": ["Yttrium", 88.90585],
        "Zr": ["Zirconium", 91.224],
        "Nb": ["Niobium", 92.90638],
        "Mo": ["Molybdenum", 95.96],
        "Tc": ["Technetium", 98],
        "Ru": ["Ruthenium", 101.07],
        "Rh": ["Rhodium", 102.9055],
        "Pd": ["Palladium", 106.42],
        "Ag": ["Silver", 107.8682],
        "Cd": ["Cadmium", 112.411],
        "In": ["Indium", 114.818],
        "Sn": ["Tin", 118.71],
        "Sb": ["Antimony", 121.76],
        "I": ["Iodine", 126.90447],
        "Te": ["Tellurium", 127.6],
        "Xe": ["Xenon", 131.293],
        "Cs": ["Cesium", 132.9054519],
        "Ba": ["Barium", 137.327],
        "La": ["Lanthanum", 138.90547],
        "Ce": ["Cerium", 140.116],
        "Pr": ["Praseodymium", 140.90765],
        "Nd": ["Neodymium", 144.242],
        "Pm": ["Promethium", 145],
        "Sm": ["Samarium", 150.36],
        "Eu": ["Europium", 151.964],
        "Gd": ["Gadolinium", 157.25],
        "Tb": ["Terbium", 158.92535],
        "Dy": ["Dysprosium", 162.5],
        "Ho": ["Holmium", 164.93032],
        "Er": ["Erbium", 167.259],
        "Tm": ["Thulium", 168.93421],
        "Yb": ["Ytterbium", 173.04],
        "Lu": ["Lutetium", 174.967],
        "Hf": ["Hafnium", 178.49],
        "Ta": ["Tantalum", 180.94788],
        "W": ["Tungsten", 183.84],
        "Re": ["Rhenium", 186.207],
        "Os": ["Osmium", 190.23],
        "Ir": ["Iridium", 192.217],
        "Pt": ["Platinum", 195.084],
        "Au": ["Gold", 196.966569],
        "Hg": ["Mercury", 200.59],
        "Tl": ["Thallium", 204.3833],
        "Pb": ["Lead", 207.2],
        "Bi": ["Bismuth", 208.9804],
        "Th": ["Thorium", 232.03806],
        "Pa": ["Protactinium", 231.03588],
        "U": ["Uranium", 238.02891],
        "Np": ["Neptunium", 237],
        "Pu": ["Plutonium", 244],
        "Am": ["Americium", 243],
        "Cm": ["Curium", 247],
        "Bk": ["Berkelium", 247],
        "Cf": ["Californium", 251],
        "Es": ["Einsteinium", 252],
        "Fm": ["Fermium", 257],
        "Md": ["Mendelevium", 258],
        "No": ["Nobelium", 259],
        "Lr": ["Lawrencium", 262],
        "Rf": ["Rutherfordium", 267],
        "Db": ["Dubnium", 268],
        "Sg": ["Seaborgium", 271],
        "Bh": ["Bohrium", 270],
        "Hs": ["Hassium", 277],
        "Mt": ["Meitnerium", 276],
        "Ds": ["Darmstadtium", 281],
        "Rg": ["Roentgenium", 280],
        "Cn": ["Copernicium", 285],
        "Nh": ["Nihonium", 284],
        "Fl": ["Flerovium", 289],
        "Mc": ["Moscovium", 288],
        "Lv": ["Livermorium", 293],
        "Ts": ["Tennessine", 294],
        "Og": ["Oganesson", 294],
    }

def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
    total_mass = 0.0
    for symbol, quantity in symbol_quantity_list:
        # Get the name and atomic_mass of the element
        name, atomic_mass = periodic_table_dict[symbol]
        # Update the total_mass of all the elements in symbol_quantity_list
        total_mass += atomic_mass * quantity
    return total_mass

def get_formula_name(formula, known_molecules_dict):
    return known_molecules_dict.get(formula, "unknown compound")

def main():
    # Get a chemical formula for a molecule from the user.
    formula = input("Enter the chemical formula: ").strip()
    # Get the mass of a chemical sample in grams from the user.
    sample_mass = float(input("Enter the mass of the sample in grams: ").strip())

    # Call the make_periodic_table function and store the periodic table in a variable.
    periodic_table_dict = make_periodic_table()

    # Convert formula to uppercase to handle case sensitivity
    formula_upper = formula.upper()

    try:
        # Call the parse_formula function to convert the chemical formula to a compound list
        symbol_quantity_list = parse_formula(formula_upper, periodic_table_dict)
    except Exception as e:
        print(f"Error parsing formula: {e}")
        return

    try:
        # Call the compute_molar_mass function to compute the molar mass of the molecule
        molar_mass = compute_molar_mass(symbol_quantity_list, periodic_table_dict)
        # Compute the number of moles in the sample
        number_of_moles = sample_mass / molar_mass

        # Print the results
        print(f"The molar mass of {formula} is: {molar_mass:.5f} grams/mole")
        print(f"The number of moles in the sample is: {number_of_moles:.5f} moles")

        # Exceeding requirements: Print the name of the compound if known
        # This is an additional feature beyond the basic requirements
        print(get_formula_name(formula_upper, known_molecules_dict))

    except ValueError as ve:
        print(ve)

if __name__ == "__main__":
    main()