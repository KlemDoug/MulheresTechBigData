#INTEGRAÇÃO PANDAS + MYSQL
#
#(NO TERMINAL)
#pip install sqlalchemy pymysql
#
#(código no arquivo .py)
#
from sqlalchemy import create_engine
import pandas as pd

host='localhost'

user='root'

password='senac%40123'

database='mulherestech'

engine=create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

df=pd.read_sql('alunos',con=engine)
print(df)

#ATIVIDADE (github):

#Crie mais duas tabelas (sugestão: 'cursos' e 'filiais') no mesmo banco de dados
#onde você criou 'alunos' e 'professores'. Façam mais características para essas tabelas (ao menos 5)
#e criem, pelo menos, 10 injeções de dados para as novas tabelas e 1 consulta para cada uma delas. 
# No final, peça (no VSCode) para que o Pandas leia cada tabela nova que foi criada.