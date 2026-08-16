from setuptools import setup, find_packages

setup(
    name="sketion",
    version="3.4.0",
    description="Motor Editorial de Diagramas de Negocio y Arquitectura para Excalidraw (.excalidraw)",
    author="Luis Rodriguez",
    url="https://github.com/luisrodriguez-rgb/Sketion-Diagram-Design-Engine-",
    packages=find_packages(),
    py_modules=["sketion_cli"],
    entry_points={
        "console_scripts": [
            "sketion=sketion_cli:main",
        ],
    },
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Topic :: Multimedia :: Graphics :: Presentation",
    ],
)
