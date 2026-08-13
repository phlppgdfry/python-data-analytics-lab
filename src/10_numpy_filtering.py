"""Fase 1.3 — NumPy indexing, slicing en filtering.

Voer uit met: python src/10_numpy_filtering.py
"""

import numpy as np


revenues = np.array([1200, 1450, 980, 1700, 2100])

print(f"Eerste omzet: €{revenues[0]:.2f}")
print(f"Laatste omzet: €{revenues[-1]:.2f}")
print(f"Omzetten op positie 1 t/m 3: {revenues[1:4]}")

high_revenues = revenues[revenues >= 1500]

print(f"Hoge omzetten: {high_revenues}")
print(f"Aantal hoge omzetten: {len(high_revenues)}")
