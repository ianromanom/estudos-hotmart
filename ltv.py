   """Módulo de métricas de retenção — cálculo de LTV."""

def calcular_ltv(ticket_medio, frequencia_compras, margem=1.0):
    """LTV = ticket médio x frequência de compras x margem."""
    return ticket_medio * frequencia_compras * margem


if __name__ == "__main__":
    ltv = calcular_ltv(ticket_medio=157, frequencia_compras=1.74)
    print(f"LTV: R$ {ltv:.2f}")
