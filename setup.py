import sys
from setuptools import setup, find_packages

version = '1.2.5.dev0'

additional_install_requires = []

if sys.platform[:3].lower() == "win":
    additional_install_requires += ['nt_svcutils']


setup(
    name = "plone.recipe.zeoserver",
    version = version,
    author = "Hanno Schlichting",
    author_email = "hannosch@plone.org",
    description = "ZC Buildout recipe for installing a ZEO server",
    long_description = open('README.txt').read() + '\n' +
                       open('CHANGES.txt').read(),
    license = "ZPL 2.1",
    keywords = "zope2 zeo zodb buildout",
    url='http://pypi.python.org/pypi/plone.recipe.zeoserver',
    classifiers=[
        "License :: OSI Approved :: Zope Public License",
        "Framework :: Buildout",
        "Framework :: Zope2",
        "Programming Language :: Python",
    ],
    packages = find_packages('src'),
    include_package_data = True,
    package_dir = {'': 'src'},
    namespace_packages = ['plone', 'plone.recipe'],
    install_requires = [
        'zc.buildout',
        'setuptools',
        'zc.recipe.egg',
        'zope.mkzeoinstance',
        'ZODB3 >= 3.8',
        'ZopeUndo',
    ] + additional_install_requires,
    zip_safe=False,
    entry_points = {
        'zc.buildout': ['default = plone.recipe.zeoserver:Recipe'],
    },
    )
