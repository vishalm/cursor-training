# Backend Service

The backend service is built with FastAPI and provides a robust API for the restaurant ordering system. It includes AI-powered features using Ollama and comprehensive test coverage.

## Features

- FastAPI-based REST API
- AI-powered menu recommendations
- Real-time cart management
- JWT authentication
- Comprehensive test suite
- Swagger/OpenAPI documentation
- Environment-based configuration
- Logging and monitoring

## Project Structure

```
backend/
├── app/
│   ├── api/              # API routes and endpoints
│   ├── core/             # Core functionality and config
│   ├── models/           # Data models and schemas
│   ├── services/         # Business logic and services
│   └── utils/            # Utility functions
├── tests/
│   ├── unit/            # Unit tests
│   ├── integration/     # Integration tests
│   ├── conftest.py      # Test configuration
│   └── requirements-test.txt  # Test dependencies
├── requirements.txt     # Main dependencies
└── run.py              # Application entry point
```

## Setup

1. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment:
```bash
cp .env.example .env
# Edit .env with your configuration
```

4. Run the application:
```bash
python run.py
```

## Testing

### Test Structure

- `tests/unit/`: Unit tests for individual components
- `tests/integration/`: Integration tests for API endpoints
- `conftest.py`: Shared test fixtures and configuration
- `requirements-test.txt`: Test-specific dependencies

### Running Tests

1. Install test dependencies:
```bash
pip install -r tests/requirements-test.txt
```

2. Run all tests:
```bash
pytest
```

3. Run specific test types:
```bash
pytest -m unit          # Run unit tests
pytest -m integration   # Run integration tests
```

4. Generate coverage report:
```bash
pytest --cov=app --cov-report=html
```

### Test Coverage

The test suite includes:
- Unit tests for all services and utilities
- Integration tests for all API endpoints
- Mocked external service calls
- Error case handling
- Edge case scenarios

## API Documentation

Once the server is running, access the API documentation at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Development Guidelines

### Code Style

- Follow PEP 8 guidelines
- Use type hints
- Write docstrings for all functions
- Keep functions small and focused
- Use meaningful variable names

### Testing Guidelines

- Write tests for all new features
- Maintain test coverage above 80%
- Use appropriate test markers
- Mock external dependencies
- Test both success and error cases

### Git Workflow

1. Create feature branch
2. Write tests first
3. Implement feature
4. Run all tests
5. Submit pull request

## Environment Variables

Required environment variables:
- `FLASK_APP`: Application entry point
- `FLASK_ENV`: Environment (development/production)
- `FLASK_DEBUG`: Debug mode
- `JWT_SECRET`: Secret for JWT tokens
- `OLLAMA_BASE_URL`: Ollama service URL
- `OLLAMA_MODEL`: AI model to use

## Dependencies

Main dependencies:
- FastAPI
- Uvicorn
- Pydantic
- Python-jose
- Passlib
- PyYAML
- Requests
- Aiohttp

Test dependencies:
- Pytest
- Pytest-cov
- Pytest-asyncio
- Pytest-mock
- Httpx

## Contributing

1. Fork the repository
2. Create feature branch
3. Write tests
4. Implement feature
5. Submit pull request

## License

This project is licensed under the MIT License. 