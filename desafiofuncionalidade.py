
# Criação da classe geradora.
class gerador:
    # Definindo a função que retornará a String com os sequenciais inteiros concatenados a um texto e ao seu respectivo valor.
    def gerar_valores(self, valores):
        resultado = ''
        total = 0
        # Laço de repetição para formatar os valores e calcular o total.
        for i, valor in enumerate(valores, start=1):
            total += valor
            resultado += f'{i} cujo valor é R${valor:.2f}, '

        resultado = resultado.rstrip(", ") + "."
        resultado += f' Total = R${total:.2f}.'
        return f'Remesse gerada: {resultado}'

# Instanciando a classe para o teste
gerador = gerador()

valores = [88.00, 130.00, 54.90, 293.30, 44.80] #Valores dados de exemplo para o desafio
print(gerador.gerar_valores(valores)) # Modelo de retorno esperado
print()

valores_1 = [100.00]
print(gerador.gerar_valores(valores_1))
print()

valores_2 = [15.25, 25.50, 35.75, 45.00]
print(gerador.gerar_valores(valores_2))
print()

valores_3 = [12.50, 22.75, 32.00, 42.25, 52.50, 62.75]
print(gerador.gerar_valores(valores_3))
print()

valores_4 = [10.00, 20.00, 30.00, 40.00, 50.00, 60.00, 70.00]
print(gerador.gerar_valores(valores_4))