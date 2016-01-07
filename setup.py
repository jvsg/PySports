try:
	from setuptools import setup
except:
	from distutils.core import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name = 'PySports',
    version = 0.1,
    description = 'Sport notifications direct to your desktop',
    long_description = readme(),
    url = 'https://github.com/jvsg/Score-Seeker',
    author = 'Jaskaran Veer Singh', 
    author_email = 'jvsg1303@gmail.com',
    license = 'GPL-3.0',
    packages = ['PySports'],
    install_requires=[
          'pynotify',
          'untangle',
          'logging',
      ],
    entry_points={
        'console_scripts':[
            'PySports = PySports.main'
            ]
        },
    zip_safe = False
        )
