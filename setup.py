# coding: utf-8
# from __future__ import unicode_literals

import re
import codecs

from setuptools import find_packages, setup

with codecs.open('wxpy/__init__.py', encoding='utf-8') as fp:
    version = re.search(r"__version__\s*=\s*'([\w\-.]+)'", fp.read()).group(1)

with codecs.open('README.rst', encoding='utf-8') as fp:
    readme = fp.read()

setup(
    name='bl-wxpy',
    version=version,
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'wxpy = wxpy.utils:shell_entry'
        ]
    },
    install_requires=[
        'requests>=2.4.0',
        'pyqrcode',
        'pypng',
        'future',
    ],
    tests_require=[
        'pytest',
    ],
    url='https://github.com/frkhit/bl-wxpy',
    license='MIT',
    author='frkhit',
    author_email='frkhit@gmail.com',
    description='wxpy 定制版, 基于 https://github.com/youfou/wxpy:new-core 分支(不使用 itChat)',
    long_description=readme,
    keywords=[
        '微信',
        'WeChat',
        'API'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent',
        'Topic :: Communications :: Chat',
        'Topic :: Utilities',
    ]
)
