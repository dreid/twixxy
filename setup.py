from setuptools import setup

with open('README.rst') as readme:
    long_description = readme.read()


setup(
    name='twixxy',
    version='0.1.1',
    description='Twisted integration with the twiggy logging library.',
    url='https://github.com/dreid/twixxy',
    author='David Reid',
    author_email='dreid@dreid.org',
    packages=['twixxy', 'twixxy.features'],
    license='MIT',
    long_description=long_description,
    install_requires=['Twisted', 'twiggy']
)
