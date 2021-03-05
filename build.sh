#!/bin/bash

if [ ! -d "venv" ]; then
  python3 -mvenv venv
fi

source venv/bin/activate

docker run -v `pwd`:/src swaggerapi/swagger-codegen-cli:2.4.13 generate \
    --config /src/config-python.json \
    -l python \
    -i /src/semp-v2-swagger-config.yaml \
    -o /src/output/python_config

cd output/python_config
python setup.py install
