import argparse
import logging
import keras
import numpy as np
from keras import backend as K
from keras.datasets import mnist
from keras.layers import Conv2D, Dense, Flatten, MaxPooling2D
from keras.models import Sequential
from keras.callbacks import TensorBoard
import nni
import os

LOG = logging.getLogger('mnist_keras')
K.set_image_data_format('channels_last')

H, W = 28, 28
NUM_CLASSES = 10

def create_mnist_model(hyper_params, input_shape=(H, W, 1), num_classes=NUM_CLASSES):
    '''
    Create simple convolutional model
    '''
    layers = [
        Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=input_shape),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D(pool_size=(2, 2)),
        Flatten(),
        Dense(100, activation='relu'),
        Dense(num_classes, activation='softmax')
    ]

    model = Sequential(layers)

    if hyper_params['optimizer'] == 'Adam':
        optimizer = keras.optimizers.Adam(lr=hyper_params['learning_rate'])
    else:
        optimizer = keras.optimizers.SGD(lr=hyper_params['learning_rate'], momentum=0.9)
    model.compile(loss=keras.losses.categorical_crossentropy, optimizer=optimizer, metrics=['accuracy'])

    return model

def load_mnist_data(args):
    '''
    Load MNIST dataset
    '''
    (x_train, y_train), (x_test, y_test) = mnist.load_data()

    # 使用方括号访问字典的键
    x_train = (np.expand_dims(x_train, -1).astype(float) / 255.)[:args['num_train']]
    x_test = (np.expand_dims(x_test, -1).astype(float) / 255.)[:args['num_test']]
    y_train = keras.utils.to_categorical(y_train, NUM_CLASSES)[:args['num_train']]
    y_test = keras.utils.to_categorical(y_test, NUM_CLASSES)[:args['num_test']]

    LOG.debug('x_train shape: %s', (x_train.shape,))
    LOG.debug('x_test shape: %s', (x_test.shape,))

    return x_train, y_train, x_test, y_test


def train_model(model, x_train, y_train, x_test, y_test, hyper_params):
    '''
    Train the model and use TensorBoard to log training process
    '''
    log_dir = os.path.join("logs", "fit", "mnist_model", "train")
    # 确保日志目录存在
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    tensorboard_callback = TensorBoard(log_dir=log_dir, histogram_freq=1)

    model.fit(x_train, y_train, 
              batch_size=hyper_params['batch_size'], 
              epochs=hyper_params['epochs'], 
              validation_data=(x_test, y_test), 
              callbacks=[tensorboard_callback])



def get_params():
    '''
    Get the hyperparameters for the model
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('--batch_size', type=int, default=128)
    parser.add_argument('--epochs', type=int, default=12)
    parser.add_argument('--learning_rate', type=float, default=0.01)
    parser.add_argument('--optimizer', type=str, default='SGD', choices=['SGD', 'Adam'])
    parser.add_argument('--num_train', type=int, default=60000)
    parser.add_argument('--num_test', type=int, default=10000)
    args = parser.parse_args()
    return args

def main():
    # Get hyperparameters from NNI or argparse
    tuner_params = nni.get_next_parameter()
    LOG.debug(tuner_params)
    hyper_params = vars(get_params())
    hyper_params.update(tuner_params)
    
    # Load data
    x_train, y_train, x_test, y_test = load_mnist_data(hyper_params)

    # Create model
    model = create_mnist_model(hyper_params)
    
    # Train model
    train_model(model, x_train, y_train, x_test, y_test, hyper_params)

    # Report the final accuracy to NNI
    score = model.evaluate(x_test, y_test, verbose=0)
    LOG.debug('Test loss: %s', score[0])
    LOG.debug('Test accuracy: %s', score[1])
    nni.report_final_result(score[1])

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()
