import yaml
from Networksecurity.exception.exception import NetworkSecurityException
from Networksecurity.logging.logger import logging
import os
import sys
import numpy as np     
import pickle  # No need to import dill if unused

def read_yaml_file(file_path: str) -> dict:
    """Reads a YAML file and returns its contents as a dictionary."""
    try:
        file_path = os.path.abspath(file_path)  # Convert to absolute path

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Schema file not found: {file_path}")

        with open(file_path, "rb") as yaml_file:
            return yaml.safe_load(yaml_file)

    except Exception as e:
        raise NetworkSecurityException(e, sys) 

def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    """Writes data to a YAML file."""
    try: 
        file_path = os.path.abspath(file_path)  # Ensure absolute path
        
        if replace and os.path.exists(file_path):
            os.remove(file_path)  # Remove existing file if replace=True

        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, "w", encoding="utf-8") as file:  # Use UTF-8 encoding
            yaml.dump(content, file)

    except Exception as e:
        raise NetworkSecurityException(e, sys) 
    

def save_numpy_array_data(file_path: str, array: np.array):
    """"
    save numpy array data to file
    file_path: str location of file to save
    array: np.aarray data to save
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path,"wb") as file_obj:
            np.save(file_obj, array)
    except Exception as e:
        raise NetworkSecurityException(e,sys)
    
    
def save_object(file_path: str, obj: object) -> None:
    try:
        logging.info("Entered the save_object method of MainUtils class")
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)
        logging.info("Exited the save_object method of MainUtils class")
    except Exception as e:
        raise NetworkSecurityException(e, sys) from e
