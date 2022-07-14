from z_pii.DataTransformer import DataTransformer
import jsonlines

# Path to .txt files in tests folder
FILE_PATH = "tests/test_data_9999-99-99.txt"

# Load in test data and transform using DataTransformer class
loader_class = DataTransformer(FILE_PATH)
loader_class.load_transform_data()

# Test functions
def test_absence_of_first_name():
    """
    Ensure C_FIRST_NAME field has been removed from each record.
    """
    for record in loader_class.data:
        assert 'C_FIRST_NAME' not in record

def test_absence_of_last_name():
    """
    Ensure C_LAST_NAME field has been removed from each record.
    """
    for record in loader_class.data:
        assert 'C_LAST_NAME' not in record

def test_email_removed():
    """
    Ensure that PII of email address is removed from each record.
    """
    for record in loader_class.data:
        assert 'C_EMAIL_ADDRESS' not in record

def test_domain_saved():
    """
    Ensure that email domain is saved in own field fore each record.
    """
    for record in loader_class.data:
        assert 'C_EMAIL_DOMAIN' in record

def test_length_file():
    """
    Ensure all no data leakage by checking that the number of records before and
    after transformation are equal.
    """
    with jsonlines.open(FILE_PATH) as f:
        raw_data = []
        for data_record in f.iter(): #dictionary
            raw_data.append(data_record)
    assert len(raw_data) == len(loader_class.data)

# if __name__ == "__main__":
#     test_absence_of_first_name()
