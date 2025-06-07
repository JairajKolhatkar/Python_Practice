from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="contact-management-app",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A Django-based contact management application",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/contact-management-app-django",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Framework :: Django :: 3.2",
    ],
    python_requires=">=3.6",
    install_requires=[
        "Django>=3.2.19,<4.0",
        "django-crispy-forms>=1.7.2",
        "django-import-export>=1.2.0",
        "Pillow>=9.5.0",
    ],
) 