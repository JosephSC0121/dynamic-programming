# DP Solver

A collection of implementations for **Project Euler Problem 67** and the **Travelling Salesman Problem (TSP)** using different approaches.

## Structure

```plaintext
.  
├── backend/       # Go implementation of Problem 67  
│   └── main.go  
├── bruteforce/    # Brute-force approach in Go for Problem 67  
│   └── bruteforce.go  
├── frontend/      # Visualization for the TSP solution  
│   
│ main.py  # Held-Karp algorithm for TSP    
```

## Install & Run

### Backend (Optimized DP Solution for Problem 67)
```sh
cd backend
go run main.go
```

### Brute Force Approach for Problem 67
```sh
cd bruteforce
go run bruteforce.go
```

### Frontend (Held-Karp TSP Solution)
```sh
cd frontend
pnpm run dev
```
### main.py (Held-Karp TSP Solution)
```sh
uvicorn main:app --host 0.0.0.0 --port 80
```

## Notes
- The backend uses a **dynamic programming** approach to optimize performance.
- The brute-force method serves as a benchmark but is not practical for large inputs.
- The frontend visualization aids in understanding the **Held-Karp algorithm** for solving TSP.


