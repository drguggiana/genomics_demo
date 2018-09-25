from rna import RNA
from dna import DNA
import pytest

def test_bad_sequence_raises_error():
    with pytest.raises(ValueError):
        RNA('ATB')


def test_complimentary_sequence_works():
    assert RNA('GUC').complimentary_sequence == RNA('CAG')
    assert RNA('AUC').complimentary_sequence == RNA('UAG')


def test_is_dna():
    with pytest.raises(ValueError):
        RNA('ATG')

def test_does_it_transcribe():
    assert RNA('AUGC').retrotranscribe() == DNA('TACG')