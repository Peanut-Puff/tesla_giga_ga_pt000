import os
import tensorflow as tf

from dataset import get_car_set


def init_model(input_shape=(224, 224, 3)):
    model = tf.keras.Sequential([
        tf.keras.layers.Conv2D(32, 5, 3, input_shape=input_shape),
        tf.keras.layers.BatchNormalization(3),
        tf.keras.layers.ReLU(),
        tf.keras.layers.MaxPool2D(),
        tf.keras.layers.Conv2D(64, 3),
        tf.keras.layers.BatchNormalization(3),
        tf.keras.layers.ReLU(),
        tf.keras.layers.MaxPool2D(),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(2048, 'relu'),
        tf.keras.layers.Dense(1, 'sigmoid')
    ])

    model.summary()

    return model


def train(model_name='model.h5'):
    os.chdir('C:/Users/luuux/Desktop/tasks/w1')
    train_X, train_Y, test_X, test_Y = get_car_set(
        'tesla_giga_ga_pt000/data/train')
    print(train_X.shape)  # (m, 224, 224, 3)
    print(train_Y.shape)  # (m, 1)
    
    if len(os.listdir('tesla_giga_ga_pt000/model')) > 0:
        model = tf.keras.models.load_model(
            'tesla_giga_ga_pt000/model/'+model_name, compile=False)
    else:
        model = init_model()

    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])
    model.fit(train_X, train_Y, epochs=20, batch_size=16)
    model.evaluate(test_X, test_Y)
    model.save('tesla_giga_ga_pt000/model/'+model_name)


if __name__ == '__main__':
    train()
