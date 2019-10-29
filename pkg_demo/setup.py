import os
import setuptools

setuptools.setup(
    name='zjw-pkgdemo',
    version='0.0.1',
    keywords='pkgdemo',
    description='A demo for python packaging.',
    long_description=open(
        os.path.join(
            os.path.dirname(__file__),
            'README.md'
        )
    ).read(),
    author='zjunwei',
    author_email='zjunweihit@163.com',
    #url='https://github.com/DeliangFan/packagedemo',
    packages=setuptools.find_packages(),
    license='MIT'
)

