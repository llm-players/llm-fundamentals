"""
Step 1: Single Neuron from Scratch

Teaches: CONCEPTS_FOR_ENGINEERS.md - Part 1

A neuron is like a smooth if-statement:
- Takes inputs (money, tiredness, etc.)
- Multiplies each by a weight (how important is it?)
- Adds a bias (baseline preference)
- Applies activation (smooth decision)

Formula: output = activation(weights * inputs + bias)
"""

import numpy as np
import matplotlib.pyplot as plt


class Neuron:
    """A single neuron with learnable weights and bias."""
    
    def __init__(self, n_inputs):
        """
        Initialize neuron with random weights and zero bias.
        
        Args:
            n_inputs: Number of input features
        """
        # Random small weights (important for learning)
        self.weights = np.random.randn(n_inputs) * 0.01
        self.bias = 0.0
        
        print(f"Created neuron with {n_inputs} inputs")
        print(f"Initial weights: {self.weights}")
        print(f"Initial bias: {self.bias}")
    
    def forward(self, inputs):
        """
        Compute neuron output.
        
        Args:
            inputs: Input values (numpy array)
            
        Returns:
            Neuron output
        """
        # Step 1: Weighted sum
        weighted_sum = np.dot(self.weights, inputs) + self.bias
        
        # Step 2: Activation (ReLU: max(0, x))
        output = max(0, weighted_sum)
        
        return output


def demo_coffee_decision():
    """Real-world example: Should I buy coffee?"""
    
    print("="*70)
    print("DEMO 1: COFFEE DECISION (Real-World Example)")
    print("="*70)
    print("\nScenario: Should I buy coffee?")
    print("Inputs: [money, tiredness]")
    print()
    
    # Create a neuron with 2 inputs
    neuron = Neuron(n_inputs=2)
    
    # Set weights manually (how much each factor matters)
    neuron.weights = np.array([0.3, 0.7])  # tiredness matters more!
    neuron.bias = -2.0  # Generally reluctant to buy coffee
    
    print(f"Weights: {neuron.weights} (money=0.3, tiredness=0.7)")
    print(f"Bias: {neuron.bias} (baseline reluctance)")
    
    # Test scenarios
    scenarios = [
        ("Broke and awake", [2.0, 3.0]),
        ("Rich but awake", [10.0, 3.0]),
        ("Broke and exhausted", [2.0, 9.0]),
        ("Rich and exhausted", [10.0, 9.0]),
    ]
    
    print("\n" + "="*70)
    print("TESTING SCENARIOS")
    print("="*70)
    
    for description, inputs in scenarios:
        inputs_array = np.array(inputs)
        output = neuron.forward(inputs_array)
        decision = "BUY COFFEE!" if output > 3.0 else "Skip coffee"
        print(f"\n{description}")
        print(f"  Money: ${inputs[0]}, Tiredness: {inputs[1]}/10")
        print(f"  Neuron output: {output:.2f} → {decision}")


def demo_single_neuron():
    """Generic demonstration of how a neuron works."""
    
    print("\n" + "="*70)
    print("DEMO 2: GENERIC NEURON (Abstract Example)")
    print("="*70)
    
    # Create a neuron with 3 inputs
    neuron = Neuron(n_inputs=3)
    
    # Test with different inputs
    test_inputs = [
        np.array([1.0, 2.0, 3.0]),
        np.array([0.5, -1.0, 2.0]),
        np.array([-1.0, -2.0, -3.0]),
    ]
    
    print("\nMAKING PREDICTIONS")
    
    for i, inputs in enumerate(test_inputs, 1):
        output = neuron.forward(inputs)
        weighted_sum = np.dot(neuron.weights, inputs) + neuron.bias
        print(f"\nInput {i}: {inputs}")
        print(f"  Weighted sum: {weighted_sum:.4f}")
        print(f"  After ReLU: {output:.4f}")


def visualize_neuron_behavior():
    """Visualize how a neuron transforms inputs."""
    
    print("\n" + "="*70)
    print("DEMO 3: VISUALIZING NEURON BEHAVIOR")
    print("="*70)
    
    # Create a simple neuron with 1 input
    neuron = Neuron(n_inputs=1)
    neuron.weights = np.array([2.0])  # Set weight to 2
    neuron.bias = -1.0  # Set bias to -1
    
    print(f"\nNeuron: output = ReLU(2.0 * input - 1.0)")
    
    # Generate input range
    inputs = np.linspace(-2, 2, 100)
    outputs = []
    
    for x in inputs:
        output = neuron.forward(np.array([x]))
        outputs.append(output)
    
    # Plot
    plt.figure(figsize=(10, 6))
    plt.plot(inputs, outputs, linewidth=2, label='Neuron Output')
    plt.axhline(y=0, color='k', linestyle='--', alpha=0.3)
    plt.axvline(x=0, color='k', linestyle='--', alpha=0.3)
    plt.xlabel('Input', fontsize=12)
    plt.ylabel('Output', fontsize=12)
    plt.title('Single Neuron with ReLU Activation', fontsize=14, fontweight='bold')
    plt.legend(fontsize=10)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('phase-1-neural-nets/outputs/01_neuron_behavior.png', dpi=150)
    print("\nPlot saved to: phase-1-neural-nets/outputs/01_neuron_behavior.png")


def main():
    """Run all demos."""
    
    # Demo 1: Real-world example (coffee decision)
    demo_coffee_decision()
    
    # Demo 2: Generic neuron
    demo_single_neuron()
    
    # Demo 3: Visualize behavior
    visualize_neuron_behavior()
    
    print("\n" + "="*70)
    print("KEY TAKEAWAYS (Review CONCEPTS_FOR_ENGINEERS.md Part 1)")
    print("="*70)
    print("1. A neuron is like a smooth if-statement")
    print("2. Weights = How much each input matters")
    print("3. Bias = Baseline preference")
    print("4. Activation (ReLU) = Smooth decision function")
    print("5. Formula: output = max(0, weights·inputs + bias)")
    print("\nYou just built a decision-maker that can be trained!")
    print("\nNext: 02_backpropagation.py - Learn how neurons LEARN")
    print("="*70)


if __name__ == "__main__":
    # Create output directory
    import os
    os.makedirs("phase-1-neural-nets/outputs", exist_ok=True)
    
    main()
