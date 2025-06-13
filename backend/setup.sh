#!/bin/bash

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Create .env file if it doesn't exist
if [ ! -f ".env" ]; then
    echo "Creating .env file..."
    cp .env.example .env
    echo "Please update the .env file with your configuration"
fi

# Create logs directory
if [ ! -d "logs" ]; then
    echo "Creating logs directory..."
    mkdir logs
fi

echo "Setup complete! You can now run the application with:"
echo "source venv/bin/activate"
echo "python run.py"