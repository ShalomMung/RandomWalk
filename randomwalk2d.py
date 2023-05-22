import numpy as np
import matplotlib.pyplot as plt

def main():
    N = 50
    X = np.zeros((N+1, 2))
    # start at origo
    X[0, :] = 0
    choices = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    for i in range(N):
        index = np.random.randint(0, 4)
        Ri = choices[index]
        X[i+1, :] = X[i, :] + Ri

    fig, ax = plt.subplots(1, 2)
    ax[0].plot(X[: N//2, 0], X[: N//2, 1]) # Plotting a half of the whole N
    # Red spot as a string point
    ax[0].plot([X[0, 0]], [X[0, 1]], "ro")
    ax[1].plot(X[:, 0], X[:, 1])
    ax[1].plot([X[0, 0]], [X[0, 1]], "ro")
    plt.show()
    
if __name__ == "__main__":
    main()