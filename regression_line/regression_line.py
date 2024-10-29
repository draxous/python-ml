import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from matplotlib import pyplot as plt


def main():
    seed = 0
    torch.manual_seed(seed)

    # Define the neural network model
    model = nn.Sequential(
        nn.Linear(in_features=1, out_features=30),  # Input layer to hidden layer
        nn.Sigmoid(),
        nn.Linear(in_features=30, out_features=1)  # Hidden layer to output layer
    )

    # Prepare the new training data
    x_ineffective = [0.5, 1, 1.5, 2, 2.5, 7.5, 8, 8.5, 9, 9.5]
    y_ineffective = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    x_effective = [4, 4.5, 5, 5.5, 6]
    y_effective = [1, 1, 1, 1, 1]

    # Combine the training data
    x_train = torch.FloatTensor(x_ineffective + x_effective).reshape(-1, 1)
    y_train = torch.FloatTensor(y_ineffective + y_effective).reshape(-1, 1)

    # Define loss function
    loss_function = nn.MSELoss()

    # Define the optimizer
    optimizer = optim.Adam(model.parameters())

    found = False

    # Training loop with multiple seeds for robust training
    for seed in range(100):
        torch.manual_seed(seed)

        for epoch in range(1000):
            # Predicts the output
            predictions = model(x_train)
            # Finds the loss of the predicted output and train data.
            loss = loss_function(predictions, y_train)

            # Check for the low loss threshold
            if loss < 0.00001:
                print(f"Converged at seed: {seed}")
                found = True
                break

            # Backward pass and optimization
            loss.backward()
            optimizer.step()
            optimizer.zero_grad()

        if found:
            break

    # Print the final model state
    print(f"Model state_dict: {model.state_dict()}")

    # Plot the regression line along with training data
    def plot_results():
        with torch.no_grad():
            plt.scatter(x_ineffective, y_ineffective, color="red", label="Ineffective")
            plt.scatter(x_effective, y_effective, color="green", label="Effective")

            # Predict across a range for smooth plotting
            x_range = torch.linspace(0, 10, 100).unsqueeze(1)
            y_pred_range = model(x_range)

            plt.plot(x_range.numpy(), y_pred_range.numpy(), color='blue', label='Regression Line')

            plt.xlabel("Drug Intake")
            plt.ylabel("Effectiveness")
            plt.title("Neural Network Regression Results")
            plt.legend()
            plt.show()

    plot_results()


main()
