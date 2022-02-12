# HOW TO RUN

Per buildare
`rm -rf definitions && mkdir -p definitions && python -m grpc_tools.protoc -I. --python_betterproto_out=definitions scraper.proto`\