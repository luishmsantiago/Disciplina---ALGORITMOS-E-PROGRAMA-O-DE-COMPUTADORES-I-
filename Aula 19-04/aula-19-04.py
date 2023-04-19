##nome do funcionario, anoNascimento, numero de filhos, rg, salario, ativo. Atribua valores às respectivas variáveis. A variável ativo deverá receber um valor lógico.

from datetime import date
  
def calculateAge(dob):
    today = date.today()
    age = today.year - dob.year -((today.month, today.day) <
         (dob.month, dob.day))
  
    return age

nomeDoFuncionario = "Luis"
anoNascimento = 1993
#idade = 2023-anoNascimento
numeroFilhos = 0
regGeral = "5.863.562"
salario = 3000
ativo = True 

print("O funcionario", nomeDoFuncionario, "com rg", regGeral, "possui", calculateAge(date(1993, 12, 14)), "anos de vida. \n" "O salário do funcionário", nomeDoFuncionario, "é de R$", salario, "e possui", 
numeroFilhos, "filhos.\nSituação ativo:", ativo)
