  
from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='tokeninfo',
  version='0.0.1',
  description='tokeninfo is a Python Package created for simply scraping discord account data with the use of an account token.',
  long_description=open('README.md').read(),
  url='https://github.com/7uk/tokeninfo-package',  
  author='7uk',
  author_email='doopycheats@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='discord', 
  packages=find_packages(),
  install_requires=['requests', 'json'] 
)
	
