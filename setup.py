from setuptools import find_packages


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
"""
这里这么写的目的是防止setup导入出错，安装出现异常。但一般不会出错
"""

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='visualize',
    version='0.1.2', # 版本号
    author='rentianhe',
    author_email='596106517@qq.com',
    description='useful visualization function',
    license='MIT',  
    packages=find_packages(),#需要安装的代码包，也可以用find_packages函数
    install_requires=['numpy',
                      'opencv-python',
                      'matplotlib',
                      'Pillow'
                      ],
    classifiers = [
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        ],
    keywords='computer vision',
    url='https://github.com/rentainhe/visualization',
    # zip_safe=True, # 设为True，以zip的方式进行传输
    # include_package_data=True,
    platforms='any',
    long_description=long_description,
    long_description_content_type="text/markdown",
)