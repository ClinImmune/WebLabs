from distutils.core import setup, Extension

databaseModule = Extension(
    'database',
    sources = [
        'src/database.cpp',
    ]
)

setup(
    name = 'AlleleTree',
    version = '0.1a',
    description = 
    '''
    This module allows python to access a database and create epitope analysis
    jobs.
    ''',
    ext_modules = [
        databaseModule,
    ]
)
