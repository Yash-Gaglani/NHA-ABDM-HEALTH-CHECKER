import json


def load_json_file(file_path):
    with open(file_path, 'r') as json_file:
        return json.load(json_file)


test_data = load_json_file('test_data.json')

config_data = {
    "client_id": "",
    "client_secret": "",
    "mongo_db_url": "mongodb://localhost:27017/mydatabase",
    "abdm_gateway_url": "https://dev.abdm.gov.in/gateway",
    "abdm_cm_url": "https://dev.abdm.gov.in/cm",
    "abdm_abha_url": "https://healthidsbx.abdm.gov.in/api",
    "abdm_phr_url": "https://phrsbx.abdm.gov.in/api"
}

# Configuration data
# config_data = load_config('config.json')

client_id = config_data.get('client_id', '')
client_secret = config_data.get('client_secret', '')
mongo_db_url = config_data.get('mongo_db_url', '')
abdm_gateway_url = config_data.get('abdm_gateway_url', '')
abdm_cm_url = config_data.get('abdm_cm_url', '')
abdm_abha_url = config_data.get('abdm_abha_url', '')
abdm_phr_url = config_data.get('abdm_phr_url', '')


def set_client_credentials(new_client_id, new_client_secret):
    global client_id, client_secret
    client_id = new_client_id
    client_secret = new_client_secret

