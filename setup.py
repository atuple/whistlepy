from setuptools import setup
from setuptools import setup, find_packages

readme = 'README.md'

with open(readme, 'rb') as f:
    long_description = f.read().decode('utf-8')

with open('requirements.txt') as f:
    requirements = [l for l in f.read().splitlines() if l]

setup(
    name='whistlepy',
    version='0.0.2',
    author='sai',
    author_email='3030159@qq.com',
    url='https://github.com/atuple/whistlepy',
    keywords='whistle, SDK, weishao',
    description=u'whistle sdk',
    license='MIT',
    packages=["whistlepy"],
    zip_safe=False,
    install_requires=requirements
)
