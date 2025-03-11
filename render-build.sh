#!/bin/bash

# Update package list and install required system dependencies
apt-get update && apt-get install -y \
    pkg-config \
    libcairo2-dev \
    python3-dev \
    build-essential \
    libffi-dev

# Install Python dependencies
pip install -r requirements.txt
