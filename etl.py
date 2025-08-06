
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# extraindo os dados
url = 'https://raw.githubusercontent.com/alura-cursos/challenge2-data-science/refs/heads/main/TelecomX_Data.json'

df1 = pd.read_json(url)

# Transformação  - verificando se tem clientes dupliados
df1['customerID'].duplicated().sum()

# normalizando os dados
colunas = list(df1.columns)

# normalizando as colunas
df_colunas = []
for i in colunas[2:]:
    df_colunas.append(pd.json_normalize(df1[i]))


df2 = pd.concat(df_colunas, axis=1)
df = pd.concat([df1['Churn'], df2], axis=1)


# mudar tipos dos dados - bool types
colunas_bool = ['Churn', 'Partner', 'Dependents', 'PhoneService', 'MultipleLines', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 'PaperlessBilling']

for col in colunas_bool:
    df[col] = df[col].astype('bool')

# mudar tipos dos dados - float types

df['Charges.Total'] = df['Charges.Total'].str.replace(',', '.').str.strip().replace('', np.nan)

df['Charges.Total'] = df['Charges.Total'].astype(np.float64)



# criando coluna de contas diárias dos clientes
df['Contas_Diarias'] = (df['Charges.Total'] / 30).round(2)

# Load - Análise descritiva: média (mean), mediana(50%), desvio padrão(std)
colunas_num = ['tenure', 'Charges.Monthly', 'Charges.Total', 'Contas_Diarias']
for col in colunas_num:
    print(df[col].describe())


df['gender'].describe()
# possui mais clientes masculinos - com 3675 clientes

df['PaymentMethod'].describe()
# a maioria dos clientes pagam por eletrônico -  com 2445 freq

df['Contract'].describe()
# a maioria dos clientes possuem contrato mensal - com 4005 freq

df['InternetService'].describe()
# a maioria dos clientes possuem internet de fibra ótica - com 3198 freq

sns.set(style="whitegrid")

# gráfico de evasão - Gráfico de barras
cores2 = ['#66b3ff', '#ff9999']

sns.countplot(data=df, x='Churn', palette=cores2)
plt.title('Distribuição de Churn')
plt.show()


# gráfico de evasão - Gráfico de pizza
cores = ['#66b3ff', '#ff9999']

cont_churn = df['Churn'].value_counts()

plt.figure(figsize=(8,6))
plt.pie(cont_churn, labels=cont_churn.index, autopct='%1.1f%%', startangle=90, colors=cores)
plt.title('Proporção de Churn')
plt.axis('equal')
plt.show()


# Contagem de Evasão por Variáveis Categóricas 
# Gráfico de evasão por gênero
dados = df.groupby(['gender', 'Churn']).size().unstack()

fig, axes = plt.subplots(1, 2, figsize=(12, 6))

cores2 = ['#ff9999','#66b3ff']

for i, genero in enumerate(dados.index):
    valores = dados.loc[genero]
    axes[i].pie(valores, labels=valores.index, autopct='%1.1f%%', startangle=90, colors=cores2)
    axes[i].set_title(f'{genero}')

plt.suptitle('Proporção de Churn por Gênero', fontsize=16)
plt.tight_layout()
plt.show()

df_no_churn = df[df['Churn'] == True]

contagem_no_churn = df_no_churn.groupby('Contract').size().sort_values()

plt.figure(figsize=(10, 7))
plt.barh(contagem_no_churn.index, contagem_no_churn.values, color='#66b3ff')
plt.title('Total de Clientes que evadiram por Tipo de Contrato')
plt.ylabel('Tipo de Contrato')

plt.grid(False)
plt.gca().axes.get_xaxis().set_visible(False)

for bar in plt.gca().patches:
    largura = bar.get_width()
    plt.text(largura + 2, bar.get_y() + bar.get_height()/2,
             f'{int(largura)}', va='center')

plt.tight_layout()
plt.show()


df_churn = df[df['Churn'] == True]

contagem_churn = df_churn.groupby('PaymentMethod').size().sort_values()

plt.figure(figsize=(10, 7))
bars = plt.barh(contagem_churn.index, contagem_churn.values, color='#66b3ff')
plt.title('Total de Clientes que evadiram por Método de Pagamento')
plt.ylabel('Método de Pagamento')
plt.grid(False)
plt.gca().axes.get_xaxis().set_visible(False)

for bar in bars:
    largura = bar.get_width()
    plt.text(largura + 2, bar.get_y() + bar.get_height()/2,
             f'{int(largura)}', va='center')

plt.tight_layout()
plt.show()


df_churn = df[df['Churn'] == True]

contagem_churn = df_churn.groupby('InternetService').size().sort_values()

plt.figure(figsize=(10, 7))
bars = plt.barh(contagem_churn.index, contagem_churn.values, color='#66b3ff')
plt.title('Número de Clientes que evadiram por Tipo de Serviço de Internet')
plt.ylabel('Tipo de Serviço de Internet')
plt.grid(False)
plt.gca().axes.get_xaxis().set_visible(False)


for bar in bars:
    largura = bar.get_width()
    plt.text(largura + 2, bar.get_y() + bar.get_height()/2,
             f'{int(largura)}', va='center')

plt.tight_layout()
plt.show()


# Contagem de Evasão por Variáveis Numéricas
# Boxplot - Total gasto × Churn
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
sns.boxplot(data=df, x='Churn', y='Charges.Total', palette=cores2)
plt.title('Total Gasto por Churn')
plt.ylabel('Total Gasto')
plt.xlabel('Churn')

# Boxplot - Tempo de contrato × Churn
plt.figure(figsize=(7, 5))

sns.boxplot(data=df, x='Churn', y='tenure', palette=cores2)
plt.title('Tempo de Contrato por Churn')
plt.xlabel('Churn')
plt.ylabel('Meses de Contrato')
plt.tight_layout()
plt.show()
