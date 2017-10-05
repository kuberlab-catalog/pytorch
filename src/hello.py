from __future__ import print_function

import cntk



def main(_):
    print("CNTK: "+cntk.__version__)
    print(cntk.minus([1, 2, 3], [4, 5, 6]).eval())


if __name__ == '__main__':
    tf.app.run()