from setuptools import setup

setup(name='amusement',
      version='0.1',
      description='A python package and CLI to get wait times for rides at various theme parks',
      url='http://github.com/astephen2/amusement',
      author='Alex Stephen',
      license='MIT',
      packages=['amusement'],
      install_requires=[
        'requests',
        'beautifulsoup4',
        'nose',
        'python-dateutil'
      ],
      zip_safe=False)
