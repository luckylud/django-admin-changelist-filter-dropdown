from setuptools import setup, find_packages

import os


setup_dir = os.path.abspath(os.path.dirname(__file__))

about = {}
with open(os.path.join(setup_dir, 'django_admin_changelist_filter_dropdown', '__about__.py')) as f:
    exec(f.read(), about)


install_requires = [
    'django>1.6',
]

setup(
    name=about['__title__'],
    description=about['__summary__'],
    license='MIT',
    url=about['__url__'],
    version=about['__version__'],
    author=about['__author__'],
    packages=find_packages(where='.'),
    keywords=['django', 'admin', 'filter', 'dropdown'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        'Topic :: Internet :: WWW/HTTP',
    ],
    install_requires=install_requires,
)
