complimentary_ribonucleotides = {'A': 'U', 'U': 'A', 'C': 'G', 'G': 'C'}
complimentary_nucleotides = {'A': 'T', 'U': 'A', 'C': 'G', 'G': 'C'}
from dna import DNA

class RNA:
    def __init__(self, sequence: str):
        self.sequence = sequence
        if not self._check_validity():
            raise ValueError("Bad sequence. Sequences must only contain G, C, A, and U")

    def __eq__(self, other):
        return True if str(self) == str(other) else False

    def __str__(self):
        return self.sequence

    def __repr__(self):
        return "RNA(sequence='{}')".format(self.sequence)

    def _check_validity(self):
        are_good = (nucleotide.upper() in 'GCAU' for nucleotide in self.sequence)
        return True if all(are_good) else False

    @property
    def complimentary_sequence(self):
        return RNA(''.join(complimentary_ribonucleotides[nt.upper()] for nt in self.sequence))

    def retrotranscribe(self):
        return DNA(''.join(complimentary_nucleotides[nt.upper()] for nt in self.sequence))
