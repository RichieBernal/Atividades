"""Main module."""
from load.load_data import DataRetriever
from train.train_data import TitanicDataPipeline
import pandas as pd
from sklearn.model_selection import train_test_split
import joblib
import os
from sklearn.metrics import accuracy_score, roc_auc_score
from google.colab import drive
drive.mount('/content/drive')
            
DATASETS_DIR = './data/'
URL = 'C:\Users\rbernal\Documents\GitHub\Rich\mlops\module-2\session-3\activity\Atividades\venv9\Proyecto\cookie_test\data\retrieved_data.csv'
RETRIEVED_DATA = 'retrieved_data.csv'


SEED_SPLIT = 404
TRAIN_DATA_FILE = DATASETS_DIR + 'train.csv'
TEST_DATA_FILE  = DATASETS_DIR + 'test.csv'

TARGET  = 'STATUS'
FEATURES = ['SIZE','FUEL','DISTANCE','DESIBEL','AIRFLOW','FREQUENCY']
CATEGORICAL_VARS = ['FUEL']
NUMERICAL_VARS = ['SIZE','DISTANCE','DESIBEL','AIRFLOW','FREQUENCY']

SEED_MODEL = 404

TRAINED_MODEL_DIR = './models/'
PIPELINE_NAME = 'xgboost'
PIPELINE_SAVE_FILE = f'{PIPELINE_NAME}_output.pkl'
