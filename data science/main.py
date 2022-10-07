import pandas as pd

sales_df = pd.read_excel("dataframes/Vendas.xlsx")
sales_df__december = pd.read_excel("dataframes/Vendas - Dez.xlsx")
#sales_df = sales_df.concat(sales_df__december)
#o método concat substituiu o append
pd.concat([sales_df,sales_df__december])
sales_df['Comissão'] = sales_df['Valor Final'] * 0.05
transations_df = sales_df['ID Loja'].value_counts()
#transations_df.to_excel('dfOutput/transacoes.xlsx')