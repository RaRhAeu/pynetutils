from distutils.core import setup

setup(
    name='pynetutils',
    version='1.0.0',
    packages=['pynetutils'],
    scripts=['/bin/ranc', 'bin/rascan', 'bin/raxy'],
    url='https://github.com/RaRhAeu/pynetutils',
    license='MIT',
    author='RaRhAeu',
    author_email='radzim_ko@wp.pl',
    description='"Small python package containing several network scripts'
)
