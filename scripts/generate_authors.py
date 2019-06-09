"""
Generate a json file containing 1000 randomly generated first/last names.
"""

import random
import json
import os

names_dest = os.path.abspath(os.path.join(os.path.dirname(__file__), "names.json"))
first_name_list = os.path.abspath(os.path.join(os.path.dirname(__file__), "first-names.txt"))
surname_list = os.path.abspath(os.path.join(os.path.dirname(__file__), "surnames.txt"))

def reservior_select(filename, count):
    """
    Return count randomly selected lines from filename.
    
    From: https://en.wikipedia.org/wiki/Reservoir_sampling#Example_implementation
    """
    sample = []
    
    with open(filename, "r") as fp:
        for index, line in enumerate(fp):
            line = line.strip()
            if index < count:
                sample.append(line)
            else:
                r = random.randint(0, index)
                if r < count:
                    sample[r] = line
                    
    return sample
    
    
if __name__ == '__main__':
    first_names = reservior_select(first_name_list, 100)
    last_names = reservior_select(surname_list, 100)
    
    output = []
    
    while len(output) < 1000:
        first = random.choice(first_names)
        last = random.choice(last_names)
        
        output.append(f"{first} {last}")
        
    with open(names_dest, "w") as outfile:
        json.dump(output, outfile, indent="\t")

