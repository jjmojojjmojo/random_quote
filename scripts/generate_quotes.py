"""
Generate a CSV file of random quotes attributed to random authors.
"""

import csv
import markovify
import json
import random
import os

import argparse

names_source = os.path.abspath(os.path.join(os.path.dirname(__file__), "names.json"))
chain_source = os.path.abspath(os.path.join(os.path.dirname(__file__), "chain.json"))

class QuoteGenerator:
    """
    Generates random quotes based on a pre-configured markov chain and
    list of random author names.
    
    When called, yields one new quote.
    """
    def __init__(self, chainfile, namefile):
        """
        chainfile is an open file handle containing JSON data saved by markovify
        
        namefile is an open file handle containing a JSON list of pre-generated
        author names
        
        see: generate_authors.py, build_markov_chain.py
        """
        self.chars_per_sentence = (50, 200)
        self.max_sentences = 3
        
        self.text_model = markovify.Text.from_json(chainfile.read())
        
        self.authors = json.load(namefile)
            
    def generate_quote(self):
        """
        Generate a single quote and author.
        """
        output = {
            'author': random.choice(self.authors)
        }
        
        quote = []
        
        sentences = random.randrange(1, self.max_sentences+1)
        for i in range(sentences):
            max_chars = random.randint(self.chars_per_sentence[0], self.chars_per_sentence[1])
            sentence = self.text_model.make_short_sentence(min_chars=25, max_chars=max_chars)
            if sentence:
                quote.append(sentence)
            else:
                # sometimes markovify gives up and returns None. 
                # we are opting to produce fewer sentences instead of re-generating.
                #print(f"Sentence not built. sentences: {sentences}, max_chars: {max_chars}, out: {sentence}")
                pass
            
        
        output['quote'] = " ".join(quote)
        
        return output
        
    def __call__(self, count=1000):
        """
        Generator; creates random quotes. 
        
        Count sets how many are to be generated in total.
        """
        for i in range(count):
            yield self.generate_quote()

parser = argparse.ArgumentParser(description='Generate a CSV file containing 1000 random quotes using a Markov chain.')
parser.add_argument(
    '-o', '--outfile', 
    type=argparse.FileType('w'), 
    default="quotes.csv", 
    help="Output is written to this file as CSV. Default: quotes.csv")
parser.add_argument(
    '-a', '--authornames', 
    type=argparse.FileType('r'), 
    default=names_source, 
    help=f"A JSON list containing the pool of possible author names. Default: {names_source}")
parser.add_argument(
    '-c', '--chainfile', 
    type=argparse.FileType('r'), 
    default=chain_source, 
    help=f"Stored state of markovify markov chain used to generate quotes. Default: {chain_source}")
parser.add_argument(
    '-s', '--seed', 
    type=int, 
    help="Seed the random number generator for reproducible results.")
parser.add_argument(
    'count', 
    metavar="COUNT", 
    type=int, 
    nargs="?", 
    default=1000, help="Number of quotes to generate. Defaults to 1000.")

if __name__ == '__main__':
    count = 0
    
    opts = parser.parse_args()
    
    if opts.seed:
        random.seed(opts.seed)
    
    generator = QuoteGenerator(opts.chainfile, opts.authornames)
    
    writer = csv.DictWriter(opts.outfile, fieldnames=['quote', 'author'])
    writer.writeheader()
    for quote in generator(opts.count):
        writer.writerow(quote)