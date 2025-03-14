cotacao_dollar = float(input("Digite a cotação do Dollar"))  # Solicita ao usuário a cotação do dólar e converte para float (número decimal).
qtd_dollar = int(input("Quanto dolares você tem?"))  # Solicita ao usuário a quantidade de dólares que ele possui e converte para inteiro.
real = cotacao_dollar * qtd_dollar  # Calcula o valor em reais multiplicando a cotação do dólar pela quantidade de dólares.
modeda_real = f"R$ {real:_.2f}"  # Formata o valor em reais com 2 casas decimais e separador de milhar como sublinhado.
moeda_real = moeda_real.replace('.',',').replace('_','.')  # Substitui o ponto por vírgula para adequar à notação monetária brasileira e o sublinhado por ponto.
print(f"$${qtd_dollar} dollars são {moeda_real}")  # Exibe a quantidade de dólares e o valor correspondente em reais. (Erro de digitação em "dolares")
