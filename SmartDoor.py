# Declaração das variáveis
nivel_acesso: int = 5
porta_destravada: bool = False

# Estrutura condicional
if nivel_acesso >= 5:
    porta_destravada = True
    print("acesso liberado")
else:
    print("Acesso negado: Permissão insuficiente")