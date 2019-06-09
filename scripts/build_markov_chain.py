"""
Construct a markov chain based on Mary Shelley Wollstonecraft's works.
"""

import markovify
import json

from pathlib import Path
import os

chain_dest = os.path.abspath(os.path.join(os.path.dirname(__file__), "chain.json"))
source_text = os.path.abspath(os.path.join(os.path.dirname(__file__), "source-text"))

chains = []

for path in Path(source_text).iterdir():
    output = ""
    with open(path, "r") as source:
        output = source.read()
        
    chains.append(markovify.Text(output, retain_original=False))
    
main = markovify.combine(chains)

with open(chain_dest, "w") as dest:
    json.dump(main.to_dict(), dest, indent="\t")