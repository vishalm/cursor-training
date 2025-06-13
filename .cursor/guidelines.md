# Project Guidelines and Standards

## Code Organization

### Backend (Python/Flask)
- Follow PEP 8 style guide
- Use type hints for all function parameters and return values
- Maximum line length: 88 characters (Black formatter standard)
- Use meaningful variable and function names
- Document all public functions and classes with docstrings
- Keep functions small and focused (max 20-30 lines)
- Use dependency injection for better testability

### Frontend (React/TypeScript)
- Follow Airbnb JavaScript Style Guide
- Use TypeScript for all components and utilities
- Maximum line length: 100 characters
- Use functional components with hooks
- Implement proper error boundaries
- Follow atomic design principles for components
- Use CSS-in-JS or styled-components for styling

## Git Workflow

### Branch Naming
- feature/feature-name
- bugfix/bug-description
- hotfix/issue-description
- release/version-number

### Commit Messages
- Use conventional commits format:
  - feat: new feature
  - fix: bug fix
  - docs: documentation changes
  - style: formatting changes
  - refactor: code refactoring
  - test: adding tests
  - chore: maintenance tasks

### Pull Requests
- Must include description of changes
- Must include test coverage
- Must pass all CI checks
- Must be reviewed by at least one team member

## Testing Standards

### Backend
- Unit tests for all business logic
- Integration tests for API endpoints
- Mock external services (Ollama)
- Minimum 80% code coverage
- Use pytest for testing

### Frontend
- Unit tests for components
- Integration tests for user flows
- E2E tests for critical paths
- Use Jest and React Testing Library
- Minimum 80% code coverage

## Documentation

### Code Documentation
- Use JSDoc for JavaScript/TypeScript
- Use Python docstrings for Python code
- Document all public APIs
- Keep documentation up to date

### API Documentation
- Use OpenAPI/Swagger for API documentation
- Document all endpoints, request/response schemas
- Include example requests and responses
- Document error scenarios

## Security Guidelines

### Backend
- Input validation for all endpoints
- Rate limiting implementation
- Proper error handling
- Secure configuration management
- CORS configuration
- Authentication/Authorization checks

### Frontend
- Input sanitization
- XSS prevention
- CSRF protection
- Secure storage of sensitive data
- Proper error handling
- Loading states management

## Performance Guidelines

### Backend
- Implement caching where appropriate
- Optimize database queries
- Use connection pooling
- Implement proper indexing
- Monitor memory usage

### Frontend
- Code splitting
- Lazy loading
- Image optimization
- Bundle size optimization
- Performance monitoring

## Development Environment

### Required Tools
- Python 3.8+
- Node.js 16+
- Docker
- Git
- VS Code/Cursor
- Postman/Insomnia

### VS Code/Cursor Extensions
- Python
- ESLint
- Prettier
- GitLens
- Docker
- REST Client

## CI/CD Pipeline

### Stages
1. Lint
2. Test
3. Build
4. Deploy

### Requirements
- All tests must pass
- No linting errors
- Successful build
- Security scan passed

## Monitoring and Logging

### Backend
- Structured logging
- Error tracking
- Performance monitoring
- Health checks
- Metrics collection

### Frontend
- Error tracking
- Performance monitoring
- User analytics
- Error boundary logging

## Accessibility

### Frontend
- WCAG 2.1 compliance
- Keyboard navigation
- Screen reader support
- Color contrast
- Focus management

## Internationalization

### Frontend
- Use i18n for translations
- Support RTL languages
- Date/time formatting
- Number formatting
- Currency handling

## Error Handling

### Backend
- Consistent error response format
- Proper HTTP status codes
- Detailed error messages
- Error logging
- Error tracking

### Frontend
- User-friendly error messages
- Error boundaries
- Fallback UI
- Retry mechanisms
- Error reporting

## Code Review Checklist

### General
- [ ] Follows coding standards
- [ ] Proper error handling
- [ ] Documentation updated
- [ ] Tests included
- [ ] No security vulnerabilities
- [ ] Performance considered

### Backend
- [ ] Input validation
- [ ] Error handling
- [ ] Logging
- [ ] Security checks
- [ ] Database optimization

### Frontend
- [ ] Component structure
- [ ] State management
- [ ] Error boundaries
- [ ] Loading states
- [ ] Accessibility 