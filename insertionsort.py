import numpy as np
import random
import matplotlib.pyplot as plt
import time

# Declaração de variáveis

tamanho=10
tempos=[]
tamanhos=[]

# Implementação da função de ordenação

def insertionsort (vetor):
	for i in range(1,len(vetor)):
		aux = vetor[i]
		j = i-1
		while(j>=0) and aux < vetor[j]:
			vetor[j+1]=vetor[j]
			j=j-1
		vetor[j+1]=aux
	return vetor
	
while(tamanho<=10000):

	# Geração o Array aleatório
	vetor = []
	for _ in range(tamanho):
		vetor.append(random.randint(0, 100))
	
	# Execução da ordenação medindo o tempo gasto
	inicio = time.time()
	insertionsort(vetor)
	fim = time.time()
	tempo=fim-inicio
	
	# Limpando o Array

	del vetor [ 00:len(vetor) ] 

	# Adição os dados aos arrays que servirão de base para a plotagem
	tamanhos.append(tamanho)
	tempos.append(tempo)
	
	# Incremento do tamanho do Array	

	if(tamanho>=1000):
		tamanho=tamanho+250
	else:
		tamanho=tamanho*10

# Plotagem do gráfico

plt.plot(tamanhos, tempos,'k')
plt.xlabel('tamanho do vetor')
plt.ylabel('tempo(s)')
plt.show()
