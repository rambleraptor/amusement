from setuptools import setup, find_packages

setup(name='amusement',
      version='0.1.1',
      description='A python package and CLI to get wait times for rides at various theme parks',
      url='http://github.com/astephen2/amusement',
      author='Alex Stephen',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      install_requires=[
        'requests==2.5.3',
        'beautifulsoup4',
        'nose',
        'python-dateutil',
        'Click'
      ],
      entry_points= {
          'console_scripts' :
                'amusement = amusement.scripts.cli:cli'
                    }, 
      zip_safe=False)
