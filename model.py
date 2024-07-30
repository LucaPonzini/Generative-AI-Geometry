import tensorflow as tf
import numpy as np

# Simple generative model for 2D images
class SimpleGenerativeModel(tf.keras.Model):
    def __init__(self, latent_dim):
        super(SimpleGenerativeModel, self).__init__()
        self.dense1 = tf.keras.layers.Dense(128, activation='relu')
        self.dense2 = tf.keras.layers.Dense(784, activation='sigmoid')  # 28x28 image

    def call(self, inputs):
        x = self.dense1(inputs)
        x = self.dense2(x)
        return tf.reshape(x, [-1, 28, 28])  # Reshape to 28x28 image

# Function to generate 2D images
def generate_images(model, num_images, latent_dim):
    random_latent_vectors = tf.random.normal(shape=(num_images, latent_dim))
    generated_images = model(random_latent_vectors)
    return generated_images.numpy()
