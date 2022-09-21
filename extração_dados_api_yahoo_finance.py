import yfinance as yf
import pandas as pd
import os
import re

#procura por arquivo que termina com '.xlsx'
for root, dirs, files in os.walk('/home/krijs/Área de Trabalho/Henrique/analise'):
    for file in files:
        if file.endswith('.xlsx'):
            name = os.path.join(root, file)
#----------pega data atual--------------#
day = '01'
#descobre o ano de referência do arquivo
find_year = re.findall('[0-9]+', name)
year = ''.join(find_year)#transformar lista em string

#identifica o mês de referência do arquivo
if (re.findall(r"Janeiro", name)): mes = '01'
elif (re.findall(r"Fevereiro", name)): mes = '02'
elif (re.findall(r"Março", name)): mes = '03'
elif (re.findall(r"Abril", name)): mes = '04'
elif (re.findall(r"Maio", name)): mes = '05'
elif (re.findall(r"Junho", name)): mes = '06'
elif (re.findall(r"Julho", name)): mes = '07'
elif (re.findall(r"Agosto", name)): mes = '08'
elif (re.findall(r"Setembro", name)): mes = '09'
elif (re.findall(r"Outubro", name)): mes = '10'
elif (re.findall(r"Novembro", name)): mes = '11'
elif (re.findall(r"Dezembro", name)): mes = '12'

#tcriando string de comparação dentro do iloc
data = [year, mes, day]
merge = '-'.join(data)
#print(merge)
#------------------taxas e indices------------------#
def consulta_bcb(codigo_bcb):
    url = 'http://api.bcb.gov.br/dados/serie/bcdata.sgs.{}/dados?formato=json'.format(codigo_bcb)
    df = pd.read_json(url)
    df['data'] = pd.to_datetime(df['data'], dayfirst=True)
    return df

zero = pd.DataFrame()
one = pd.DataFrame()
two = pd.DataFrame()
three = pd.DataFrame()
four = pd.DataFrame()
a = consulta_bcb(4390)#Selic
b = consulta_bcb(433)#IPCA
c = consulta_bcb(189)#IGP-M
d = consulta_bcb(4391)#CDI
e = consulta_bcb(7811)#TR
zero = a
one = b
two = c
three = d
four = e

bola = zero.merge(one, on='data')
dog = bola.merge(two, on='data')
cash = dog.merge(three, on='data')
yen = cash.merge(four, on='data')
yen.columns = ["Data", "Selic", "IPCA", "IGP-M", "CDI", "TR"]
#print("Base de dados: API BCB")
yun = (yen[yen["Data"] == merge])
print(yun)
#----------------------------commodities e bolsas----------------------#
tick = 'GC=F ^BVSP ^DJI ^IXIC CL=F'
bd_y = yf.download(tick, period='5y', interval='1mo', actions=False, rounding=True)[["Open", "Adj Close"]]
dfn = bd_y
hyf = (((dfn["Adj Close"] - dfn["Open"]) * 100)/dfn["Open"])

hyf.columns = ["Óleo Cru (Futuro)", "Ouro (Futuro)", "IBOVESPA (Delayed Price)", "DJI (Real Time Price)", "Nasdaq GIDS Real Time Price"]
bou = hyf.reset_index()
baw = (bou[bou["Date"] == merge])
print(baw)
'''
bh = selic_mensal.reset_index()
bh.columns = ["DATA", "MARGEM"]
NEW = bh

print(NEW[NEW["DATA"] == merge])
'''
#------------------------salvar em pdf----------------------#
'''
fig, ax = plt.subplots(figsize = (12, 4))
ax.axis('tight')
ax.axis('off')
the_table = ax.table(cellText = yen.values, colLabels = yen.columns, loc = 'center')


pp = PdfPages("1.pdf")
pp.savefig(fig, bbox_inches='tight')
pp.close()
'''