import pymysql
import numpy as np 
import matplotlib.pyplot as plt

#Conexão com o banco de dados
try:
    link = pymysql.connect(host="127.0.0.1", user="root", password="654321", db="fpmmrsape")

except:
    print("Conexão não estabelecida com a base de dados.")

#Executar as consultas
try:
    with link.cursor() as c:
        
        sql = "select sum(valor) from transferencias group by ano order by ano"
        c.execute(sql)
        valor = c.fetchall()

        sqlano = "select distinct ano from transferencias"
        c.execute(sqlano)
        ano = c.fetchall()

except:
    print("Erro de consulta.")

#Montando os gráficos
try:
    plt.plot(ano, valor, label ='Total de transferencias recebidas na região')
    plt.legend()
    plt.title("Transferencias")
    plt.show()
    '''
    fig =  plt.figure()
    ax1= fig.add_subplot(2,1,1)
    ax1.plot(ano,valor, label='Total de tansferencias para a região')
    '''
except:
    print("Erro na criação dos gráficos")

finally:
    link.close()
    print("Fim do programa")