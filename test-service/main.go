package main

import (
	"encoding/json"
	"fmt"
	"net/http"
	"strconv"
	"strings"
	"time"
)

type LoginRequest struct {
	Username string `json:"username"`
	Password string `json:"password"`
}

type User struct {
	ID    int    `json:"id"`
	Name  string `json:"name"`
	Email string `json:"email"`
}

var users = []User{
	{ID: 1, Name: "John Doe", Email: "john@test.com"},
	{ID: 2, Name: "Jane Smith", Email: "jane@test.com"},
}

func writeJSON(w http.ResponseWriter, status int, data interface{}) {
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(status)
	json.NewEncoder(w).Encode(data)
}

// GET /health
func healthHandler(w http.ResponseWriter, r *http.Request) {
	writeJSON(w, http.StatusOK, map[string]interface{}{
		"status": "UP",
		"time":   time.Now(),
	})
}

// POST /login
func loginHandler(w http.ResponseWriter, r *http.Request) {
	var req LoginRequest

	if err := json.NewDecoder(r.Body).Decode(&req); err != nil {
		writeJSON(w, http.StatusBadRequest, map[string]string{
			"error": "invalid request",
		})
		return
	}

	if req.Username == "admin" && req.Password == "password123" {
		writeJSON(w, http.StatusOK, map[string]string{
			"token": "fake-jwt-token-12345",
		})
		return
	}

	writeJSON(w, http.StatusUnauthorized, map[string]string{
		"error": "invalid credentials",
	})
}

// GET /users
func usersHandler(w http.ResponseWriter, r *http.Request) {
	writeJSON(w, http.StatusOK, users)
}

// GET /users/{id}
func userByIDHandler(w http.ResponseWriter, r *http.Request) {
	parts := strings.Split(r.URL.Path, "/")

	if len(parts) < 3 {
		http.NotFound(w, r)
		return
	}

	id, err := strconv.Atoi(parts[2])
	if err != nil {
		writeJSON(w, http.StatusBadRequest, map[string]string{
			"error": "invalid id",
		})
		return
	}

	for _, user := range users {
		if user.ID == id {
			writeJSON(w, http.StatusOK, user)
			return
		}
	}

	writeJSON(w, http.StatusNotFound, map[string]string{
		"error": "user not found",
	})
}

// POST /users
func createUserHandler(w http.ResponseWriter, r *http.Request) {
	var user User

	if err := json.NewDecoder(r.Body).Decode(&user); err != nil {
		writeJSON(w, http.StatusBadRequest, map[string]string{
			"error": "invalid payload",
		})
		return
	}

	user.ID = len(users) + 1
	users = append(users, user)

	writeJSON(w, http.StatusCreated, user)
}

// GET /delay?seconds=5
func delayHandler(w http.ResponseWriter, r *http.Request) {
	secondsStr := r.URL.Query().Get("seconds")

	seconds, err := strconv.Atoi(secondsStr)
	if err != nil || seconds < 0 {
		seconds = 3
	}

	time.Sleep(time.Duration(seconds) * time.Second)

	writeJSON(w, http.StatusOK, map[string]interface{}{
		"message": fmt.Sprintf("Delayed %d seconds", seconds),
	})
}

// GET /error
func errorHandler(w http.ResponseWriter, r *http.Request) {
	writeJSON(w, http.StatusInternalServerError, map[string]string{
		"error": "simulated server error",
	})
}

func main() {
	http.HandleFunc("/health", healthHandler)
	http.HandleFunc("/login", loginHandler)
	http.HandleFunc("/users", usersHandler)
	http.HandleFunc("/users/", userByIDHandler)
	http.HandleFunc("/create-user", createUserHandler)
	http.HandleFunc("/delay", delayHandler)
	http.HandleFunc("/error", errorHandler)

	fmt.Println("Server running on :8080")
	http.ListenAndServe(":8080", nil)
}