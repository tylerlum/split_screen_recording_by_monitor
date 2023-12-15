from setuptools import setup, find_packages
from pathlib import Path

VERSION = "0.0.1"
DESCRIPTION = "Split a screen recording video file into N video files, one per monitor"
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="split_screen_recording_by_monitor",
    version=VERSION,
    author="Tyler Lum",
    author_email="tylergwlum@gmail.com",
    url="https://github.com/tylerlum/split_screen_recording_by_monitor",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=["ffmpeg-python", "screeninfo", "tyro"],
    keywords=["python", "screen recording", "ffmpeg", "split", "monitor"],
    entry_points={
        "console_scripts": [
            "split_screen_recording_by_monitor=split_screen_recording_by_monitor.core:main",
        ],
    },
    classifiers=[
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
    ],
)
