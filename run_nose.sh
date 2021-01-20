#!/usr/bin/env bash
ENVIRONMENT="development" ./run_with_env.sh env/env_var.env nosetests ./unittests --cover-erase --with-coverage --cover-html --cover-html-dir=./cover --cover-package=functionality --nologcapture
