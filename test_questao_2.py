from questao_2 import contadorVogal

def test_conta_vogais():
    assert contadorVogal("Teste do CONTA vogais")
    assert contadorVogal("exercicio 2 realizado")
    assert contadorVogal("atividade 2")