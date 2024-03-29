import unittest
import os

if __name__ == '__main__':
    loader = unittest.TestLoader()
    start_dir = os.path.join('.')
    suite = loader.discover(start_dir)

    runner = unittest.TextTestRunner()
    runner.run(suite)
