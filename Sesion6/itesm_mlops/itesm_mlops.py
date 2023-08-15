"""Main module."""
from load.load_data import DataRetriever
from train_.train_data import TitanicDataPipeline
import pandas as pd
from sklearn.model_selection import train_test_split
import joblib

DATASETS_DIR = 'datasets/'
URL = 'C:\Users\rbernal\Documents\GitHub\Rich\mlops\module-2\session-3\activity\Atividades\venv9\cookie_test\itesm_mlops\data\retrieved_data.csv'
DROP_COLS = None
#DROP_COLS = ['boat','body','home.dest','ticket','name']
RETRIEVED_DATA = 'retrieved_data.csv'


SEED_SPLIT = 404
TRAIN_DATA_FILE = f'{DATASETS_DIR}train.csv'
TEST_DATA_FILE = f'{DATASETS_DIR}test.csv'


TARGET = 'STATUS'
FEATURES = ['SIZE','FUEL','DISTANCE','DESIBEL','AIRFLOW','FREQUENCY','STATUS']
NUMERICAL_VARS = ['DISTANCE','DESIBEL','AIRFLOW','FREQUENCY']
CATEGORICAL_VARS = ['FUEL']



NUMERICAL_VARS_WITH_NA = None
CATEGORICAL_VARS_WITH_NA = None
NUMERICAL_NA_NOT_ALLOWED = [var for var in NUMERICAL_VARS if var not in NUMERICAL_VARS_WITH_NA]
CATEGORICAL_NA_NOT_ALLOWED = [var for var in CATEGORICAL_VARS if var not in CATEGORICAL_VARS_WITH_NA]

SEED_MODEL = 404


TRAINED_MODEL_DIR = 'trained_models/'
PIPELINE_NAME = 'logistic_regression'
PIPELINE_SAVE_FILE = f'{PIPELINE_NAME}_output.pkl'


if __name__ == "__main__":
    # Retrieve data
    data_retriever = DataRetriever(URL)
    result = data_retriever.retrieve_data()
    print(result)
    
    # Create Titanic pipeline
    
    # Instantiate the TitanicDataPipeline class
    titanic_data_pipeline = TitanicDataPipeline(seed_model=SEED_MODEL)
    # Create the pipeline
    titanic_pipeline = titanic_data_pipeline.create_pipeline()
    
    # Read data
    df = pd.read_csv(DATASETS_DIR + RETRIEVED_DATA)
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
                                                        df.drop(TARGET, axis=1),
                                                        df[TARGET],
                                                        test_size=0.2,
                                                        random_state=404
                                                   )
    
    # Fit the model
    titanic_pipeline.fit(X_train, y_train)
    
    
    # Persist/Save model
    save_file_name = f'{PIPELINE_SAVE_FILE}'
    save_path = TRAINED_MODEL_DIR + save_file_name

    result = joblib.dump(titanic_pipeline, save_path)
    print(f"Model saved in {result}")
    
    file_path = TRAINED_MODEL_DIR + PIPELINE_SAVE_FILE
    trained_model = joblib.load(filename=file_path)
    new_data = prueba = '{"SIZE":1,"FUEL":"gasoline","DISTANCE":10,"DESIBEL":96,"AIRFLOW":0,"FREQUENCY":75}'
    predictions = trained_model.predict(new_data)
    print(f"The prediction is: {predictions}")