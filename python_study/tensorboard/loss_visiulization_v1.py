import tensorflow as tf
import os

# Load and normalize MNIST data
mnist_data = tf.keras.datasets.mnist
(X_train, y_train), (X_test, y_test) = mnist_data.load_data()
X_train, X_test = X_train / 255.0, X_test / 255.0

# Define the model
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Compile the model
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Ensure the logs directory exists
log_dir = "./logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Create TensorBoard callback
tf_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir)

# Train the model
model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=5, callbacks=[tf_callback])

