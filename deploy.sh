#!/bin/bash

# Build Docker image
docker build -t code-executor-app .

# Run Docker container
docker run -d -p 5000:5000 --name code_executor_container code-executor-app
