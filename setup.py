from setuptools import find_packages
from setuptools import setup


setup(
    name='togglepo',
    version='1.0.0',
    description='Togglepo shows how much you achieve your goal.',
    author='Takumi Ishii',
    packages = find_packages(),
    install_requires=[
        'click',
        'prettytable',
        'python-dateutil',
        'requests'
    ],
    url='https://github.com/it-akumi/togglepo',
    entry_points = {
        'console_scripts': [
            'tglp = tglp.main:main'
        ]
    }
)
