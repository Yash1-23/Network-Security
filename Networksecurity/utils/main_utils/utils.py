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
        raise NetworkSecurityException(e, sys) from e

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
        raise NetworkSecurityException(e, sys) from e
