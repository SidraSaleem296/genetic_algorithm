# Play with AI
# Genetic Algorithm 

Welcome to the **Genetic Algorithm for Tic-Tac-Toe Strategies** project repository! 🧬🕹️

In this project, we explore the world of artificial intelligence and genetic algorithms to evolve strategies for playing Tic-Tac-Toe. By using a genetic algorithm, we aim to find strategies that can win against random opponents. Let's dive into the details!

## Project Overview

This project focuses on evolving Tic-Tac-Toe strategies using a genetic algorithm approach. We'll start by creating a population of random strategies and evaluate their performance by having them play against random opponents. The goal is to evolve strategies over multiple generations to find the best one that can consistently win the game.

## Implementation

The Python script provided in this repository contains the genetic algorithm implementation. Here's a quick breakdown of its components:

### Components

- Population Initialization: We begin with a population of randomly generated strategies.
- Fitness Evaluation: Each strategy is evaluated by playing against random opponents to determine its fitness.
- Selection: Parents are selected for reproduction based on their fitness scores.
- Crossover: Crossover is performed between two parents to create new child strategies.
- Mutation: Mutation introduces diversity by randomly changing specific moves in a strategy.
- Next Generation: The next generation is formed by combining offspring from crossover and mutation.
- Termination: The algorithm iterates through multiple generations to improve strategies.

### Playing the Game

You can also play a Tic-Tac-Toe game against the best-evolved strategy. The script allows you to make your moves, and the AI will respond with its own strategies. Can you beat the evolved AI?

## Getting Started

1. Make sure you have Python installed on your system.
2. Run the provided script `genetic_algorithm_for_games` in your preferred Python environment.
3. Follow the prompts to play the game against the AI using the best-evolved strategy.

## Conclusion

The **Genetic Algorithm for Tic-Tac-Toe Strategies** project showcases how genetic algorithms can be utilized to evolve strategies for playing games. By combining artificial intelligence and evolutionary principles, we're able to create strategies that improve over generations. Feel free to explore the code, experiment with parameters, and challenge yourself against the evolved AI!
