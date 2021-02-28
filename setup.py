from setuptools import setup

with open("README.md") as f:
    README = f.read()

with open("LICENSE") as f:
    LICENSE = f.read()

setup(
    name='hfsp',
    version='0.0.1',
    description='Uncovering the OS of Trees',
    maintainer='Douglas G. Moore',
    maintainer_email='doug@dglmoore.com',
    url='https://github.com/elife-asu/hfsp',
    license=LICENSE,
    install_requires=['neet', 'pygraphviz'],
    setup_requires=['green'],
    packages=['hfsp'],
    test_suite='test',
    platforms=['Windows', 'OS X', 'Linux']
)
