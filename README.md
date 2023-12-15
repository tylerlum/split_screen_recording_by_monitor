# split_screen_recording_by_monitor

Split a screen recording video file into N video files, one per monitor 

# Installing

Install:

```
pip install split_screen_recording_by_monitor
```

# Usage

In Ubuntu, it is very convenient to start and stop screen-recording with CTRL + ALT + SHIFT + R. From my experience, it produces a more compact video file than [Kazam](https://github.com/henrywoo/kazam), which is very useful when we want to convert videos to gifs so they can be put into Google Slides (50 MB limit per GIF). 

The problem this library solves is when screen recording with dual monitors. The screen recording captures both monitors, but we often only want the screen recording for one monitor. You could do the cropping with an online tool, but this can be slow, manual, and time-consuming. This problem is even worse when you have large files and slow upload speeds.

Simply screen record as usual with CTRL + ALT + SHIFT + R, then run `split_screen_recording_by_monitor --input-video-filepath <PATH_TO_SCREEN_RECORDING>` the result will be N video files (one per monitor).

```
split_screen_recording_by_monitor --help
usage: split_screen_recording_by_monitor [-h] --input-video-filepath PATH [--output-video-folderpath PATH]

╭─ arguments ──────────────────────────────────────────────────╮
│ -h, --help        show this help message and exit            │
│ --input-video-filepath PATH                                  │
│                   (required)                                 │
│ --output-video-folderpath PATH                               │
│                   (default: /home/tylerlum)                  │
╰──────────────────────────────────────────────────────────────╯
```
