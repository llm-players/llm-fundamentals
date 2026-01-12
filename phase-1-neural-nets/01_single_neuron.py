"""
Step 1: Single Neuron from Scratch

A neuron is the basic building block of neural networks.
It does: output = activation(weights * inputs + bias)

We'll build one neuron, make predictions, and understand what it does.
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


def demo_single_neuron():
    """Demonstrate how a single neuron works."""
    
    print("="*70)
    print("SINGLE NEURON DEMO")
    print("="*70)
    
    # Create a neuron with 3 inputs
    neuron = Neuron(n_inputs=3)
    
    # Test with different inputs
    test_inputs = [
        np.array([1.0, 2.0, 3.0]),
        np.array([0.5, -1.0, 2.0]),
        np.array([-1.0, -2.0, -3.0]),
    ]
    
    print("\n" + "="*70)
    print("MAKING PREDICTIONS")
    print("="*70)
    
    for i, inputs in enumerate(test_inputs, 1):
        output = neuron.forward(inputs)
        print(f"\nInput {i}: {inputs}")
        print(f"Output: {output:.4f}")


def visualize_neuron_behavior():
    """Visualize how a neuron transforms inputs."""
    
    print("\n" + "="*70)
    print("VISUALIZING NEURON BEHAVIOR")
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
    
    # Demo 1: Basic neuron
    demo_single_neuron()
    
    # Demo 2: Visualize behavior
    visualize_neuron_behavior()
    
    print("\n" + "="*70)
    print("KEY TAKEAWAYS")
    print("="*70)
    print("1. A neuron does: output = activation(weights * inputs + bias)")
    print("2. Weights determine how much each input matters")
    print("3. Bias shifts the output")
    print("4. ReLU activation makes output 0 or positive")
    print("\nNext: Learn how to make the neuron LEARN (backpropagation)")
    print("="*70)


if __name__ == "__main__":
    # Create output directory
    import os
    os.makedirs("phase-1-neural-nets/outputs", exist_ok=True)
    
    main()
