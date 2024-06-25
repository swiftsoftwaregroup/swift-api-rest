#!/usr/bin/env bash

uvicorn swift_api_rest.app:app --port 8001 --reload
