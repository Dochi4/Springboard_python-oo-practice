"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self,start):
        """
        Creates a starting number for Serial Generator
        """
        self.start = start
        self.initial_value = start

    def generate (self):
        """
        Returns the next sequential number: 
        """
        self.start = self.start+1
        return self.start
    
    def reset(self):
        """
        Resets SerialGenerator to the input value
        """
        self.start = self.initial_value
        return self.start
     