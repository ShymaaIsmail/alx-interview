#!/usr/bin/python3
"""Prime Game"""


def sieve_of_eratosthenes(max_num):
    """Return a list of primes up to max_num (inclusive)."""
    sieve = [True] * (max_num + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes
    for start in range(2, int(max_num**0.5) + 1):
        if sieve[start]:
            for multiple in range(start*start, max_num + 1, start):
                sieve[multiple] = False
    return [num for num, is_prime in enumerate(sieve) if is_prime]


def isWinner(x, nums):
    """Determine who wins the most rounds in the prime game."""
    max_n = max(nums) if nums else 0
    primes = sieve_of_eratosthenes(max_n)

    def play_game(n):
        """Simulate a single game of prime removal with maximum number n."""
        if n < 2:
            return 'Ben'
        # Initialize the game state
        remaining = set(range(1, n + 1))
        turn = 0  # 0 for Maria, 1 for Ben
        while remaining:
            # Find the smallest prime
            chosen_prime = next((p for p in primes
                                if p <= n and p in remaining),
                                None)

            if chosen_prime is None:
                # No valid moves, current player loses
                return 'Ben' if turn == 0 else 'Maria'

            # Remove chosen prime and its multiples
            to_remove = set(p for p in remaining if p % chosen_prime == 0)
            remaining.difference_update(to_remove)
            # Switch turn
            turn = 1 - turn
        return 'Ben' if turn == 0 else 'Maria'
    if x == 0 or not nums:
        return None

    results = {'Maria': 0, 'Ben': 0}

    for n in nums:
        winner = play_game(n)
        if winner:
            results[winner] += 1

    if results['Maria'] > results['Ben']:
        return 'Maria'
    elif results['Ben'] > results['Maria']:
        return 'Ben'
    else:
        return None
