import requests
import json
import config
from ApiCall import ApiCall
import pandas as pd

abdm_api_list = pd.read_csv('abdm_api_list.csv')


def do_api_call(api_call: ApiCall):
    try:
        response = None
        url = api_call.baseurl + api_call.endpoint
        headers = {'Content-Type': 'application/json'}
        if api_call.request_headers:
            headers = {**headers, **api_call.request_headers}
        api_call.request_headers = headers
        json_data = api_call.request_body
        params = api_call.request_params

        if api_call.method == "GET":
            response = requests.get(url=url, headers=headers, params=params)
        if api_call.method == "POST":
            response = requests.post(url=url, json=json_data, headers=headers, params=params)

        if response is not None:
            api_call.response_status = response.status_code
            api_call.response_headers = response.headers
            api_call.response_body = response.text

    except requests.exceptions.RequestException as e:
        print("Request Exception:", e)

    return api_call


def get_abdm_api_scheme(api_name: str):
    api = abdm_api_list[abdm_api_list['api_name'] == api_name].iloc[0]
    api_call = ApiCall()
    base_url = api['base_url']
    if base_url.startswith("{{") and base_url.endswith("}}"):
        base_url = base_url.replace('{{', '').replace('}}', '')
        base_url = config.config_data[base_url]
    api_call.baseurl = base_url
    api_call.endpoint = api['endpoint']
    api_call.method = api['method']
    if isinstance(api['request_params'], str) and api['request_params'].strip() != "":
        api_call.request_params = json.loads(api['request_params'])
    if isinstance(api['request_body'], str) and api['request_body'].strip() != "":
        api_call.request_body = json.loads(api['request_body'])
    if isinstance(api['request_headers'], str) and api['request_headers'].strip() != "":
        api_call.request_headers = json.loads(api['request_headers'])
    return api_call


def get_abdm_session():
    api_call = get_abdm_api_scheme('abdm_session')
    body = api_call.request_body
    body['clientId'] = config.client_id
    body['clientSecret'] = config.client_secret
    api_call.request_body = body
    api_call = do_api_call(api_call)
    return api_call


def is_all_blank(value: str):
    return value is None or value.strip() == ""
