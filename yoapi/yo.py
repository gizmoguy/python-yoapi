#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

class api():
    def __init__(self, api_key):
        self.api_key = api_key

    def yoall(self):
        requests.post("http://api.justyo.co/yoall/", data={'api_token': self.api_key})
