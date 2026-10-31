"""Die 18 Vereine der 2. Bundesliga 2026/27 an EINER Stelle.
generate.py baut daraus VEREIN_FILTER, VEREIN_WAPPEN, KLUB_LOGO und VEREIN_SLUG.
Aufstieg und Abstieg: nur diese Liste, die Logos in logos/ und OPENLIGADB_ID ändern."""

# (Kurzname, Slug, voller Name, Suchbegriffe im Text, OpenLigaDB-Name)
VEREINE = [
    ("Heidenheim",     "heidenheim",     "1. FC Heidenheim 1846",   ["1. fc heidenheim", "fc heidenheim", "heidenheim", "fch"]),
    ("Kaiserslautern", "kaiserslautern", "1. FC Kaiserslautern",    ["1. fc kaiserslautern", "fc kaiserslautern", "kaiserslautern", "die roten teufel"]),
    ("Magdeburg",      "magdeburg",      "1. FC Magdeburg",         ["1. fc magdeburg", "fc magdeburg", "magdeburg"]),
    ("Nürnberg",       "nuernberg",      "1. FC Nürnberg",          ["1. fc nürnberg", "fc nürnberg", "nürnberg"]),
    ("Bielefeld",      "bielefeld",      "DSC Arminia Bielefeld",   ["arminia bielefeld", "dsc arminia", "arminia", "bielefeld"]),
    ("Dresden",        "dresden",        "Dynamo Dresden",          ["dynamo dresden", "sg dynamo", "dresden"]),
    ("Braunschweig",   "braunschweig",   "Eintracht Braunschweig",  ["eintracht braunschweig", "braunschweig"]),
    ("Cottbus",        "cottbus",        "Energie Cottbus",         ["energie cottbus", "cottbus"]),
    ("St. Pauli",      "stpauli",        "FC St. Pauli",            ["fc st. pauli", "st. pauli", "st pauli", "kiezkicker"]),
    ("Hannover",       "hannover",       "Hannover 96",             ["hannover 96", "hannover"]),
    ("Hertha",         "hertha",         "Hertha BSC",              ["hertha bsc", "hertha"]),
    ("Kiel",           "kiel",           "Holstein Kiel",           ["holstein kiel", "holstein", "die störche"]),
    ("Karlsruhe",      "karlsruhe",      "Karlsruher SC",           ["karlsruher sc", "ksc", "karlsruhe"]),
    ("Fürth",          "fuerth",         "SpVgg Greuther Fürth",    ["greuther fürth", "spvgg fürth", "fürth", "kleeblatt"]),
    ("Darmstadt",      "darmstadt",      "SV Darmstadt 98",         ["sv darmstadt 98", "darmstadt 98", "darmstadt", "die lilien"]),
    ("Bochum",         "bochum",         "VfL Bochum",              ["vfl bochum", "bochum"]),
    ("Osnabrück",      "osnabrueck",     "VfL Osnabrück",           ["vfl osnabrück", "osnabrück"]),
    ("Wolfsburg",      "wolfsburg",      "VfL Wolfsburg",           ["vfl wolfsburg", "wolfsburg"]),
]
LIGA = {"openligadb": "bl2", "transfermarkt": "L2", "name": "2. Bundesliga", "kurz": "2. Liga"}
