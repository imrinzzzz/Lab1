import tensorflow as tf

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

    print(session.run(tf.zeros_like(t_2)))
    print(session.run(tf.ones_like(t_2)))