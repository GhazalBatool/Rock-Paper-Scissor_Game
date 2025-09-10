import random
from collections import defaultdict

CHOICES = ["rock", "paper", "scissors"]
BEATS = {"rock": "scissors", "scissors": "paper", "paper": "rock"}

# track user patterns
user_counts = defaultdict(int)
epsilon = 0.1  # exploration rate

def random_ai_choice():
    return random.choice(CHOICES)

def learning_ai_choice(user_counts, epsilon=0.1):
    # Laplace smoothing
    smoothed = {c: user_counts.get(c, 0) + 1 for c in CHOICES}
    total = sum(smoothed.values())
    probs = {c: smoothed[c] / total for c in CHOICES}

    def outcome_score(ai, user):
        if ai == user: return 0.5
        return 1.0 if BEATS[ai] == user else 0.0

    expected = {}
    for ai in CHOICES:
        expected[ai] = sum(probs[u] * outcome_score(ai, u) for u in CHOICES)

    best_val = max(expected.values())
    best_moves = [m for m, v in expected.items() if v == best_val]

    # Exploration
    if random.random() < epsilon:
        return random.choice(CHOICES)
    return random.choice(best_moves)

def decide_winner(user, ai):
    if user == ai:
        return "tie"
    if BEATS[user] == ai:
        return "user"
    return "ai"
