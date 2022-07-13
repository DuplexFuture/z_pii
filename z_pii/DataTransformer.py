import jsonlines
import re
from params import file_path_dict

# Path to .txt files in raw_data folder
FILE_ONE = file_path_dict['FILE_ONE']
FILE_TWO = file_path_dict['FILE_TWO']
SAVED_FILE_PATH = file_path_dict['SAVED_FILE_PATH']

class DataTransformer():

    def __init__(self, file_path):
        self.file_path = file_path

    def load_transform_data(self):
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
            - remove salutation (optional - may remove)
        """

        keys_to_remove = ['C_FIRST_NAME', 'C_LAST_NAME', 'C_SALUTATION']

        return {key: val for key, val in data_record.items() if key not in keys_to_remove}

    def retreive_domain(self, data_record):
        """
        Accepts a dict representing one data record from input file.
        Returns a 'cleaned' dict:
            - remove PII of email address
            - retreive and store email domain in new key
        """

        key_to_remove = ['C_EMAIL_ADDRESS']
        try:
            data_record['C_EMAIL_DOMAIN'] = data_record['C_EMAIL_ADDRESS'].split('@')[1]
        except:
            data_record['C_EMAIL_DOMAIN'] = None

        return {key: val for key, val in data_record.items() if key not in key_to_remove}

    def write_to_file(self, saved_file_path):
        regex = "\d{4}-\d{2}-\d{2}"
        file_name = re.search(regex, self.file_path).group(0) # looks for '2021-01-11'

        with jsonlines.open(file=f"{saved_file_path + file_name}-TRANSFORMED.txt", mode='w') as f:
            for record in self.data:
                f.write(record)




if __name__ == "__main__":

    data_transformer = DataTransformer(FILE_ONE)
    data_transformer.load_transform_data()
    data_transformer.write_to_file(SAVED_FILE_PATH)
