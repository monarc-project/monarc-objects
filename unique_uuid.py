#!/usr/bin/env python
# -*- coding: utf-8 -*-

from glob import glob
import json

all_uuids = {}
for json_file in glob('./*/*.json'):
    with open(json_file, 'r') as f:
        d = json.load(f)
        try:
            uuid = d['uuid']
        except:
            # no uuid for this kind of object. should not be possible in the
            # future
            continue
        if 'language' in d.keys() and d['language'] != "EN":
            # do not check translations of original objects
            continue
        if all_uuids.get(uuid):
            raise Exception('Same uuid for {} and {} ({})'.format(json_file, all_uuids.get(uuid), uuid))
        all_uuids[uuid] = json_file
