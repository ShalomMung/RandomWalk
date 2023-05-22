import numpy as np

def flip_coin(N):
    flips = np.random.randint(2, size=N)
    heads = np.sum(flips==0)
    tails = N - heads
    return heads, tails

print("Flipping 1000 coins")
heads, tails = flip_coin(N=1000)
print("Heads", heads)
print("Tails", tails)
