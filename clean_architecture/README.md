# User Management Backend with Clean Architecture in Go

A backend system for managing users, built with Go and following Clean Architecture principles. This project demonstrates separation of concerns, testability, and maintainability through layered architecture.

![Go Version](https://img.shields.io/badge/Go-1.21%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

## Features
- **CRUD Operations**: Create, read, and list users via REST API.
- **Validation**: Email format validation for user creation.
- **In-Memory Storage**: Simple storage for development/testing.
- **Unit Tests**: Test coverage for business logic.
- **Clean Architecture**: Strict separation of domain, use cases, and infrastructure.

## Installation
1. **Prerequisites**:
   - Go 1.21+ ([Download](https://go.dev/dl/))

2. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/user-management-go.git
   cd user-management-go

3. **Project structure**:
```
 user-management-go/
├── cmd/
│   └── main.go            # Entry point
└── internal/
    ├── domain/            # Entities and interfaces
    ├── usecase/           # Business logic
    ├── handler/           # HTTP handlers
    └── repository/        # Data storage (in-memory)
    