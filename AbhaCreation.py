import json
import time

import Util
import config
from ApiCall import ApiCall
from FeatureHealth import FeatureHealth


def abha_create_aadhaar():
    feature_health = FeatureHealth()
    feature_health.feature = "ABHA creation with AADHAAR (Pre-Verified)"

    # 1. abdm session
    session = Util.get_abdm_session()
    feature_health.add_api_call(session)
    if session.response_status != 200:
        feature_health.status = FeatureHealth.FAILING
        return feature_health
    access_token = 'Bearer ' + json.loads(session.response_body)['accessToken']

    # 2. generate aadhaar otp
    aadhaar = config.test_data['test_aadhaar_no']
    if Util.is_all_blank(aadhaar):
        aadhaar = str(input("Please input your aadhaar:"))
    api_call = Util.get_abdm_api_scheme('v1_reg_generate_aadhaar_otp')
    body = api_call.request_body
    body['aadhaar'] = aadhaar
    api_call.request_body = body
    api_call.request_headers = {'Authorization': access_token}
    api_call = Util.do_api_call(api_call)
    feature_health.add_api_call(api_call)
    if api_call.response_status != 200:
        feature_health.status = FeatureHealth.FAILING
        return feature_health

    # 3. resend aadhaar otp
    time.sleep(40)
    txn_id = json.loads(api_call.response_body)['txnId']
    resend_call = Util.get_abdm_api_scheme('v1_reg_resend_aadhaar_otp')
    body = resend_call.request_body
    body['txnId'] = txn_id
    resend_call.request_body = body
    resend_call.request_headers = {'Authorization': access_token}
    resend_call = Util.do_api_call(resend_call)
    feature_health.add_api_call(resend_call)
    if resend_call.response_status != 200:
        feature_health.status = FeatureHealth.FAILING
        return feature_health

    # 4. verify aadhaar otp
    otp = str(input("Please input aadhaar OTP:"))
    verify_otp = Util.get_abdm_api_scheme('v1_reg_verify_aadhaar_otp')
    body = verify_otp.request_body
    body['txnId'] = txn_id
    body['otp'] = otp
    verify_otp.request_body = body
    verify_otp.request_headers = {'Authorization': access_token}
    verify_otp = Util.do_api_call(verify_otp)
    feature_health.add_api_call(verify_otp)
    if verify_otp.response_status != 200:
        feature_health.status = FeatureHealth.FAILING
        return feature_health

    # 5. create health_id with pre verified
    pre_verified = Util.get_abdm_api_scheme('v1_reg_create_hid_pre_verified')
    body = pre_verified.request_body
    body['txnId'] = txn_id
    pre_verified.request_body = body
    pre_verified.request_headers = {'Authorization': access_token}
    pre_verified = Util.do_api_call(pre_verified)
    feature_health.add_api_call(pre_verified)
    if pre_verified.response_status != 200:
        feature_health.status = FeatureHealth.FAILING
        return feature_health

    feature_health.status = FeatureHealth.PASSING
    return feature_health
