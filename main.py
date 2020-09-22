#
# Trabalho de Probabilidade e Estatistica 
# Autores: Jardielma Q. Lima e Amanda Souza
#

import matplotlib.pyplot as plt

def CalculaMedia(listaDados):
	somatorio = 0
	media = 0 
	tam = len(listaDados) #quantidade total da amostra
	
	for valor in listaDados:
		somatorio = somatorio + valor;
	#fim  for
	media = somatorio/tam
	
	return media
#fim função media

def EhPar(listaDados):
	if len(listaDados)%2 == 0:
		return True
	#fim if
	
	return False
#fim função
	
def CalculaMediana(listaDados):	
	#Verifica se o tamanho da lista é par
	if EhPar:
		pos1 = listaDados[int((len(listaDados)/2)-1)]
		pos2 = listaDados[int((len(listaDados)/2))]
		media = CalculaMedia([pos1,pos2])
		return media
	#Se for impar
	else:
		pos = listaDados[int(len(listaDados)/2)]
		return pos
#fim função mediana

def CaculaOcorrencias(listaChaves,dicDados):
	maior = 0
	moda = 0
	
	for chave in listaChaves:
		if dicDados[chave] > maior:
			moda = chave
			maior = dicDados[chave]
		#fim if 
	#fim for
	
	return moda
#fim função
	
	
def CalculaModa(listaDados):
	dicDados = {} 	#dicionario de ocorrencias
	
	for valor in listaDados:
		if valor in dicDados.keys():
			dicDados[valor] = dicDados[valor]+1
		else:
			dicDados[valor] = 1
	#fim for

	listaChaves = dicDados.keys()
	moda = CaculaOcorrencias(listaChaves,dicDados)
	
	return moda
#fim função moda

def CalculaVariancia(listaDados):
	media = CalculaMedia(listaDados)
	somatorio = 0
	tam = len(listaDados)
	variancia = 0

	for valor in listaDados:
		somatorio = somatorio + ((valor - media) ** 2)
	#fim for 
	variancia = somatorio/tam-1
	
	return variancia
#fim função variancia

def VerificaDesvioPadrao(listaDados):
	variancia = CalculaVariancia(listaDados)
	variancia = variancia ** (1/2)
	
	return variancia
##fim função Desvio padrão

def PrimeiroQuartil(listaDados):
	pos = round((len(listaDados)+1)*0.25)
	return listaDados[pos]
#fim função 

def TerceiroQuartil(listaDados):
	pos = round((len(listaDados)+1)*0.75)
	return listaDados[pos]
#fim função 

def AmplitudeInterquartil(listaDados):
	primquartil = PrimeiroQuartil(listaDados)
	terquartil = TerceiroQuartil(listaDados)
	return terquartil - primquartil
#fim função 

def ImprimeBoxplot(listaDados):
	#Cria o boxplot
	plt.boxplot(listaDados)
	#Adiciona titulo
	plt.title("Taxa de Atividade Por Grupos de Idade / Mensal")
	#Mostra na tela
	plt.show()
#fim função 

def ImprimeHistograma(listaDados):
	listaAux = [] #lista sem repetição
	for num in listaDados:
		if num not in listaAux:
			listaAux.append(num)
	#fim for
	listaAux = sorted(listaAux)
	#print(listaAux)
	#criando o histograma
	plt.hist(listaDados,listaAux,histtype="bar",rwidth=0.8)
	
	#criando o titulo e as legendas dos eixos
	plt.xlabel("Grupos de Idade")
	plt.ylabel("Taxa de Atividade")
	plt.title("Taxa de Atividade Por Grupos de Idade")
	#Mostra o histograma na tela
	plt.show()
#fim função

def lerArquivo():
	mat_Dados = []
	arquivo = open("series_historicas.csv", "rt")
	linha = arquivo.readline();
	
	while linha != "":
		linha = linha.strip("\n")
		linha = linha.split(";")	
		mat_Dados.append(linha)
		linha = arquivo.readline()
	#fim while
	
	arquivo.close()
	#print(mat_Dados)
	return mat_Dados
#fim funçao

def trataDados(matDados):
	listaDados = []
	for linha in range(len(matDados)):
		for coluna in range(len(matDados[linha])):
			if (len(matDados[linha][coluna])) == 2:
				valor = int(matDados[linha][coluna])
				listaDados.append(valor)
			#fim for
		#fim for
	#fim for
	return listaDados
#fim função

def main():
	listaDados = []
	
	#Obtendo os dados já ordenados
	matDados = sorted(lerArquivo())
	listaDados = trataDados(matDados)
	#print(listaDados)
	#print("\n\n")
	
	#Imprime todos as analises dos dados
	print('Media: %.6f '% CalculaMedia(listaDados))
	print('Moda: %d '% CalculaModa(listaDados))
	print('Mediana: %.2f '% CalculaMediana(listaDados))
	
	print("Variancia: %.6f" % CalculaVariancia(listaDados))
	print("Desvio Padrao: %.6f " % VerificaDesvioPadrao(listaDados))
	print("Primeiro Quartil: %d" % PrimeiroQuartil(listaDados))
	print("Terceiro Quartil: %d" % TerceiroQuartil(listaDados))
	print("Amplitude Interquartil: %d" % AmplitudeInterquartil(listaDados))

	#Histograma
	ImprimeHistograma(listaDados)

	#BoxPLot
	ImprimeBoxplot(listaDados)
	
if __name__ == '__main__':
	main()
