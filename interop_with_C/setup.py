from setuptools import Extension, setup

setup(
    name="matrix",
    version="1.0.0",
    description="matrix situation",
    author="chronorose",
    author_email="rendemare@gmail.com",
    ext_modules=[
        Extension(
            name="matrix",
            sources=["matrix_power.c"],
            )
        ]
)
