#!/usr/bin/python env
# -*- coding: utf-8 -*-
#__author__ = zyh
"""
import tensorflow as tf
hello_op = tf.constant('Hello, Tensorflow!')
a = tf.constant(10)
b = tf.constant(32)
compute_op = tf.add(a, b)

with tf.Session() as sess:
	print(sess.run(hello_op))
	print(sess.run(compute_op))
"""


"""
import tensorflow as tf
import numpy as np

train_X = np.linspace(-1, 1, 100)
train_Y = 2 * train_X + np.random.randn(*train_X.shape) * 0.33 + 10

# Define the model

X = tf.placeholder("float")
Y = tf.placeholder("float")
w = tf.Variable(0.0, name="weight")
b = tf.Variable(0.0, name="bias")
loss = tf.square(Y - tf.mul(X, w) - b)
train_op = tf.train.GradientDescentOptimizer(0.01).minimize(loss)

# Create session to run

with tf.Session() as sess:
	sess.run(tf.initialize_all_variables())
	epoch = 1
	for i in range(10):
		for (x, y) in zip(train_X, train_Y):
			_,w_value,b_value = sess.run([train_op, w, b], feed_dict={X: x, Y: y})
		print("Epoch: {}, w: {}, b: {}").format(epoch, w_value, b_value)
		epoch += 1
"""

"""
class Myclass():
	@classmethod
	def thisIsClassMethod(cls, parament):
		print "this is a class method"
		print cls.__name__
		print type(cls)

if __name__ == "__main__":
	Myclass.thisIsClassMethod(None)
	print type(Myclass)
"""

"""
import functools
def log(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print('text:%s, call %s():' % (text, func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator

@log('execute')
def now():
	print('2016-98-98')

now()
print log('execute').__name__
print log('execute')(now).__name__
print  now.__name__
"""

import functools

def log(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		print ('call %s():' % func.__name__)
		return func(*args, **kw)
	return wrapper

@log
def now():
	print ('2017-03-17')

now()
print now.__name__
print log(now).__name__

def logger(text):
	def decorador(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print ('Text: %s, call %s()' % (text, func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorador

@logger('hello, hyz')
def today():
	print ('Hello, today is 2017-03-17!')

today()
print today.__name__
print logger('hello')(today).__name__