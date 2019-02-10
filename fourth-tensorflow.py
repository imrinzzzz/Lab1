import tensorflow as tf
import numpy as np

# Python native types

t_0 = 19
t_1 = [b"apple", b"peach", b"grape"]
t_2 = [[True, False, False],
       [False, False, False],
       [False, True, False]]

with tf.Session() as session:
    print(session.run(tf.zeros_like(t_0)))
    print(session.run(tf.ones_like(t_0)))

    print(session.run(tf.zeros_like(t_1)))
    # print(session.run(tf.ones_like(t_1))) # expect string, got 1 (int) instead
    print(session.run(tf.ones([2, 2], np.float32))) # or tf.float32 is Ok too

    print(session.run(tf.zeros_like(t_2)))
    print(session.run(tf.ones_like(t_2)))