#!/bin/bash

set -e

for f in *; do
    if [[ -d $f ]]; then
        for object in $f/*.json
        do
            jsonschema -i ${object} $f-shema.json
        done
    fi
done
