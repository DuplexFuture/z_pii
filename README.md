# Data cleaning
- Document here the project: z_pii
- Description: Python package to clean and remove Personal Identifiable Information (PII) from a .txt file that is in JSON Lines format.
- Data Source: The sample dataset is a subset of the [TPC-DS benchmark](http://www.tpc.org/tpc_documents_current_versions/pdf/tpc-ds_v2.5.0.pdf)
available as sample data in [Snowflake](https://docs.snowflake.com/en/user-guide/sample-data-tpcds.html).
- params.py:
  - ensure params.py has the following format:
  `file_path_dict = {
    "FILE_ONE": "raw_data/path_to_text_file.txt",
    "FILE_TWO": "raw_data/path_to_text_file_2.txt",
    "SAVED_FILE_PATH": "raw_data/path_to_desired_directory/"
    }`


# Startup the project

The initial setup.

Create virtualenv and install the project:
```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv ~/venv ; source ~/venv/bin/activate ;\
    pip install pip -U; pip install -r requirements.txt
```

Unittest test:
```bash
make clean install test
```

Check for z_pii in gitlab.com/{group}.
If your project is not set please add it:

- Create a new project on `gitlab.com/{group}/z_pii`
- Then populate it:

```bash
##   e.g. if group is "{group}" and project_name is "z_pii"
git remote add origin git@github.com:{group}/z_pii.git
git push -u origin master
git push -u origin --tags
```

Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
z_pii-run
```

# Install

Go to `https://github.com/{group}/z_pii` to see the project, manage issues,
setup you ssh public key, ...

Create a python3 virtualenv and activate it:

```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv -ppython3 ~/venv ; source ~/venv/bin/activate
```

Clone the project and install it:

```bash
git clone git@github.com:{group}/z_pii.git
cd z_pii
pip install -r requirements.txt
make clean install test                # install and test
```
Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
z_pii-run
```
