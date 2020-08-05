import os
from setuptools import setup


base_dir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(base_dir, 'README.md')) as fid:
    long_description = fid.read()
with open(os.path.join(base_dir, 'VERSION')) as fid:
    version_number = fid.read()


setup(
    name='abstract_traffic_generator',
    version=version_number,
    description='The Abstract Traffic Generator Python Package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/open-traffic-generator/abstract-python-package',
    author='ajbalogh',
    author_email='andy.balogh@keysight.com',
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing :: Traffic Generation',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    keywords='abstract testing traffic generator automation',
    packages=['abstract_traffic_generator'],
    include_package_data=True,
    python_requires='>=3, <4'
)
