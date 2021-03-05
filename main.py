#!/usr/bin/env python
from solace_semp_config import AllApi
from solace_semp_config.configuration import Configuration
from solace_semp_config.api_client import ApiClient

config = Configuration()
config.host = "http://localhost:8080/SEMP/v2/config"
config.username = "admin"
config.password = "admin"

api_client = ApiClient(configuration=config)

all_api = AllApi(api_client = api_client)

res = all_api.get_msg_vpns(where=["enabled==true", "maxConnectionCount&gt;0"])
print(res)