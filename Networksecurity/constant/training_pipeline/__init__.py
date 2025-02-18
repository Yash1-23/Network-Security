
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

"""
    Data  Ingestion related constant start with DATA_INGESTION VAR NAME
    
 """
 
DATA_INGESTION_COLLECTION_NAME : str = "Network_Data"
DATA_INGESTION_DATABASE_NAME : str = "YASHAI"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str ="feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2


# Define and export 'training_pipeline'
training_pipeline = {
    'TARGET_COLUMN': TARGET_COLUMN,
    'PIPELINE_NAME': PIPELINE_NAME,
    'ARTIFACTS_DIR': ARTIFACTS_DIR,
    'FILE_NAME': FILE_NAME,
    'TRAIN_FILE_NAME': TRAIN_FILE_NAME,
    'TEST_FILE_NAME': TEST_FILE_NAME,
    'DATA_INGESTION_COLLECTION_NAME': DATA_INGESTION_COLLECTION_NAME,
    'DATA_INGESTION_DATABASE_NAME': DATA_INGESTION_DATABASE_NAME,
    'DATA_INGESTION_DIR_NAME': DATA_INGESTION_DIR_NAME,
    'DATA_INGESTION_FEATURE_STORE_DIR': DATA_INGESTION_FEATURE_STORE_DIR,
    'DATA_INGESTION_INGESTED_DIR': DATA_INGESTION_INGESTED_DIR,
    'DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO': DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
    
}