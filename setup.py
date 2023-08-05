from setuptools import setup, find_packages

def read(path: str) -> str:
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

setup(
    name='py-tempmail',
    version='1.0.0',
    description='Python library for generating and managing temporary email addresses.',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    author='cubicbyte',
    author_email='bmaruhnenko@gmail.com',
    url='https://github.com/cubicbyte/py-tempmail',
    packages = find_packages(),
    license='MIT',
    keywords='disposable-email temporary-email temp-email temp-mail email mail email-generator mail-generator',
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)