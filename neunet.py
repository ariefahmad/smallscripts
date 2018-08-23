"""
A simple introduction to making a neural network;
just a scale model to learn more about neural networks
Script will just discriminate between inputs and output
which one will generate the desired o utput
"""

# make variable arrays
inputs = [0, 0, 0, 0, 1, 0]   # o for wrong button, 1 for desired index
weights = [0, 0, 0, 0, 0, 0]  # weightage
desired_result = 1      # accept
learning_rate = 0.2     # learning rate..
trials = 6              # number of trials


def evaluate_neural_network(input_array, weight_array):
    """
    function that takes these inputs & weights and calculates an output;
    the neural net output
    just multiply weight and sum up
    """
    result = 0
    for i in range(len(input_array)):
        layer_value = input_array[i] * weight_array[i]
        result += layer_value
    print("evaluate_neural_network: " + str(result))
    print("weights: " + str(weights))
    return result

def evaluate_error(desired, actual):
    """
    function to calculate whether right value, or not
    """
    error = desired - actual
    print("evaluate_error: " + str(error))
    return error

def learn(input_array, weight_array):
    """
    learning function; changing weight array, representative of changing
    after an experience;
    dependant on learing rate
    """
    print("learning...")
    for i in range(len(input_array)):
        if input_array[i] > 0:
            weight_array[i] += learning_rate

def train(trials):
    """
    function to do repetitions
    """
    for i in range(trials):
        neural_net_result = evaluate_neural_network(inputs, weights)
        learn(inputs, weights)

if __name__ == '__main__':
    train(trials)   # do it..
