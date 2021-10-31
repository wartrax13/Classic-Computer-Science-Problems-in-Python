# Calculando pi com a fórmula de Leibniz
# pi = 4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11...
# O denominador pode ser uma variavel que começa em 1 e é incrementada de 2.
# A operação pode ser representada como -1 ou 1, já que estamos subtraindo ou somando


def calculate_pi(n_terms: int) -> float:
    numerator: float = 4.0
    denominador: float = 1.0
    operation: float = 1.0
    pi: float = 0.0

    for _ in range(n_terms):
        pi += operation * (numerator / denominador)
        denominador += 2.0
        operation *= -1.0
    return pi

if __name__ == "__main__":
    print(calculate_pi(1000000))
