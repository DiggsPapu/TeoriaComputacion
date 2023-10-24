def imprimir_gramatica(gramatica: dict):
    for no_terminal, production in gramatica.items():
        production_string = "|".join(production)
        print(f"    {no_terminal} -> {production_string}")