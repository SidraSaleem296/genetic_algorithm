import random
import numpy as np
EMPTY = 0
PLAYER_X = 1
PLAYER_O = -1
BOARD_SIZE = 3

# Define the population size and the number of generations
POPULATION_SIZE = 100
NUM_GENERATIONS = 5
MUTATION_PROBABILITY = 0.1


def create_population(size):
    """Create a population of random Tic-Tac-Toe strategies."""
    return [random.choices([PLAYER_X, PLAYER_O, EMPTY], k=BOARD_SIZE**2) for _ in range(size)]


def evaluate_strategy(strategy, player):
    """Evaluate a Tic-Tac-Toe strategy by playing against a random opponent."""
    wins = 0
    for _ in range(100):
        board = np.zeros((BOARD_SIZE, BOARD_SIZE))
        current_player = PLAYER_X
        while not game_over(board):
            if current_player == player:
                move = select_move(board, strategy)
                board[move[0], move[1]] = player
            else:
                random_move = select_random_move(board)
                board[random_move[0], random_move[1]] = get_opponent(player)
            current_player = get_opponent(current_player)
        if get_winner(board) == player:
            wins += 1
    return wins


def select_move(board, strategy):
    """Select a move based on the strategy."""
    possible_moves = np.argwhere(board == EMPTY)
    move = random.choice(possible_moves)
    return move


def select_random_move(board):
    """Select a random move from the available empty cells on the board."""
    possible_moves = np.argwhere(board == EMPTY)
    move = random.choice(possible_moves)
    return move


def get_opponent(player):
    """Get the opponent player symbol."""
    return PLAYER_O if player == PLAYER_X else PLAYER_X


def game_over(board):
    """Check if the game is over (win or draw)."""
    return get_winner(board) or np.all(board != EMPTY)


def get_winner(board):
    """Get the winner (if any) for the current board state."""
    rowsum = np.sum(board, axis=0)
    colsum = np.sum(board, axis=1)
    diag_sum_tl = np.trace(board)
    diag_sum_tr = np.trace(np.fliplr(board))

    # Check if any row, column, or diagonal has a sum equal to the board size,
    # indicating a win for 'X'.
    if any(rowsum == BOARD_SIZE) or any(colsum == BOARD_SIZE) or diag_sum_tl == BOARD_SIZE or diag_sum_tr == BOARD_SIZE:
        return PLAYER_X
    # Check if any row, column, or diagonal has a sum equal to the negative board size,
    # indicating a win for 'O'.
    elif any(rowsum == -BOARD_SIZE) or any(colsum == -BOARD_SIZE) or diag_sum_tl == -BOARD_SIZE or diag_sum_tr == -BOARD_SIZE:
        return PLAYER_O
    # Check if the board is full (no empty cells), indicating a tie.
    elif np.all(board != EMPTY):
        return 0
    else:
        return None


def crossover(parent1, parent2):
    """Perform crossover between two parent strategies."""
    crossover_point = random.randint(1, BOARD_SIZE**2 - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2


def mutate(strategy):
    """Perform mutation on the strategy by randomly changing one of the moves."""
    mutated_strategy = strategy.copy()
    move_index = random.randint(0, BOARD_SIZE**2 - 1)
    mutated_strategy[move_index] = random.choice([PLAYER_X, PLAYER_O, EMPTY])
    return mutated_strategy


def select_parents(population, fitness_scores):
    """Select two parents for reproduction based on their fitness scores."""
    weights = [score / sum(fitness_scores) for score in fitness_scores]
    parent1 = random.choices(population, weights)[0]
    parent2 = random.choices(population, weights)[0]
    return parent1, parent2


def genetic_algorithm():
    # Create the initial population
    population = create_population(POPULATION_SIZE)

    for generation in range(NUM_GENERATIONS):
        print(f"Generation {generation + 1}:")

        # Evaluate the fitness of each strategy in the population
        fitness_scores = []
        for strategy in population:
            wins = evaluate_strategy(strategy, PLAYER_X)
            fitness_scores.append(wins)

        # Select the best strategy from the current population
        best_strategy = population[np.argmax(fitness_scores)]
        best_fitness = max(fitness_scores)
        print(f"Best Fitness: {best_fitness}")

        # Select parents, perform crossover, and apply mutation to create the next generation
        next_generation = []
        while len(next_generation) < POPULATION_SIZE:
            parent1, parent2 = select_parents(population, fitness_scores)
            child1, child2 = crossover(parent1, parent2)

            if random.random() < MUTATION_PROBABILITY:
                child1 = mutate(child1)
            if random.random() < MUTATION_PROBABILITY:
                child2 = mutate(child2)

            next_generation.append(child1)
            next_generation.append(child2)

        # Replace the current population with the next generation
        population = next_generation

    return best_strategy


def play_game(strategy):
    """Play a game against the user using the specified strategy."""
    board = np.zeros((BOARD_SIZE, BOARD_SIZE))
    current_player = PLAYER_X

    print("Tic-Tac-Toe Game")  
    print("-----------------")

    while not game_over(board):
        print_board(board)

        if current_player == PLAYER_X:
            move = select_move(board, strategy)
            board[move[0], move[1]] = PLAYER_X
            current_player = PLAYER_O
        else:
            user_move = get_user_move(board)
            board[user_move[0], user_move[1]] = PLAYER_O
            current_player = PLAYER_X

    print_board(board)
    winner = get_winner(board)
    if winner == PLAYER_X:
        print("You lost. Better luck next time!")
    elif winner == PLAYER_O:
        print("Congratulations! You won!")
    else:
        print("It's a tie!")


def get_user_move(board):
    """Get the user's move by entering the coordinates of the desired move."""
    while True:
        try:
            row = int(input("Enter the row (1-3): ")) - 1
            column = int(input("Enter the column (1-3): ")) - 1
            if board[row, column] == EMPTY:
                return row, column
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Try again.")


def print_board(board):
    """Print the Tic-Tac-Toe board."""
    symbols = {EMPTY: " ", PLAYER_X: "X", PLAYER_O: "O"}

    for i in range(BOARD_SIZE):
        print("-------------")
        row_str = "|"
        for j in range(BOARD_SIZE):
            row_str += f" {symbols[board[i, j]]} |"
        print(row_str)
    print("-------------")


# Run the genetic algorithm to find the best strategy
best_strategy = genetic_algorithm()

# Play a game against the user using the best strategy
play_game(best_strategy)
