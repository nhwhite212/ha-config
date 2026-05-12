import logging
logging.basicConfig(level=logging.DEBUG)

from pykumo.py_kumo_cloud_account_v3 import KumoCloudV3

v3 = KumoCloudV3('nhw1@stern.nyu.edu', 'Oscar123_')
print("Login result:", v3.login())
print("Access token:", v3._access_token)
print("Sites:", v3.get_sites())