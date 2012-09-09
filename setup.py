from distutils.core import setup

setup(
    name='twcmds',
    version='0.1.0',
    author='Jake Burchard',
    packages=['twcmds'],
    license='LICENSE.txt',
    description='Execute custom commands from Twitter',
    long_description=open('README.txt').read(),
    install_requires=[
        "Tweepy"
    ]
)
