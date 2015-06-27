# coding: utf-8

from setuptools import setup, find_packages

README = open('README.md').read()
CHANGES = open('CHANGES.md').read()


setup(
    name='donkey',
    version='0.0.2',

    author='hbc',
    author_email='bcxxxxxx@gmail.com',
    url='https://github.com/bcho/donkey',

    description='A simple cron-like library for executing scheduled jobs.',
    long_description='\n'.join((README, CHANGES)),
    license='MIT',

    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    install_requires=[
        'gevent',
    ],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
    ]
)
