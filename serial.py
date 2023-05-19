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

    def __init__(self, start=0):
        """Initialize serial number generator with start number."""
        self.start = start
        self.next = start

    def __repr__(self):
        """Return representation."""
        return f"<SerialGenerator start={self.start} next={self.next}>"

    def generate(self):
        """Return next serial number."""
        self.next += 1
        return self.next - 1

    def reset(self):
        """Reset serial number to original start number."""
        self.next = self.start
