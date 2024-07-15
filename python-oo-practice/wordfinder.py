"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    ...
    def __init__(self,path):
        """
        
        """
        self.path = path
    
    def random(self):
        rando_choice = (random.choice(list(open(f"{self.path}"))))
        return  rando_choice.strip("\n")
    
class SpecialWordFinder(WordFinder):
    def __init__(self, path):
        super().__init__(path)
    
    def random(self):
        words = []
        with open(self.path, 'r') as file:
            for line in file:
                line = line.strip()
                if line and not line.startswith("#"):
                    words.append(line)
        
        return random.choice(words) if words else None