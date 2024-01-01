import os
import logging
import json
from datetime import datetime
import hashlib
import time

def setup_logger(log_name, log_file, level=logging.INFO):
    """Function to set up a logger"""
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

    handler = logging.FileHandler(log_file)        
    handler.setFormatter(formatter)

    logger = logging.getLogger(log_name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

def read_json(file_path):
    """Function to read a JSON file"""
    with open(file_path, 'r') as file:
        return json.load(file)

def write_json(data, file_path):
    """Function to write a JSON file"""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def create_directory(dir_path):
    """Function to create a directory if it doesn't exist"""
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

def current_timestamp():
    """Function to get the current timestamp"""
    return datetime.now().strftime("%Y%m%d-%H%M%S")

def divider1(dividertext1='*='):
    """Function to print a divider"""
    print(f'{dividertext1}'*20)

def calculate_md5(file_path):
    """Function to calculate the MD5 checksum of a file"""
    with open(file_path, 'rb') as file:
        data = file.read()
        md5_checksum = hashlib.md5(data).hexdigest()
    return md5_checksum

def time_execution(function):
    """Decorator to measure the execution time of a function"""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = function(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f'Executed {function.__name__} in {execution_time} seconds')
        return result
    return wrapper

def safe_division(x, y):
    """Function to safely divide two numbers"""
    try:
        result = x / y
    except ZeroDivisionError:
        print("Error: Division by zero.")
        result = None
    return result

def cal_percentage(n1, n2):
    """Function to calculate the percentage of two numbers"""
    return round((n1 / n2) * 100, 2)

