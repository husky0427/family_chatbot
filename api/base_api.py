from email.utils import parseaddr
from urllib import response
import requests
import logging

class BaseApi():
    def __init__(self):
        self._session = requests.Session()

    def _send_request(self, method: str, url: str) -> requests.Response:
        try:
            resp = self._session.request(method, url)
        except requests.exceptions.RequestException as e:
            response = None
            # TODO: Define logging setting.
            logging.ERROR(f"Request Error > url: [{method}]{url}, errmsg: {e}")
        return response
        