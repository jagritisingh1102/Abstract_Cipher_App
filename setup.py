from setuptools import setup

setup(
    name='abs_cipher',
    version='1.0.0',
    py_modules=['abs_cipher'],
    python_requires=">=3.6",
    install_requires=['Click'],
    entry_points={
        'console_scripts': [
            'abs_cipher=abs_cipher:main'
        ]
    }
)
