import numpy as np
import matplotlib.pyplot as plt

def main():
    pass

def main_vectorize(N, M):
    K = 2 * np.random.randint(0, 2, size=(N, M)) - 1
    X = np.zeros((N+1, M))
    X[0] = 0
    X[1:] = np.cumsum(K, axis=0)

    # Plotting
    fig, ax = plt.subplots()
    ax.step(np.arange(N+1), X)
    ax.set_xlabel("Number of steps")
    ax.set_ylabel("Position of object")
    plt.grid()
    plt.show()
    
if __name__ == "__main__":
    main_vectorize(N=1_000, M=200)