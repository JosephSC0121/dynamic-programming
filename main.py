from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Tuple

app = FastAPI()

origins = [
    "http://127.0.0.1:4321",  # React frontend URL
    "http://localhost:8000",  
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class DistanceMatrixInput(BaseModel):
    distance_matrix: List[List[int]]

def held_karp(distance_matrix: List[List[int]]) -> Tuple[List[int], int]:
    n = len(distance_matrix)
    C = {}

    for k in range(1, n):
        C[(1 << k, k)] = (distance_matrix[0][k], 0)

    for subset_size in range(2, n):
        for subset in combinations(range(1, n), subset_size):
            bits = 0
            for bit in subset:
                bits |= 1 << bit
            for k in subset:
                prev_bits = bits & ~(1 << k)
                res = []
                for m in subset:
                    if m == 0 or m == k:
                        continue
                    res.append((C[(prev_bits, m)][0] + distance_matrix[m][k], m))
                C[(bits, k)] = min(res)

    bits = (2**n - 1) - 1
    res = []
    for k in range(1, n):
        res.append((C[(bits, k)][0] + distance_matrix[k][0], k))
    opt, parent = min(res)

    path = []
    last = parent
    bits = (2**n - 1) - 1
    for i in range(n - 1):
        path.append(last)
        new_bits = bits & ~(1 << last)
        _, last = C[(bits, last)]
        bits = new_bits

    path.append(0)

    return path[::-1], opt

def combinations(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i + 1, r):
            indices[j] = indices[j - 1] + 1
        yield tuple(pool[i] for i in indices)

@app.post("/solve_tsp/")
def solve_tsp_endpoint(data: DistanceMatrixInput):
    distance_matrix = data.distance_matrix
    if not distance_matrix or not all(len(row) == len(distance_matrix) for row in distance_matrix):
        raise HTTPException(status_code=400, detail="Invalid distance matrix")

    route, distance = held_karp(distance_matrix)
    cities = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
    route_letters = [cities[i] for i in route]
    return {
        "route": route,
        "distance": distance,
        "cites": route_letters
    }

# Datos de entrada
data = DistanceMatrixInput(distance_matrix=[
    [0, 6, 34, 65, 11, 13, 20, 19, 61, 41, 60, 47, 31],
    [6, 0, 21, 8, 51, 6, 30, 23, 24, 34, 36, 12, 63],
    [34, 21, 0, 41, 21, 9, 27, 41, 10, 22, 50, 25, 61],
    [65, 8, 41, 0, 18, 63, 63, 19, 56, 37, 6, 50, 9],
    [11, 51, 21, 18, 0, 12, 46, 61, 20, 17, 40, 37, 61],
    [13, 6, 9, 63, 12, 0, 53, 53, 61, 53, 14, 57, 46],
    [20, 30, 27, 63, 46, 53, 0, 41, 31, 29, 16, 53, 27],
    [19, 23, 41, 19, 61, 53, 41, 0, 7, 61, 43, 31, 56],
    [61, 24, 10, 56, 20, 61, 19, 7, 0, 20, 5, 34, 47],
    [41, 34, 22, 6, 17, 53, 31, 61, 20, 0, 52, 63, 45],
    [27, 16, 31, 10, 63, 62, 20, 27, 18, 51, 0, 46, 16],
    [37, 51, 10, 31, 6, 61, 7, 62, 52, 7, 46, 0, 21],
    [5, 40, 48, 11, 59, 61, 52, 18, 49, 18, 16, 21, 0]
])

# Resolver el problema del viajero
route, distance = held_karp(data.distance_matrix)
print(f"Ruta: {route}")
print(f"Distancia: {distance}")

# Mapear los índices a las letras de las ciudades
cities = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
route_letters = [cities[i] for i in route]

print(f"Ruta en letras: {route_letters}")
print(f"Distancia: {distance}")