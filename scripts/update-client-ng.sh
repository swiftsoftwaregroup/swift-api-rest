#!/usr/bin/env bash

# switch to parent directory
script_path=`dirname ${BASH_SOURCE[0]}`
pushd $script_path/..

# directory to which python client sdk should be generated 
output="../swift-api-rest-ng"

if [ ! -z "$1" ]
  then
    $output = $1
fi

mkdir -p $output
# rm -rf $output/*

java -jar openapi-generator-cli.jar generate \
  --input-spec http://localhost:8001/openapi.json \
  --generator-name typescript-angular \
  --output $output \
  --config clients/typescript-ng.json

popd