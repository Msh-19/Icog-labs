// internal/repository/user_repository.go
package repository

import (
	"errors"
	"sync"
	"userManagement/internal/domain"
)

type UserRepo struct {
	mu    sync.Mutex
	users map[string]*domain.User
}

func NewUserRepo() *UserRepo {
	return &UserRepo{
		users: make(map[string]*domain.User),
	}
}

func (r *UserRepo) Create(user *domain.User) error {
	r.mu.Lock()
	defer r.mu.Unlock()
	r.users[user.ID] = user
	return nil
}

func (r *UserRepo) FindByID(id string) (*domain.User, error) {
	r.mu.Lock()
	defer r.mu.Unlock()
	user, exists := r.users[id]
	if !exists {
		return nil, errors.New("user not found")
	}
	return user, nil
}

func (r *UserRepo) FindAll() ([]*domain.User, error) {
	r.mu.Lock()
	defer r.mu.Unlock()
	users := make([]*domain.User, 0, len(r.users))
	for _, user := range r.users {
		users = append(users, user)
	}
	return users, nil
}
