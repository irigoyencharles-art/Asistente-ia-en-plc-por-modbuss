"""Script simple para demostrar su funcionamiento."""

from pathlib import Path


def sumar(a: float, b: float) -> float:
    """Devuelve la suma de dos números."""
    return a + b


def main() -> None:
    """Muestra información básica del script y realiza una suma de ejemplo."""

    script_path = Path(__file__).resolve()
    numero_uno = 5
    numero_dos = 7
    resultado = sumar(numero_uno, numero_dos)

    print("=== Ejemplo de funcionamiento ===")
    print(f"Archivo en ejecución: {script_path.name}")
    print(f"Ubicación del archivo: {script_path.parent}")
    print(f"Primer número: {numero_uno}")
    print(f"Segundo número: {numero_dos}")
    print(f"Resultado de la suma: {resultado}")


if __name__ == "__main__":
    main()
