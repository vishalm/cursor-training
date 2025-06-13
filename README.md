# Food Order Cart System

A full-stack application for managing food order carts with AI-powered conversation capabilities. The system consists of a Flask backend API and a React frontend application.

## Project Structure

```
food-order-cart/
├── .cursor/                 # Project guidelines and standards
├── backend/                 # Flask API backend
│   ├── README.md           # Backend documentation
│   ├── app/                # Application code
│   ├── tests/              # Backend tests
│   └── requirements.txt    # Python dependencies
├── frontend/               # React frontend
│   ├── README.md          # Frontend documentation
│   ├── src/               # Source code
│   ├── public/            # Static files
│   └── package.json       # Node dependencies
└── README.md              # This file
```

## Quick Start

### Prerequisites
- Python 3.8+
- Node.js 16+
- Ollama running locally
- Docker (optional)

### Development Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd food-order-cart
   ```

2. **Backend Setup**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   python run.py
   ```

3. **Frontend Setup**
   ```bash
   cd frontend
   npm install
   npm start
   ```

4. **Access the Applications**
   - Backend API: http://localhost:5000
   - Frontend App: http://localhost:3000
   - API Documentation: http://localhost:5000/swagger-ui

## Features

- **Backend**
  - RESTful API with Flask
  - Swagger/OpenAPI documentation
  - Ollama AI integration
  - In-memory storage
  - Comprehensive testing

- **Frontend**
  - React with TypeScript
  - Modern UI/UX
  - Real-time cart updates
  - AI-powered suggestions
  - Responsive design

## Documentation

- [Backend Documentation](./backend/README.md)
- [Frontend Documentation](./frontend/README.md)
- [Project Guidelines](./.cursor/guidelines.md)

## Development Guidelines

Please refer to the [Project Guidelines](./.cursor/guidelines.md) for detailed information about:
- Code organization
- Git workflow
- Testing standards
- Documentation requirements
- Security guidelines
- Performance optimization
- And more

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 