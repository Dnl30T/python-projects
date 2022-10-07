import pandas as pd

sales_df = pd.read_excel("Vendas.xlsx")

#Mostrar a tabela no console

#print(sales_df)
#print(sales_df.head(5))
#print(sales_df.shape)
#print(sales_df.describe())

#Manipular exibição da tabela

#print(sales_df[['Produto','ID Loja']])
#print(sales_df.loc[99:104])
#print(sales_df.loc[sales_df['ID Loja'] == 'Shopping Morumbi'])

sales_df__cueca = sales_df.loc[sales_df['Produto'] == 'Cueca',["ID Loja","Quantidade","Produto"]]
sales_df__morumbi_cueca = sales_df__cueca.loc[sales_df__cueca['ID Loja']=='Rio Mar Recife']
#print(sales_df__morumbi_cueca)
#sales_df__morumbi_cueca.to_excel('cueca.xlsx')