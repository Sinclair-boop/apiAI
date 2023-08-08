# %%
import os

# %%
os.listdir("../../../../../../Downloads/Mobile-money-fraud-detection-main")

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# %% [markdown]
# # Importer la donnée

# %%
df = pd.read_csv('../../../../../../Downloads/Mobile-money-fraud-detection-main/archive.zip')

# %%
df.head()

# %%
df.shape

# %%
df.info()

# %%
df.describe()

# %%
24*31

# %%
df['step'].max()

# %%
df.isnull().sum().any()

# %%
df['isFraud'].value_counts()

# %%
(df['isFraud'].value_counts() / len(df)) * 100

# %%
sns.countplot(df['isFraud'])

# %%
df.amount.min(), df.amount.max()

# %% [markdown]
# # Analyse exploratoire des données

# %% [markdown]
# ## Investiguons isFlaggedFraud

# %%
df['isFlaggedFraud'].value_counts()

# %%
df[df['isFlaggedFraud'] == 1].amount.min(), df[df['isFlaggedFraud'] == 1].amount.max()

# %%
df[df['isFlaggedFraud'] == 0].amount.min(), df[df['isFlaggedFraud'] == 0].amount.max()

# %% [markdown]
# ## Type de transactions

# %%
df['type'].value_counts()

# %% [markdown]
# Deux types de clients:
# * clients normaux
# * marchands

# %%
sns.countplot(df['type'])


# %%
df.groupby(['type', 'isFraud']).size()

# %%
data = df[df['type'].isin(['CASH_OUT', 'TRANSFER'])].reset_index(drop=True)

# %%
len(df), len(data)

# %%
sns.catplot(data=data, x='isFraud', y='amount', col='type')
plt.show()

# %% [markdown]
# ## Marchands

# %%
data.columns

# %%
data[data['nameDest'].str.startswith('M')]

# %%
data[data['nameOrig'].str.startswith('M')]

# %% [markdown]
# ## FRaud = transfert + cashout ?

# %%
fraud = data[data["isFraud"] == 1]

# %%
fraud[fraud['type'] == 'TRANSFER'].nameDest.isin(fraud[fraud['type'] == 'CASH_OUT'].nameOrig).any()

# %%
data.sample(5)

# %%
data['type'].value_counts()

# %% [markdown]
# ## Initiateur n'a pas d'argent

# %%
data[data['oldbalanceOrg'] == 0]

# %%
data[data['oldbalanceOrg'] == 0].isFraud.value_counts()

# %%
data['oldbalanceOrgMissing'] = (data['oldbalanceOrg'] == 0)

# %%
data[data['newbalanceDest'] == 0].isFraud.value_counts()

# %%
data['newbalanceDestMissing'] = (data['newbalanceDest'] == 0)

# %%
data.head()

# %% [markdown]
# ## Verifions

# %%
data['newbalanceOrig'] = data['oldbalanceOrg'] - data['amount']
data['newbalanceDest'] = data['oldbalanceDest'] + data['amount']

# %%
data['errorOrig'] = data['newbalanceOrig'] - (data['oldbalanceOrg'] - data['amount'])
data['errorDest'] = data['newbalanceDest'] - (data['oldbalanceDest'] + data['amount'])

# %%
data[['errorOrig', 'errorDest']].describe()

# %% [markdown]
# ## Matrice de correlation

# %%
corr = data.corr()
sns.heatmap(corr, annot=True, cmap='YlGnBu')

# %%
corr = data.corr()
sns.heatmap(corr[['isFraud']], annot=True, cmap='YlGnBu')

# %% [markdown]
# # Modeling

# %%
X = data.drop(['step', 'nameOrig', 'nameDest', 'isFlaggedFraud', 'isFraud'], axis=1)
y = data['isFraud']

# %%
X['type'] = X['type'].map({'TRANSFER': 0, 'CASH_OUT': 1})

# %%
X['type'].value_counts()

# %% [markdown]
# ## Traintest split

# %%
from sklearn.model_selection import train_test_split

# %%
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.2, random_state=42)

# %%
y_train.value_counts()/ len(y_train)

# %%
y_test.value_counts()/ len(y_test)

# %% [markdown]
# ## Gradient Boosting Machine

# %%
import xgboost as xgb

# %%
clf = xgb.XGBClassifier(max_depth=3, n_jobs=-1)

# %%
clf.fit(X_train, y_train)

# %%
from sklearn.metrics import f1_score, precision_score, recall_score, confusion_matrix

# %%
y_pred = clf.predict(X_test)

# %%
y_pred

# %%
precision_score(y_pred, y_test)

# %%
recall_score(y_pred, y_test)

# %%
f1_score(y_pred, y_test)

# %%
confusion_matrix(y_pred, y_test)

# %%
from xgboost import to_graphviz

# %%
to_graphviz(clf, rankdir='LR')

# %%



