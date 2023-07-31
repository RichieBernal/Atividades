import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

# Crear custom transformer

class MissingIndicator(BaseEstimator, TransformerMixin):

    def __init__(self, variables):
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables

    def fit(self, X, y):
        return self

    def transform(self, X):
        # TODO: Put your code here
        for var in self.variables:
            if pd.api.types.is_numeric_dtype(X[var]):
                new_var = var + "_nan"
                X[new_var] = pd.isna(X[var]).astype("int8")
 

        return X
#X[new_col] = X[var].isna().astype("bool")

# Leer el csv sin aplicar transformaciones
df = pd.read_csv("mlops/module-2/session-6/activity/raw-data.csv")

# Imprimir los primeros datos
print(df.head(10))

mi = MissingIndicator(variables=["pclass", "age", "sibsp", "parch", "fare"])
# Aplicar las transformaciones
df_mi = mi.transform(df)

# Imprimir resultados despues de las transformaciones
print(df_mi.head(20))