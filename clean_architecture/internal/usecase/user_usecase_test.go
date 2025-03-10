package usecase_test

import (
	"testing"
	"userManagement/internal/domain"
	"userManagement/internal/usecase"
)

type MockUserRepo struct {
	domain.UserRepository
	users map[string]*domain.User
}

func (m *MockUserRepo) Create(user *domain.User) error {
	m.users[user.ID] = user
	return nil
}

func TestCreateUser_ValidEmail(t *testing.T) {
	mockRepo := &MockUserRepo{users: make(map[string]*domain.User)}
	service := usecase.NewUserService(mockRepo)

	user := &domain.User{ID: "1", Name: "Test", Email: "test@valid.com"}
	err := service.CreateUser(user)
	if err != nil {
		t.Fatalf("Expected no error, got %v", err)
	}

	if mockRepo.users["1"] == nil {
		t.Fatal("User not saved in repository")
	}
}

func TestCreateUser_InvalidEmail(t *testing.T) {
	mockRepo := &MockUserRepo{users: make(map[string]*domain.User)}
	service := usecase.NewUserService(mockRepo)

	user := &domain.User{ID: "1", Name: "Test", Email: "invalid-email"}
	err := service.CreateUser(user)
	if err == nil {
		t.Fatal("Expected error for invalid email, got nil")
	}
}
