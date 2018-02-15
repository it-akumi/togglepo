from setuptools import find_packages
from setuptools import setup

import tglp


setup(
    name='togglepo',
    version=tglp.__version__,
    description='Togglepo shows how much you achieve your goal.',
    author='Takumi Ishii',
    packages=find_packages(),
    install_requires=[
        'click',
        'prettytable',
        'requests'
    ],
    url='https://github.com/it-akumi/togglepo',
    entry_points={
        'console_scripts': [
            'tglp = tglp.main:main'
        ]
    }
)
