from z_pii.DataTransformer import DataTransformer
from z_pii.params import file_path_dict
import jsonlines
# Path to .txt files in raw_data folder
# FILE_ONE = file_path_dict['FILE_ONE']
FILE_PATH = "tests/test_data_9999-99-99.txt"
# SAVED_FILE_PATH = file_path_dict['SAVED_FILE_PATH']

def test_absence_of_first_name():
    loader_class = DataTransformer(FILE_PATH)
    loader_class.load_transform_data()
    assert 'C_FIRST_NAME' not in loader_class.data[0]

def test_absence_of_last_name():
    loader_class = DataTransformer(FILE_PATH)
    loader_class.load_transform_data()
    assert 'C_LAST_NAME' not in loader_class.data[0]

def test_domain_removed():
    loader_class = DataTransformer(FILE_PATH)
    loader_class.load_transform_data()
    assert 'C_EMAIL_ADDRESS' not in loader_class.data[0]

def test_length_file():
    loader_class = DataTransformer(FILE_PATH)
    loader_class.load_transform_data()

    with jsonlines.open(FILE_PATH) as f:
        raw_data = []
        for data_record in f.iter(): #dictionary
            raw_data.append(data_record)

    assert len(raw_data) == len(loader_class.data)
