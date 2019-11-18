#!/bin/bash

set -e

for f in *; do
    if [[ -d $f ]]; then
        for object in $f/*.json
        do
            echo -n "${object}: "
            jsonschema -i ${object} $f-schema.json
            echo ''
        done
    fi
done

./unique_uuid.py
