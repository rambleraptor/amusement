#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import zipfile
import StringIO
import json
from amusement.park import Park
from amusement.ride import Ride
from amusement.config.disneyparis import strings

class DisneylandParis(Park):
    def __init__(self):
        super(DisneylandParis, self).__init__()
        self._build_park()

    def getName(self):
        return 'Disneyland Paris'

    def _build_park(self):
        times = self._get_page()
        time_list = times['l']
        for i in range(0, len(times['l']), 5):
            self._make_attr(time_list[i:i+5])

    def _get_page(self):
        body = 'key=Ajjjsh;Uj'

        headers = {
            'Host' : 'disney.cms.pureagency.com',
            'Proxy-Connection': 'close',
            'Accept-Encoding' : 'gzip',
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'Content-Length' : 18,
            'Connection' : 'close',
            'User-Agent': 'Disneyland 1.0 (iPhone; iPhone OS 4.1; en_GB'
        }

        r = requests.post('https://disney.cms.pureagency.com/cms/ProxyTempsAttente', headers=headers, data=body, verify=False)
        z = zipfile.ZipFile(StringIO.StringIO(r.content)).open('temps_attente.json')
        return json.loads(z.read())

    def _make_attr(self, array):
        if array[0] not in strings:
            return

        else:
            attr_doc = Ride()
            attr_doc.setName(strings[array[0]])
            if array[3] == 1:
                attr_doc.setOpen()
            else:
                attr_doc.setClosed()

            attr_doc.setTime(array[4])
            self.addRide(attr_doc)
