# Script pra gerar arquivos.
# arquivo = open("contatos.py", "a")
# arquivo.write("#")

inicio = 1
final = 18

sufixo = "-Exercício.py"
prefixo = "Numeração"
for c in range(inicio, final+1):
    prefixo = str(c).zfill(len(str(final)))
    nomeExercicio = prefixo+sufixo

    arquivo = open(nomeExercicio, "a")
    arquivo.write("#")

