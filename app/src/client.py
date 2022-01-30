
import logging
import os
from tkinter.messagebox import YESNOCANCEL
import requests

log = logging.getLogger('app.main.client')

# outbound url: https://echo.apps.verygood.systems/post -k -x US7m3zkWkX12sT2fPbwW6swX:e021d067-709e-48cd-8c0b-236812e6ff39@tnthlnmuhtp.SANDBOX.verygoodproxy.com:8080

class VgsClient:
    def __init__(self, username, password, tenant_id, key_location, proxy_base):
        self.proxy_url = "https://{0}:{1}@{2}.{3}".format(
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
        log.info("Response:")
        log.info(response)