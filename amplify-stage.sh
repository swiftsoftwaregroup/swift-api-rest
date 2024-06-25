#!/usr/bin/env bash

amplify_dir=./amplify/backend/api/swiftapirest/src

# App 
cp -rp src $amplify_dir/
cp -p requirements.txt $amplify_dir/

# Docker
cp -p docker/Dockerfile $amplify_dir/
cp -p docker/docker-compose.yml $amplify_dir/
