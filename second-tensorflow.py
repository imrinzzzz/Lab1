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

# input_tensor = [[0, 1], [2, 3], [4, 5]]
# a = tf.zeros_like(input_tensor, name="input_tensor")
#
# with tf.Session() as session:
#     writer = tf.summary.FileWriter('./graphs', session.graph)
#     print(session.run(a))
#
# writer.close()

# _____________________________________________________________

a = tf.ones([2, 3], tf.int32)

with tf.Session() as session:
    writer = tf.summary.FileWriter('./graphs', session.graph)
    print(session.run(a))

writer.close()
