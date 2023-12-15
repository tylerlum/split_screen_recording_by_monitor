from dataclasses import dataclass
import ffmpeg
from screeninfo import get_monitors
import tyro
import pathlib
from typing import Tuple


@dataclass
class Args:
    input_video_filepath: pathlib.Path
    output_video_folderpath: pathlib.Path = pathlib.Path(".").absolute()

    def __post_init__(self):
        assert self.input_video_filepath.exists(), f"{self.input_video_filepath}"
        assert self.input_video_filepath.is_file(), f"{self.input_video_filepath}"
        self.output_video_folderpath.mkdir(parents=True, exist_ok=True)


def assert_equals_one_of(a, bs):
    for b in bs:
        if a == b:
            return
    assert False, f"{a} not in {bs}"


def print_with_border(s: str) -> None:
    print("=" * 80)
    print(s)
    print("=" * 80 + "\n")


def get_video_resolution(video_filepath: pathlib.Path) -> Tuple[int, int]:
    probe = ffmpeg.probe(str(video_filepath))
    video_stream = next(
        (stream for stream in probe["streams"] if stream["codec_type"] == "video"),
        None,
    )
    assert video_stream is not None
    return (video_stream["width"], video_stream["height"])


def main() -> None:
    args: Args = tyro.cli(Args)

    # Check resolution of input video
    video_resolution = get_video_resolution(args.input_video_filepath)
    print_with_border(f"Found input video resolution: {video_resolution}")

    monitors = get_monitors()
    print_with_border(f"Found the following monitors: {monitors}")

    # Assumes all monitors stacked either vertically or horizontally
    # TODO: Support arbitrary monitor layouts
    widths = [monitor.width for monitor in monitors]
    heights = [monitor.height for monitor in monitors]
    assert_equals_one_of(
        get_video_resolution(args.input_video_filepath),
        [(sum(widths), max(heights)), (max(widths), sum(heights))],
    )
    print_with_border("Passed monitor layout check!")

    print_with_border("Splitting video by monitor...")
    for i, monitor in enumerate(monitors):
        output_video_filepath = (
            args.output_video_folderpath
            / f"{args.input_video_filepath.stem}_{i}{args.input_video_filepath.suffix}"
        )
        ffmpeg.input(str(args.input_video_filepath)).filter_(
            "crop", w=monitor.width, h=monitor.height, x=monitor.x, y=monitor.y
        ).output(str(output_video_filepath)).run()
    print_with_border("Done!")


if __name__ == "__main__":
    main()
