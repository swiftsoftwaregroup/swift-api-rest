#!/usr/bin/env bash

amplify_dir=./amplify/backend/api/swiftapirest/src

# App 
cp -r src $amplify_dir/
cp requirements.txt $amplify_dir/

# Docker
cp docker/Dockerfile $amplify_dir/
cp docker/docker-compose.yml $amplify_dir/
