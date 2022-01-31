
import logging
import os
import requests

log = logging.getLogger('app.main.client')

class VgsClient:
    def __init__(self, username, password, tenant_id, key_location, proxy_base):
        self.proxy_url = "http://{0}:{1}@{2}.{3}".format(
            username, password, tenant_id, proxy_base)
        log.info("PROXY_URL: {0}".format(self.proxy_url))
        self.key_location = key_location
        log.info("KEY LOCATION: {0}".format(self.key_location))

    def retrieve(self, token):
        # TODO: Change how we are setting this proxy...
        os.environ['HTTPS_PROXY'] = self.proxy_url
        response = requests.post('https://echo.apps.verygood.systems/post',
                                json={'secret_data': token},
                                verify=self.key_location)
        log.info("Response code: {0}", response.status_code) 
        data = response.json()
        log.info("Response json: {0}", data) 
        return data