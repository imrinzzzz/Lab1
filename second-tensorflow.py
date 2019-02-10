import numpy as np
import tensorflow as tf

# # constant 1D tensor (vector)
# a = tf.constant([2, 2], name="vector")
#
# # constant 2x2 tensor (matrix)
# b = tf.constant([[0, 1], [2, 3]], name="b")
#
# # create a tensor of shape and all elements are 0s
# a = tf.zeros([2, 3], tf.int32)
#
# with tf.Session as session:
#     writer = tf.summary.FileWriter('./graphs', session.graph)
#     print(session.run(a))
#
# writer.close()

# _____________________________________________________________

# ====================== zeros ======================

# input_tensor = [[0, 1], [2, 3], [4, 5]]
# a = tf.zeros_like(input_tensor, name="input_tensor")
#
# with tf.Session() as session:
#     writer = tf.summary.FileWriter('./graphs', session.graph)
#     print(session.run(a))
#
# writer.close()

# _____________________________________________________________

# ====================== ones ======================

# a = tf.ones([2, 3], tf.int32)
# input_tensor = [[0, 1], [2, 3]]
# b = tf.ones_like(input_tensor)
#
# with tf.Session() as session:
#     writer = tf.summary.FileWriter('./graphs', session.graph)
#     print(session.run(a))
#     print(session.run(b))
#
# writer.close()

# _____________________________________________________________

# ====================== fill ======================

# a = tf.fill([2,3], 8)
#
# with tf.Session() as session:
#     writer = tf.summary.FileWriter('./graphs', session.graph)
#     print(session.run(a))
#
# writer.close()

# ______________________________________________________________

# ====================== linespace ======================

# a = tf.linspace(10.0, 13.0, 4, name="linespace")
#
# with tf.Session() as session:
#     writer = tf.summary.FileWriter('./graphs', session.graph)
#     print(session.run(a))
#
# writer.close()

# ______________________________________________________________

# ====================== range ======================

# # start = 3, limit = 18, delta = 3
# a = tf.range(3, 18, 3)
#
# b = tf.range(3, 1, -0.5)
#
# # limit = 5
# c = tf.range(5)
#
# with tf.Session() as session:
#     writer = tf.summary.FileWriter('./graphs', session.graph)
#     print(session.run(a), session.run(b), session.run(c))
#
# writer.close()

# ______________________________________________________________

# ====================== zeros ======================

# unlike numpy or py sequence, TensorFlow sequences are not iterable

# for x in np.linspace(0, 10, 5):
#     print(x)

# with tf.Session() as session:
#     writer = tf.summary.FileWriter('./graphs', session.graph)
#     for x in tf.linspace(0, 10, 4):
#         print(session.run(x))
#
# writer.close()

# ______________________________________________________________

# ====================== random constants ======================