from setuptools import setup

setup(
    name='pynetutils',
    version='1.0.0',
    packages=['pynetutils'],
    # TODO: Add scripts
    scripts = ['bin/ranc',
               'bin/raproxy',
               'bin/rapot',
               'bin/rascan'
               ],
    url='https://github.com/RaRhAeu/pynetutils',
    license='MIT',
    author='RaRhAeu',
    author_email='radzim_ko@wp.pl',
    description='A small package with several network scripts'
)
