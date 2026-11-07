"""Die 20 Vereine der 3. Liga 2026/27 an EINER Stelle.
generate.py baut daraus VEREIN_FILTER, VEREIN_WAPPEN, KLUB_LOGO und VEREIN_SLUG.
Aufstieg und Abstieg: nur diese Liste und die Logos in logos/ ändern.
Suchbegriffe eindeutig halten: "köln", "stuttgart", "hoffenheim" allein meinen fast immer die Erstligisten."""

# (Kurzname, Slug, voller Name, Suchbegriffe im Text)
VEREINE = [
    ("Saarbrücken",   "saarbruecken",  "1. FC Saarbrücken",        ["1. fc saarbrücken", "fc saarbrücken", "saarbrücken"]),
    ("Aachen",        "aachen",        "Alemannia Aachen",         ["alemannia aachen", "alemannia", "aachen"]),
    ("Ingolstadt",    "ingolstadt",    "FC Ingolstadt 04",         ["fc ingolstadt", "ingolstadt", "schanzer"]),
    ("Düsseldorf",    "duesseldorf",   "Fortuna Düsseldorf",       ["fortuna düsseldorf", "düsseldorf", "f95"]),
    ("Fortuna Köln",  "fortunakoeln",  "Fortuna Köln",             ["sc fortuna köln", "fortuna köln"]),
    ("Rostock",       "rostock",       "Hansa Rostock",            ["fc hansa rostock", "hansa rostock", "fc hansa", "hansa", "rostock"]),
    ("Regensburg",    "regensburg",    "Jahn Regensburg",          ["ssv jahn regensburg", "jahn regensburg", "ssv jahn", "jahn", "regensburg"]),
    ("Duisburg",      "duisburg",      "MSV Duisburg",             ["msv duisburg", "msv", "duisburg", "zebras"]),
    ("Münster",       "muenster",      "Preußen Münster",          ["preußen münster", "sc preußen", "preußen", "münster"]),
    ("RW Essen",      "essen",         "Rot-Weiss Essen",          ["rot-weiss essen", "rot-weiß essen", "rw essen", "rwe", "essen", "essener"]),
    ("Verl",          "verl",          "SC Verl",                  ["sc verl", "verl"]),
    ("Großaspach",    "grossaspach",   "SG Sonnenhof Großaspach",  ["sonnenhof großaspach", "großaspach", "aspach"]),
    ("Meppen",        "meppen",        "SV Meppen",                ["sv meppen", "meppen"]),
    ("Mannheim",      "mannheim",      "SV Waldhof Mannheim",      ["sv waldhof mannheim", "waldhof mannheim", "sv waldhof", "waldhof", "mannheim"]),
    ("Wiesbaden",     "wiesbaden",     "SV Wehen Wiesbaden",       ["sv wehen wiesbaden", "wehen wiesbaden", "sv wehen", "wiesbaden"]),
    ("Hoffenheim II", "hoffenheim2",   "TSG 1899 Hoffenheim II",   ["tsg hoffenheim ii", "hoffenheim ii", "hoffenheim 2"]),
    ("Havelse",       "havelse",       "TSV Havelse",              ["tsv havelse", "havelse"]),
    ("Stuttgart II",  "stuttgart2",    "VfB Stuttgart II",         ["vfb stuttgart ii", "stuttgart ii", "vfb ii"]),
    ("Viktoria Köln", "viktoriakoeln", "Viktoria Köln",            ["fc viktoria köln", "viktoria köln"]),
    ("Würzburg",      "wuerzburg",     "Würzburger Kickers",       ["würzburger kickers", "würzburg"]),
]
# Vereinsnamen, die zugleich Wortanfang gewöhnlicher Wörter sind ("Verl" in "verliert", "Essen" in "Essener"
# geht, "essentiell" nicht): brauchen auch rechts eine Wortgrenze
GANZES_WORT = {"verl", "essen"}

LIGA = {"openligadb": "bl3", "transfermarkt": "L3", "name": "3. Liga", "kurz": "3. Liga"}
