// cmd/main.go
package main

import (
	"log"
	"net/http"
	"userManagement/internal/handler"
	"userManagement/internal/repository"
	"userManagement/internal/usecase"

	"github.com/gorilla/mux"
)

func main() {
	// Initialize dependencies
	userRepo := repository.NewUserRepo()
	userService := usecase.NewUserService(userRepo)
	userHandler := handler.NewUserHandler(userService)

	// Setup router
	r := mux.NewRouter()
	r.HandleFunc("/users", userHandler.CreateUserHandler).Methods("POST")
	r.HandleFunc("/users/{id}", userHandler.GetUserByIDHandler).Methods("GET")
	r.HandleFunc("/users", userHandler.GetAllUsersHandler).Methods("GET")

	// Start server
	log.Println("Server running on :8080")
	log.Fatal(http.ListenAndServe(":8080", r))
}
