"""Fase 1.1 — NumPy-arrays en berekeningen per element.

Voer uit met: python src/08_numpy_arrays.py
"""

import numpy as np


revenue_list = [1200, 1450, 980]
revenues = np.array(revenue_list)

print(f"Python-list: {revenue_list}")
print(f"NumPy-array: {revenues}")

print(f"Array × 2: {revenues * 2}")
print(f"Array + 100: {revenues + 100}")
