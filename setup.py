import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='enig',                         
    packages=['enig'],                     
    version='0.1.0',                               
    license='GNU GPL v3',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Topkinsme',
    url='https://github.com/Topkinsme/enigma_machine', 
    install_requires=[],                  
    keywords=["enigma","enigma_machine","topkinsme","enig"],
    classifiers=[ 
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Documentation',
        'License :: Other/Proprietary License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    
    download_url="https://github.com/Topkinsme/enigma_machine/archive/refs/tags/0.1.0.tar.gz",
)
