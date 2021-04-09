import setuptools

with open("README.md", "r", encoding="utf-8") as file:
    README = file.read()

setuptools.setup(
    name="paper-board",
    version="0.0.1",
    description="E-Paper board display library",
    long_description=README,
    long_description_content_type="text/markdown",
    author="AMing",
    author_email="cyberming@gmail.com",
    url="https://github.com/aming/paper-board",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license='MIT',
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'paper-board=paper_board.command_line:main',
            'pull-data=paper_board.data_puller:main',
            'render-board=paper_board.data_puller:render',
        ]
    },
    install_requires=[
        'pillow',
        'pyowm',
        'yfinance',
    ],
    extras_require={
        'spi':  [
            "spidev",
            'rpi.gpio',
        ]
    },
    python_requires=">=3.7",
)
