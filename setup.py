import io

from setuptools import find_packages, setup

with io.open('README.rst', 'rt', encoding='utf8') as f:
    readme = f.read()

setup(
    name='Music',
    version='1.0.0',
    url='https://github.com/lucoxlee/Music.git',
    license='MIT',
    maintainer='music',
    maintainer_email='music@music.com',
    description='The basic blog app built in the Flask tutorial.',
    long_description=readme,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask', 'tornado'
    ],
    extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
    },
)
