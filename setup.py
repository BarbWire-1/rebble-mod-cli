from setuptools import setup, find_packages

setup(
    name='rebble-mod-cli',
    version='0.1.0',
    description='A modular scaffolding tool for Pebble/Rebble watch development.',
    author='BarbWire aka Barbara Kälin',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/rebble-mod-cli',  # ← change when public
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'rebble_mod': ['templates/*'],
    },
    entry_points={
        'console_scripts': [
            'rebble-mod=rebble_mod.cli:main',
        ],
    },
    install_requires=[
        # Add any required packages here (e.g., click, rich, etc.)
    ],
    python_requires='>=3.6',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # or other license
        'Operating System :: OS Independent',
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Topic :: Software Development :: Build Tools',
    ],
)
