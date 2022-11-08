"""
Testing @dataclass
"""

from dataclasses import dataclass

from numpy import apply_along_axis


@dataclass
class A:
    apa: int
    bepa: int
    cepa: int = 23

a = A(1,2)
print(a)
