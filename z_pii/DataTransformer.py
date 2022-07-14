import jsonlines
import re
from z_pii.params import file_path_dict

# Path to .txt files in raw_data folder
FILE_ONE = file_path_dict['FILE_ONE'] # path to file to transform  e.g., "raw_data/..."
FILE_TWO = file_path_dict['FILE_TWO']
SAVED_FILE_PATH = file_path_dict['SAVED_FILE_PATH'] # path to directory to save transformed data e.g., "raw_data/..."

class DataTransformer():

    def __init__(self, file_path):
        self.file_path = file_path

    def load_transform_data(self):
        """
        Load data from .txt file that is off jsonline format.
        Read and apply transformations to data and store each record in a list.
        """
        with jsonlines.open(self.file_path) as f:
            self.data = []
            for data_record in f.iter():
                data_record = self.remove_name(data_record)
                data_record = self.retreive_domain(data_record)
                self.data.append(data_record)

    def remove_name(self, data_record):
        """
        Accepts a dict representing one data record from input file.
        Returns a 'cleaned' dict:
            - remove first name
            - remove second name
            - possible to remove other features such as 'C_SALUTATION' if desired
        """
        keys_to_remove = ['C_FIRST_NAME', 'C_LAST_NAME']

        return {key: val for key, val in data_record.items() if key not in keys_to_remove}

    def retreive_domain(self, data_record):
        """
        Accepts a dict representing one data record from input file.
        Returns a 'cleaned' dict:
            - remove PII of email address
            - retreive and store email domain in new key, value pair
        """
        key_to_remove = ['C_EMAIL_ADDRESS']
        try:
            data_record['C_EMAIL_DOMAIN'] = data_record['C_EMAIL_ADDRESS'].split('@')[1]
        except:
            # If email information is not present, fill value with None
            data_record['C_EMAIL_DOMAIN'] = None

        return {key: val for key, val in data_record.items() if key not in key_to_remove}

    def write_to_file(self, saved_file_path):
        regex = r"\d{4}-\d{2}-\d{2}"
        file_name = re.search(regex, self.file_path).group(0) # looks for 'YYYY-MM-DD' format

        with jsonlines.open(file=f"{saved_file_path + file_name}-TRANSFORMED.txt", mode='w') as f:
            for record in self.data:
                f.write(record)

if __name__ == "__main__":

    data_transformer = DataTransformer(FILE_ONE)
    data_transformer.load_transform_data()
    data_transformer.write_to_file(SAVED_FILE_PATH)

    data_transformer_2 = DataTransformer(FILE_TWO)
    data_transformer_2.load_transform_data()
    data_transformer_2.write_to_file(SAVED_FILE_PATH)
