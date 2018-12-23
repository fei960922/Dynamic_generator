import math
import numpy as numpy
import tensorflow as tf


def conv2d(input_, output_dim, kernal=(5, 5), strides=(2, 2), padding='SAME', stddev=0.02, name="conv2d"):
    if type(kernal) == list or type(kernal) == tuple:
        [k_h, k_w] = list(kernal)
    else:
        k_h = k_w = kernal

    if type(strides) == list or type(strides) == tuple:
        [d_h, d_w] = list(strides)
    else:
        d_h = d_w = strides

    if type(padding) == list or type(padding) == tuple:
        padding = [0] + list(padding) + [0]
        input_ = tf.pad(input_, [[p, p] for p in padding], "CONSTANT")
        padding = 'VALID'

    with tf.variable_scope(name):
        w = tf.get_variable('w', [k_h, k_w, input_.get_shape()[-1], output_dim],
                            initializer=tf.truncated_normal_initializer(stddev=stddev))
        conv = tf.nn.conv2d(input_, w, strides=[1, d_h, d_w, 1], padding=padding)
        biases = tf.get_variable('biases', [output_dim], initializer=tf.constant_initializer(0.0))
        conv = tf.nn.bias_add(conv, biases)
        # conv = tf.reshape(conv, conv.get_shape())
        return conv


def conv3d(input_, output_dim, kernal=(5, 5, 5), strides=(2, 2, 2), padding='SAME', stddev=0.001, name="conv3d"):
    if type(kernal) == list or type(kernal) == tuple:
        [k_d, k_h, k_w] = list(kernal)
    else:
        k_d = k_h = k_w = kernal
    if type(strides) == list or type(strides) == tuple:
        [d_d, d_h, d_w] = list(strides)
    else:
        d_d = d_h = d_w = strides

    if type(padding) == list or type(padding) == tuple:
        padding = [0] + list(padding) + [0]
        input_ = tf.pad(input_, [[p, p] for p in padding], "CONSTANT")
        padding = 'VALID'

    with tf.variable_scope(name):
        w = tf.get_variable('w', [k_d, k_h, k_w, input_.get_shape()[-1], output_dim],
                            initializer=tf.random_normal_initializer(stddev=stddev))
        conv = tf.nn.conv3d(input_, w, strides=[1, d_d, d_h, d_w, 1], padding=padding)
        biases = tf.get_variable('biases', [output_dim], initializer=tf.constant_initializer(0.0))
        conv = tf.nn.bias_add(conv, biases)
        return conv


def convt2d(input_, output_shape, kernal=(5, 5), strides=(2, 2), padding='SAME', stddev=0.005, name="convt2d"):
    if type(kernal) == list or type(kernal) == tuple:
        [k_h, k_w] = list(kernal)
    else:
        k_h = k_w = kernal
    if type(strides) == list or type(strides) == tuple:
        [d_h, d_w] = list(strides)
    else:
        d_h = d_w = strides

    if type(padding) == list or type(padding) == tuple:
        padding = [0] + list(padding) + [0]
        input_ = tf.pad(input_, [[p, p] for p in padding], "CONSTANT")
        padding = 'VALID'

    output_shape = list(output_shape)
    output_shape[0] = tf.shape(input_)[0]

    with tf.variable_scope(name):
        w = tf.get_variable('w', [k_h, k_w, output_shape[-1], input_.get_shape()[-1]],
                            initializer=tf.random_normal_initializer(stddev=stddev))
        convt = tf.nn.conv2d_transpose(input_, w, output_shape=tf.stack(output_shape, axis=0),
                                       strides=[1, d_h, d_w, 1], padding=padding)
        biases = tf.get_variable('biases', [output_shape[-1]], initializer=tf.constant_initializer(0.0))
        convt = tf.nn.bias_add(convt, biases)
        return convt


def convt3d(input_, output_shape, kernal=(5, 5, 5), strides=(2, 2, 2), padding='SAME', stddev=0.005, name="convt3d"):
    if type(kernal) == list or type(kernal) == tuple:
        [k_d, k_h, k_w] = list(kernal)
    else:
        k_d = k_h = k_w = kernal
    if type(strides) == list or type(strides) == tuple:
        [d_d, d_h, d_w] = list(strides)
    else:
        d_d = d_h = d_w = strides

    if type(padding) == list or type(padding) == tuple:
        padding = [0] + list(padding) + [0]
        input_ = tf.pad(input_, [[p, p] for p in padding], "CONSTANT")
        padding = 'VALID'

    output_shape = list(output_shape)
    output_shape[0] = tf.shape(input_)[0]

    with tf.variable_scope(name):
        w = tf.get_variable('w', [k_d, k_h, k_w, output_shape[-1], input_.get_shape()[-1]],
                            initializer=tf.random_normal_initializer(stddev=stddev))
        convt = tf.nn.conv3d_transpose(input_, w, output_shape=tf.stack(output_shape, axis=0),
                                       strides=[1, d_d, d_h, d_w, 1], padding=padding)
        biases = tf.get_variable('biases', [output_shape[-1]], initializer=tf.constant_initializer(0.0))
        convt = tf.nn.bias_add(convt, biases)
        return convt
