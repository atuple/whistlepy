from setuptools import setup
from setuptools import setup, find_packages

readme = 'README.md'

with open(readme, 'rb') as f:
    long_description = f.read().decode('utf-8')

setup(
    name='whistlepy',
    version='0.0.8',
    author='sai',
    author_email='3030159@qq.com',
    url='https://github.com/atuple/whistlepy',
    keywords='whistle, SDK, weishao',
    description=u'whistle sdk',
    license='MIT',
    packages=["whistlepy", "whistlepy.client", "whistlepy.session", "whistlepy.client.api"],
    zip_safe=False,
    install_requires=[
        "requests>=2.4.3",
        "python-dateutil>=2.5.2"
    ]
)
