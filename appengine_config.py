import os.path
import sys

# add `lib` subdirectory to `sys.path` for third-party libraries.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'lib'))
