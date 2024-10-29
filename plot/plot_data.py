import matplotlib.pyplot as plt
import torch


# Plot few dots
def plotDots():
    x = [0, 1, 2, 3, 4]
    y = [0, 1, 2, 3, 4]
    fig, ax = plt.subplots()
    ax.scatter(x, y, label='y = x^2')
    plt.plot(x, y)
    plt.xlabel('X axis')  # Label for the x-axis
    plt.ylabel('Y axis')  # Label for the y-axis
    plt.title('Plot of y = x^2')
    plt.show()


# plot range of x,y values
def plotDotsRange():
    x = list(range(0, 10))
    y = list(range(-10, 0))
    fig, ax = plt.subplots()
    ax.scatter(x, y, label='y = x^2')
    plt.plot(x, y)
    plt.xlabel('X axis')  # Label for the x-axis
    plt.ylabel('Y axis')  # Label for the y-axis
    plt.title('Plot of y = x^2')
    plt.show()


# plot range of values in a given start and end using linpspace.
# y = sin(x)
def plotSinCurve():
    x = torch.linspace(0, 10, 100)  # 100 values on x axis from 0 -> 10.
    y = torch.sin(x)  # sin value of x
    fig, ax = plt.subplots()
    ax.scatter(x, y, label='y = sin(x)')
    plt.plot(x, y, label='y = sin(x)')
    plt.xlabel('X axis')  # Label for the x-axis
    plt.ylabel('Y axis')  # Label for the y-axis
    plt.legend()  # Show the legend
    plt.title('Plot of Sin Curve')
    plt.show()


# plot square of a given range of values.
# y=x^2
def plotEquation():
    x = torch.linspace(-100, 100, 100)  # 100 values on x axis from -100 -> 100.
    y = torch.square(x)  # square the x value (x^2)
    fig, ax = plt.subplots()
    ax.scatter(x, y, label='y = x^2', color='red')
    plt.plot(x, y, label='y = x^2')  # Add a label for the legend
    plt.xlabel('X axis')  # Label for the x-axis
    plt.ylabel('Y axis')  # Label for the y-axis
    plt.title('Plot of y = x^2')  # Title of the plot
    plt.legend()  # Show the legend
    plt.show()


plotDots()
plotDotsRange()
plotSinCurve()
plotEquation()
