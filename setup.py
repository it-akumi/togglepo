from setuptools import setup


setup(
    name='togglepo',
    version='0.0',
    description='Togglepo shows how much you achieve your goal.',
    author='Takumi Ishii',
    install_requires=[
        'click',
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
