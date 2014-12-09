from setuptools import setup, find_packages

setup(
    name='zeit.content.link',
    version='2.0.4.dev0',
    author='gocept',
    author_email='mail@gocept.com',
    url='https://bitbucket.org/gocept/zeit.content.link',
    description="ZEIT Link",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    license='gocept proprietary',
    namespace_packages=['zeit', 'zeit.content'],
    install_requires=[
        'grokcore.component',
        'lxml',
        'setuptools',
        'zc.sourcefactory',
        'zeit.cms>=2.31.0.dev0',
        'zeit.content.image',
        'zeit.connector',
        'zeit.push>=1.7.0.dev0',
        'zope.cachedescriptors',
        'zope.component',
        'zope.formlib',
        'zope.interface',
        'zope.publisher',
        'zope.schema',
        'zope.testbrowser',
    ],
)
