"""Fase 1.2 — basisstatistiek met NumPy.

Voer uit met: python src/09_numpy_statistics.py
"""

import numpy as np


revenues = np.array([1200, 1450, 980, 1700, 2100])

print(f"Omzetten: {revenues}")
print(f"Gemiddelde omzet: €{revenues.mean():.2f}")
print(f"Mediane omzet: €{np.median(revenues):.2f}")
print(f"Standaardafwijking: €{revenues.std():.2f}")
print(f"Laagste omzet: €{revenues.min():.2f}")
print(f"Hoogste omzet: €{revenues.max():.2f}")
