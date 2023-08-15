from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.compose import ColumnTransformer
from preprocess.preprocess_data import (
    MissingIndicator,
    ExtractLetters,
    CategoricalImputer,
    NumericalImputer,
    RareLabelCategoricalEncoder,
    OneHotEncoder,
    OrderingFeatures
)

class FireDataPipeline:
    """
    A class representing the Titanic data processing and modeling pipeline.

    Attributes:
        NUMERICAL_VARS (list): A list of numerical variables in the dataset.
        CATEGORICAL_VARS_WITH_NA (list): A list of categorical variables with missing values.
        NUMERICAL_VARS_WITH_NA (list): A list of numerical variables with missing values.
        CATEGORICAL_VARS (list): A list of categorical variables in the dataset.
        SEED_MODEL (int): A seed value for reproducibility.

    Methods:
        create_pipeline(): Create and return the Titanic data processing pipeline.
    """
    
    def __init__(self, seed_model):
        self.SEED_MODEL = seed_model
    
    def create_pipeline(self):
        """
        Create and return the Titanic data processing pipeline.

        Returns:
            Pipeline: A scikit-learn pipeline for data processing and modeling.
        """
        return Pipeline(
            [
                (
                    'missing_indicator',
                    MissingIndicator(variables=self.NUMERICAL_VARS),
                ),
                ('cabin_only_letter', ExtractLetters()),
                (
                    'categorical_imputer',
                    CategoricalImputer(variables=self.CATEGORICAL_VARS_WITH_NA),
                ),
                (
                    'median_imputation',
                    NumericalImputer(variables=self.NUMERICAL_VARS_WITH_NA),
                ),
                (
                    'rare_labels',
                    RareLabelCategoricalEncoder(
                        tol=0.05, variables=self.CATEGORICAL_VARS
                    ),
                ),
                ('dummy_vars', OneHotEncoder(variables=self.CATEGORICAL_VARS)),
                ('aligning_feats', OrderingFeatures()),
                ('scaling', MinMaxScaler()),
                (
                    'log_reg',
                    LogisticRegression(
                        C=0.0005,
                        class_weight='balanced',
                        random_state=self.SEED_MODEL,
                    ),
                ),
            ]
        )