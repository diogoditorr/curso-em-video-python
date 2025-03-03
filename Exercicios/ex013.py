# Calcula o valor do salário com 15% de aumento

wage = float(input('Qual é o salário do funcionário? R$ '))
new_wage = wage + (wage*15/100)

print(f'Um funcionário que ganhava R${wage}, com 15% de aumento, passa a receber R${new_wage:.2f}')