"""
Deep Learning - Neural Network from Scratch
Author: Your Name
Description: A complete Neural Network implementation using Python & NumPy
             Also includes a TensorFlow/Keras version for comparison.
"""

# ============================================================
# PART 1: Neural Network FROM SCRATCH (using only NumPy)
# ============================================================

import numpy as np
import matplotlib.pyplot as plt

class NeuralNetwork:
    """
    Multi-layer Neural Network from scratch.
    Architecture: Input -> Hidden Layers -> Output
    """

    def __init__(self, layer_sizes, learning_rate=0.01):
        """
        layer_sizes: list of neurons per layer
                     e.g., [784, 128, 64, 10]
        """
        self.layer_sizes = layer_sizes
        self.lr = learning_rate
        self.weights = []
        self.biases = []
        self.loss_history = []

        # Initialize weights (He initialization)
        for i in range(len(layer_sizes) - 1):
            w = np.random.randn(layer_sizes[i], layer_sizes[i+1]) * np.sqrt(2 / layer_sizes[i])
            b = np.zeros((1, layer_sizes[i+1]))
            self.weights.append(w)
            self.biases.append(b)

    # ---- Activation Functions ----
    def relu(self, z):
        return np.maximum(0, z)

    def relu_derivative(self, z):
        return (z > 0).astype(float)

    def softmax(self, z):
        exp_z = np.exp(z - np.max(z, axis=1, keepdims=True))
        return exp_z / np.sum(exp_z, axis=1, keepdims=True)

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    # ---- Forward Pass ----
    def forward(self, X):
        self.activations = [X]
        self.z_values = []

        for i in range(len(self.weights) - 1):
            z = self.activations[-1] @ self.weights[i] + self.biases[i]
            self.z_values.append(z)
            a = self.relu(z)
            self.activations.append(a)

        # Output layer with softmax
        z_out = self.activations[-1] @ self.weights[-1] + self.biases[-1]
        self.z_values.append(z_out)
        output = self.softmax(z_out)
        self.activations.append(output)

        return output

    # ---- Loss: Cross Entropy ----
    def compute_loss(self, y_pred, y_true):
        m = y_true.shape[0]
        log_probs = -np.log(y_pred[range(m), y_true] + 1e-8)
        return np.mean(log_probs)

    # ---- Backward Pass ----
    def backward(self, y_true):
        m = y_true.shape[0]
        grad_weights = [None] * len(self.weights)
        grad_biases = [None] * len(self.biases)

        # Output layer gradient
        delta = self.activations[-1].copy()
        delta[range(m), y_true] -= 1
        delta /= m

        for i in reversed(range(len(self.weights))):
            grad_weights[i] = self.activations[i].T @ delta
            grad_biases[i] = np.sum(delta, axis=0, keepdims=True)
            if i > 0:
                delta = (delta @ self.weights[i].T) * self.relu_derivative(self.z_values[i-1])

        # Update weights
        for i in range(len(self.weights)):
            self.weights[i] -= self.lr * grad_weights[i]
            self.biases[i] -= self.lr * grad_biases[i]

    # ---- Train ----
    def train(self, X, y, epochs=100, batch_size=64, verbose=True):
        m = X.shape[0]
        for epoch in range(epochs):
            # Shuffle data
            indices = np.random.permutation(m)
            X_shuffled = X[indices]
            y_shuffled = y[indices]

            epoch_loss = 0
            for start in range(0, m, batch_size):
                X_batch = X_shuffled[start:start+batch_size]
                y_batch = y_shuffled[start:start+batch_size]

                y_pred = self.forward(X_batch)
                loss = self.compute_loss(y_pred, y_batch)
                epoch_loss += loss
                self.backward(y_batch)

            avg_loss = epoch_loss / (m // batch_size)
            self.loss_history.append(avg_loss)

            if verbose and (epoch + 1) % 10 == 0:
                acc = self.evaluate(X, y)
                print(f"Epoch {epoch+1}/{epochs} | Loss: {avg_loss:.4f} | Accuracy: {acc:.2f}%")

    # ---- Predict ----
    def predict(self, X):
        output = self.forward(X)
        return np.argmax(output, axis=1)

    # ---- Evaluate ----
    def evaluate(self, X, y):
        predictions = self.predict(X)
        return np.mean(predictions == y) * 100

    # ---- Plot Loss ----
    def plot_loss(self):
        plt.figure(figsize=(8, 4))
        plt.plot(self.loss_history, color='blue', linewidth=2)
        plt.title("Training Loss Over Epochs")
        plt.xlabel("Epoch")
        plt.ylabel("Loss")
        plt.grid(True)
        plt.tight_layout()
        plt.savefig("loss_curve.png")
        plt.show()
        print("Loss curve saved as loss_curve.png")


# ============================================================
# PART 2: TensorFlow / Keras Version (Modern Deep Learning)
# ============================================================

def build_keras_model(input_dim, num_classes):
    """
    Build a Neural Network using TensorFlow Keras.
    Install: pip install tensorflow
    """
    try:
        import tensorflow as tf
        from tensorflow.keras import layers, models, callbacks

        model = models.Sequential([
            layers.Input(shape=(input_dim,)),
            layers.Dense(128, activation='relu'),
            layers.BatchNormalization(),
            layers.Dropout(0.3),
            layers.Dense(64, activation='relu'),
            layers.BatchNormalization(),
            layers.Dropout(0.2),
            layers.Dense(num_classes, activation='softmax')
        ])

        model.compile(
            optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
            loss='sparse_categorical_crossentropy',
            metrics=['accuracy']
        )

        model.summary()
        return model

    except ImportError:
        print("TensorFlow not installed. Run: pip install tensorflow")
        return None


# ============================================================
# MAIN - Demo with synthetic data
# ============================================================

if __name__ == "__main__":

    print("=" * 50)
    print("  Deep Learning Neural Network Demo")
    print("=" * 50)

    # Generate synthetic dataset
    np.random.seed(42)
    num_samples = 1000
    input_dim = 20
    num_classes = 3

    X = np.random.randn(num_samples, input_dim)
    y = np.random.randint(0, num_classes, num_samples)

    # Split into train/test
    split = int(0.8 * num_samples)
    X_train, X_test = X[:split], X[split:]
    y_train, y_test = y[:split], y[split:]

    print(f"\nDataset: {num_samples} samples | {input_dim} features | {num_classes} classes")
    print(f"Train: {X_train.shape} | Test: {X_test.shape}\n")

    # ---- Train from-scratch Neural Network ----
    print("--- Training Neural Network from Scratch ---")
    nn = NeuralNetwork(
        layer_sizes=[input_dim, 64, 32, num_classes],
        learning_rate=0.01
    )
    nn.train(X_train, y_train, epochs=50, batch_size=32, verbose=True)

    test_acc = nn.evaluate(X_test, y_test)
    print(f"\nTest Accuracy (Scratch NN): {test_acc:.2f}%")

    nn.plot_loss()

    # ---- Train Keras Model ----
    print("\n--- Building Keras Model ---")
    keras_model = build_keras_model(input_dim, num_classes)

    if keras_model:
        keras_model.fit(
            X_train, y_train,
            epochs=30,
            batch_size=32,
            validation_split=0.1,
            verbose=1
        )
        _, keras_acc = keras_model.evaluate(X_test, y_test, verbose=0)
        print(f"\nTest Accuracy (Keras): {keras_acc * 100:.2f}%")
        keras_model.save("neural_network_model.h5")
        print("Keras model saved as neural_network_model.h5")