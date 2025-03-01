
import os
import sys
import numpy as np 
import pandas as pd


"""
  defining common constant for the training pipline

"""

TARGET_COLUMN = "Result"
PIPELINE_NAME: str = "NetworkSecurity"
ARTIFACTS_DIR: str = "Artifacts"
FILE_NAME :str = "phising_Data.csv"


TRAIN_FILE_NAME : str = "train.csv"
TEST_FILE_NAME :  str = "test.csv"

SCHEMA_FILE_PATH = os.path.join("data_schema", "schema.yml")

SAVED_MODEL_DIR = os.path.join("saved_models")
MODEL_FILE_NAME = "model.pkl"


"""
    Data  Ingestion related constant start with DATA_INGESTION VAR NAME
    
 """
 
DATA_INGESTION_COLLECTION_NAME : str = "Network_Data"
DATA_INGESTION_DATABASE_NAME : str = "YASHAI"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str ="feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2

    
    
"""
Data validation related constant start with DATA_VALIDATION  VAR NAME
  
"""
  
DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_VALID_DIR: str = "validated"
DATA_VALIDATION_INVALID_DIR: str = "invalid"
DATA_VALIDAITON_DRIFT_REPORT_DIR: str = "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME: str = "report.yml"
PREPROCESSING_OBJECT_FILE_NAME : str ="preprocessing.pkl"


"""
Data Transformation related constant start with DATA_TRANSFORMATION VAR NAME
"""

DATA_TRANSFORMATION_DIR_NAME : str = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR: str = "transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR:str = "transformed_object"

## KNN imputer to replace nan values
DATA_TRANSFORMATION_IMPUTER_PARAMS:dict ={
  "missing_values" : np.nan,
  "n_neighbors":3,
  "weights":"uniform",
}

DATA_TRASNFORMATION_TRAIN_FILE_PATH : str = "train.py"

DATA_TRANSFORMATON_TEST_FILE_PATH: str = "test.py"

"""
Model Trainer related constant start with MODE TRAINER VAR NAME
"""

MODEL_TRAINER_DIR_NAME : str ="model_trainer"
MODEL_TRAINER_TRAINED_MODEL_DIR: str = "trained_model"
MODEL_TRAINER_TRAINED_MODEL_NAME: str = "model.pkl"
MODEL_TRIANER_EXCEPTED_SCORE: float = 0.6
MODEL_TRAINER_OVER_FITTING_UNDER_FITTING_THRESHOLD: float =0.05
