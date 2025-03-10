package usecase

import (
	"userManagement/internal/domain"
	"errors"
	"regexp"
	"time"
)

type UserService struct {
	repo domain.UserRepository
}

func NewUserService(repo domain.UserRepository) *UserService {
	return &UserService{
		repo: repo,
	}
}

func (s *UserService) CreateUser(user *domain.User) error {
	if !isValidEmail(user.Email) {
		return errors.New("invalid email format")
	}
	user.CreatedAt = time.Now()
	return s.repo.Create(user)
}

// Get user by ID
func (s *UserService) FindUserByID(id string) (*domain.User, error) {
	return s.repo.FindByID(id)
}

// Get all users
func (s *UserService) FindAllUsers() ([]*domain.User, error) {
	return s.repo.FindAll()
}

// Helper: Validate email format
func isValidEmail(email string) bool {
	regex := `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$`
	return regexp.MustCompile(regex).MatchString(email)
}
