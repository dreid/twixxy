import os
from distutils.core import setup

setup(
    name='twixxy',
    version='0.1.0',
    packages=['twixxy'],
    license='MIT',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
)
