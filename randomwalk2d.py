import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

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

def main_vectorize(N=50, M=1): # jukselapp: choices = [(), (), (), ()]
    X = np.zeros((N+1, 2, M))
    X[0, :, :] = 0
    R = 2 * np.random.randint(0, 2, size=(N, 2, M)) -1
    X[1:, :, :] = np.cumsum(R, axis=0)

    # Plotting
    #fig, ax = plt.subplots()
    #ax.plot(X[:, 0, :], X[:, 1, :])
    #ax.plot([X[0, 0, 0]], [X[0, 1, 0]], "ro")
    #plt.show()

    # Animation
    fig, ax = plt.subplots()
    #ax.set_xlim(-N/2, N/2)
    #ax.set_ylim(-N/2, N/2)
    ax.set_xlim(np.min(X), np.max(X))
    ax.set_ylim(np.min(X), np.max(X))
    lines = ax.plot(X[:1, 0, :], X[:1, 1, :])
    def func(i):
        for k,line in enumerate(lines):
            line.set_xdata(X[:i, 0, k])
            line.set_ydata(X[:i, 1, k])
    
    frames = np.arange(N+1)
    
    ani = FuncAnimation(fig, func, frames)
    plt.show()

if __name__ == "__main__":
    #main()
    main_vectorize(N=200, M=100)