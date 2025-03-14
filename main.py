# Solicita ao usuário a cotação do dólar e converte para float (número decimal).
cotacao_dollar = float(input("Digite a cotação do Dollar"))  

# Solicita ao usuário a quantidade de dólares que ele possui e converte para inteiro.
qtd_dollar = int(input("Quanto em dollars você tem?"))  

# Calcula o valor em reais multiplicando a cotação do dólar pela quantidade de dólares.
real = cotacao_dollar * qtd_dollar  

# Formata o valor em reais com 2 casas decimais e separador de milhar como sublinhado.
modeda_real = f"R$ {real:_.2f}"  

# Substitui o ponto por vírgula para adequar à notação monetária brasileira e o sublinhado por ponto.
moeda_real = moeda_real.replace('.',',').replace('_','.')  

# Exibe a quantidade de dólares e o valor correspondente em reais. (Erro de digitação em "dolares")
print(f"$${qtd_dollar} dollars são {moeda_real}")  
