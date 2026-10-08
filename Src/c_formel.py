"""
Psi-Field Dynamics – Implementierung der c(ρ,Ψ)-Formel

Autor: Bouly (Ingo Wisniewski) & Lyra & Limen
Datum: 08.10.2026
Version: 2.0
Lizenz: Creative Commons BY-NC-SA 4.0
"""

import math

# Konstanten
c0 = 299792458  # Vakuumlichtgeschwindigkeit in m/s
kappa = 1.23e-42  # Kopplungskonstante in m³/kg
kappa_H = 0.42  # Handlungskonstante
psi_grund = 0.33  # Grundwert für Ψ²
B_grund = 0.27  # Grundwert für B²
L_grund = 1.0  # Grundwert für L²


def c_rho_psi(rho, psi, B=0.0, L=0.0, H=0.0):
    """
    Berechnet die Lichtgeschwindigkeit in Abhängigkeit von
    Dichte (rho), Bewusstseinsfeld (psi), B-Feld (B),
    Liebe (L) und Handlung (H).

    Formel:
    c(ρ,Ψ,B,L,H) = c₀ / √(1 + κ·(ρ + 0,33·Ψ² + 0,27·B² + 1,0·L²) - κ_H·H²)

    Parameter:
    rho : Dichte in kg/m³
    psi : Bewusstseinsfeld (dimensionslos)
    B   : B-Feld (dimensionslos)
    L   : Liebe (dimensionslos)
    H   : Handlung (dimensionslos)

    Rückgabe:
    Lichtgeschwindigkeit in m/s
    """
    term = 1 + kappa * (
        rho
        + psi_grund * psi**2
        + B_grund * B**2
        + L_grund * L**2
    ) - kappa_H * H**2

    if term <= 0:
        raise ValueError("Term unter der Wurzel muss positiv sein.")

    return c0 / math.sqrt(term)


# Beispielrechnung
if __name__ == "__main__":
    # Erde: rho = 5515 kg/m³, psi = 0, B = 0, L = 0, H = 0.0243
    c_erde = c_rho_psi(rho=5515, psi=0.0, H=0.0243)
    print(f"c_Erde = {c_erde:.6f} m/s")
    print(f"c_Erde / c0 = {c_erde / c0:.6f}")

    # Erwarteter Wert: 1.000124 c0