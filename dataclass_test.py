"""
Testing @dataclass
"""

from dataclasses import dataclass
from enum import Enum, auto

class Apor(Enum):
    CHIMPANS = auto()
    GORILLA = auto()
    ORANGUTANG = auto()
    GIBBON = auto()


@dataclass
class A:
    apa: Apor
    bepa: int
    cepa: int = 23


def apa(a: A) -> Apor:
    return a.apa

a = A(Apor.CHIMPANS,2)
print(a, apa(a))
