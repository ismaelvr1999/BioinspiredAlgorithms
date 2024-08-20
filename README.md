# Bioinspired Algorithms Repository

This repository contains implementations of various bioinspired algorithms for optimization and machine learning. The included algorithms are:

- Genetic Algorithm
- Ant Colony Algorithm
- Simulated Annealing
- Immune System Algorithm
- Neural Network

# Table of Contents 📚
- [Technologies Used 🔧](#Technologies-Used-)
- [Usage 🚀](#Usage-)
- [Tests and Examples 🔬](#Tests-and-Examples)
    - [Genetic Algorithm Test](#Genetic-Algorithm-Test)
    - [Ant Colony Algorithm Test](#Ant-Colony-Algorithm-Test)
    - [Simulated Annealing Test](#Simulated-Annealing-Test)
    - [Neural Network Algorithm Test](#Neural-Network-Algorithm-Test)
- [Author ✍️](#Author)


# Technologies Used 🔧
- **NumPy** 📊: For handling numerical data and arrays.
- **TensorFlow** 🤖: For building and training the neural network model.
- **Matplotlib** 📈: For visualizing the results (note: this is implied; if you used it, you should mention how it's used).
## Usage 🚀

To run the project , follow these steps:
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ismaelvr1999/BioinspiredAlgorithms.git
2. **Install Dependencies:**:
    ```bash
    pip install -r requirements.txt

# Tests and Examples

Below are examples of how to use each algorithm included in this repository.

## Genetic Algorithm Test


```python
# Parameter configuration
AlgGen = AlgBio.AlgGen()
mutation_rate = datos["AlgGen"]["MutationRate"]
iterations = datos["AlgGen"]["Iterations"]

# Initialize and generate generations
obj = ParamLib.ParamAlgGenetico(AlgGen, iterations, mutation_rate)
obj.GenerateGenerations()
```
## Ant Colony Algorithm Test

```python
# Graph configuration
graph = [
    [0, 5, 2, 10],
    [5, 0, 6, 3],
    [2, 6, 0, 8],
    [10, 3, 8, 0]
]

# Algorithm parameters
num_ants = datos["AlgAntColony"]["NumAnts"]
iterations = datos["AlgAntColony"]["Iterations"]
evaporation_rate = datos["AlgAntColony"]["EvaporationRate"]
alpha = datos["AlgAntColony"]["Alpha"]
beta = datos["AlgAntColony"]["Beta"]

# Initialization and execution
objective_function = ParamLib.ParamAlgAntColony(graph)
colony = AlgBio.AntColony(num_ants=num_ants, num_iterations=iterations, evaporation_rate=evaporation_rate, alpha=alpha, beta=beta, graph=graph, objective_function=objective_function)
best_tour, best_distance = colony.run()
print(f"Best distance found: {best_distance}")
print(f"Best path found: {best_tour}")
```
## Simulated Annealing Test

```python
# Cities configuration
cities = [(0, 0), (1, 2), (3, 1), (2, 3), (5, 2)]  # Coordinates of the cities

# Algorithm parameters
initial_temperature = datos["AlgSimulatedAnnealing"]["InitialTemp"]
cooling_factor = datos["AlgSimulatedAnnealing"]["CoolingFactor"]
iterations = datos["AlgSimulatedAnnealing"]["Iterations"]

# Initialization and execution
objective_function = ParamLib.ParamAlgSimulatedAnnealing(cities)
annealing = AlgBio.SimulatedAnnealing(cities, initial_temperature, cooling_factor, iterations, objective_function)
best_solution, best_cost = annealing.simulated_annealing()
print("Best solution found:", best_solution)
print("Cost of the best solution:", best_cost)
```
## Neural Network Algorithm Test

```python
import numpy as np
import AlgBio
import ParamLib

# Training data
celsius = np.array([0, 5, 10, 15, 20, 25, 30, 35, 40, 45,
                    50, 55, 60, 65, 70, 75, 80, 85, 90, 95,
                    100, 105, 110, 115, 120, 125, 130, 135, 140, 145,
                    150, 155, 160, 165, 170, 175, 180, 185, 190, 195], dtype=float)

fahrenheit = np.array([32, 41, 50, 59, 68, 77, 86, 95, 104, 113,
                       122, 131, 140, 149, 158, 167, 176, 185, 194, 203,
                       212, 221, 230, 239, 248, 257, 266, 275, 284, 293,
                       302, 311, 320, 329, 338, 347, 356, 365, 374, 383], dtype=float)

# Neural network parameters
num_neurons = datos["NeuralNetwork"]["num_neurons"]
learning_rate = datos["NeuralNetwork"]["learning_rate"]
num_epochs = datos["NeuralNetwork"]["num_epochs"]
num_layers = datos["NeuralNetwork"]["num_hidden_layers"]

# Initialization and training
nn_config = AlgBio.NeuralNetwork(num_neurons, learning_rate, num_layers)
model = nn_config.getModel()
neural_network = ParamLib.ParamNeuralNetwork(model, celsius, fahrenheit, num_epochs)
neural_network.train()
print(neural_network.predict(0))
```

# Author
- [@ismaelvr1999](https://www.github.com/ismaelvr1999)