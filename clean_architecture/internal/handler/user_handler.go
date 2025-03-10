package handler

import (
    "encoding/json"
    "net/http"
    "userManagement/internal/domain"
    "userManagement/internal/usecase"
)

type UserHandler struct {
    service *usecase.UserService
}

func NewUserHandler(service *usecase.UserService) *UserHandler {
    return &UserHandler{service: service}
}

// Create User Handler
func (h *UserHandler) CreateUserHandler(w http.ResponseWriter, r *http.Request) {
    var user domain.User
    if err := json.NewDecoder(r.Body).Decode(&user); err != nil {
        http.Error(w, "Invalid request body", http.StatusBadRequest)
        return
    }

    if err := h.service.CreateUser(&user); err != nil {
        http.Error(w, err.Error(), http.StatusBadRequest)
        return
    }

    w.Header().Set("Content-Type", "application/json")
    w.WriteHeader(http.StatusCreated)
    json.NewEncoder(w).Encode(user)
}

// Get User by ID Handler
func (h *UserHandler) GetUserByIDHandler(w http.ResponseWriter, r *http.Request) {
    id := r.URL.Query().Get("id")
    user, err := h.service.FindUserByID(id)
    if err != nil {
        http.Error(w, err.Error(), http.StatusNotFound)
        return
    }

    w.Header().Set("Content-Type", "application/json")
    json.NewEncoder(w).Encode(user)
}

// Get All Users Handler
func (h *UserHandler) GetAllUsersHandler(w http.ResponseWriter, r *http.Request) {
    users, err := h.service.FindAllUsers()
    if err != nil {
        http.Error(w, err.Error(), http.StatusInternalServerError)
        return
    }

    w.Header().Set("Content-Type", "application/json")
    json.NewEncoder(w).Encode(users)
}