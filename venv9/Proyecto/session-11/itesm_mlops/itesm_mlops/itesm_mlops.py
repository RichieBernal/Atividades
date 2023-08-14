"""Main module."""
from load.load_data import DataRetriever
from train.train_data import TitanicDataPipeline
import pandas as pd
from sklearn.model_selection import train_test_split
import joblib
import os
from sklearn.metrics import accuracy_score, roc_auc_score

DATASETS_DIR = './data/'
URL = 'C:/Users/rbernal/Documents/GitHub/Rich/mlops/module-2/session-3/activity/Atividades/venv9/Proyecto/session-11/itesm_mlops/itesm_mlops/data/data_fire.csv'
DROP_COLS = None #['boat','body','home.dest','ticket','name']
RETRIEVED_DATA = 'data_fire.csv'


SEED_SPLIT = 404
TRAIN_DATA_FILE = DATASETS_DIR + 'train.csv'
TEST_DATA_FILE  = DATASETS_DIR + 'test.csv'


TARGET = 'STATUS'
FEATURES = ['SIZE','FUEL','DISTANCE','DESIBEL','AIRFLOW','FREQUENCY']
NUMERICAL_VARS = ['SIZE','DISTANCE','DESIBEL','AIRFLOW','FREQUENCY']
CATEGORICAL_VARS = ['FUEL']


NUMERICAL_VARS_WITH_NA = None #['age','fare']
CATEGORICAL_VARS_WITH_NA = None #['cabin','embarked']
NUMERICAL_NA_NOT_ALLOWED = None #[var for var in NUMERICAL_VARS if var not in NUMERICAL_VARS_WITH_NA]
CATEGORICAL_NA_NOT_ALLOWED = None #[var for var in CATEGORICAL_VARS if var not in CATEGORICAL_VARS_WITH_NA]


SEED_MODEL = 404

SELECTED_FEATURES = ['SIZE','FUEL', 'FUEL_gasoline', 'FUEL_lpg', 'FUEL_kerosene',
                     'DISTANCE','DESIBEL','AIRFLOW','FREQUENCY']

TRAINED_MODEL_DIR = './models/'
PIPELINE_NAME = 'logistic_regression'
PIPELINE_SAVE_FILE = f'{PIPELINE_NAME}_output.pkl'


if __name__ == "__main__":
    
    print(os.getcwd())
    os.chdir('C:/Users/rbernal/Documents/GitHub/Rich/mlops/module-2/session-3/activity/Atividades/venv9/Proyecto/session-11/itesm_mlops/itesm_mlops')
    # Retrieve data
    data_retriever = DataRetriever(URL, DATASETS_DIR)
    result = data_retriever.retrieve_data()
    print(result)
    
    # Instantiate the TitanicDataPipeline class
    titanic_data_pipeline = TitanicDataPipeline(seed_model=SEED_MODEL,
                                                numerical_vars=NUMERICAL_VARS, 
                                                categorical_vars_with_na=CATEGORICAL_VARS_WITH_NA,
                                                numerical_vars_with_na=NUMERICAL_VARS_WITH_NA,
                                                categorical_vars=CATEGORICAL_VARS,
                                                selected_features=SELECTED_FEATURES)
    
    # Read data
    df = pd.read_csv(DATASETS_DIR + RETRIEVED_DATA)
    df.head()
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
                                                        df.drop(TARGET, axis=1),
                                                        df[TARGET],
                                                        test_size=0.2,
                                                        random_state=404
                                                   )
    
    
    logistic_regression_model = titanic_data_pipeline.fit_logistic_regression(X_train, y_train)
    
    X_test = titanic_data_pipeline.PIPELINE.fit_transform(X_test)
    y_pred = logistic_regression_model.predict(X_test)
    
    class_pred = logistic_regression_model.predict(X_test)
    proba_pred = logistic_regression_model.predict_proba(X_test)[:,1]
    print(f'test roc-auc : {roc_auc_score(y_test, proba_pred)}')
    print(f'test accuracy: {accuracy_score(y_test, class_pred)}')
    
    # # Save the model using joblib
    save_path = TRAINED_MODEL_DIR + PIPELINE_SAVE_FILE
    joblib.dump(logistic_regression_model, save_path)
    print(f"Model saved in {save_path}")
    