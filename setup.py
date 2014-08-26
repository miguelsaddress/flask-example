from setuptools import setup

setup(
    name='rpc',
    license='MIT',
    version='0.0.1',
    packages=[
        'rpc',
        'rpc.controllers'
    ],
    dependency_links=[
        'http://github.com/mcuadros/python-solid-example/tarball/master#egg=domain-0.0.1'
    ],
    install_requires=[
        'domain == 0.0.1',
        'Flask == 0.10.1',
        'Flask-Classy == 0.6.10',
        'fake-factory >= 0.4.2'  # used in the fixtures generation
    ]
)
