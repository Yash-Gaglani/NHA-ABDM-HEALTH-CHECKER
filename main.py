import ReportingUtil
import Util
import config
from AbhaCreation import abha_create_aadhaar
from FeatureHealth import FeatureHealth

if __name__ == '__main__':
    client_id = config.test_data['client_id']
    client_secret = config.test_data['client_secret']
    if Util.is_all_blank(client_id):
        client_id = input("Please provide the ABDM client_id:")
        client_secret = input("Please provide the ABDM client_secret:")
    config.set_client_credentials(client_id, client_secret)

    feature_list: FeatureHealth = []
    feature_list.append(abha_create_aadhaar())

    for feature_health in feature_list:
        print(feature_health)

    ReportingUtil.generate_report(feature_list)



