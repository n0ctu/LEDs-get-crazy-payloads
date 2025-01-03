# Bad Apple Demo

To make the Bad Apple demo look good, we decided to reduce the colors to black and white first, before applying any scaling or cropping.

## Bad Apple RAW (antialiased)

Raw format is needed for processing the video using low level programming languages. It allows to iterate over the frames and pixels easily.

```bash
ffmpeg -i input.mkv -f lavfi -i color=gray:s=1280x720 -f lavfi -i color=black:s=1280x720 -f lavfi -i color=white:s=1280x720 -filter_complex threshold,format=gray,scale=48:24:flags=area,crop=48:24 -pix_fmt rgb24 -c:v rawvideo -f rawvideo -an bad-apple.raw
```

## Bad Apple H264 (antialiased)

For processing with libraries such as OpenCV, the video can be encoded in H264 format. It should have the least amount of compression to avoid artifacts. QP 0 is 'lossless'.


```bash
ffmpeg -i input.mkv -f lavfi -i color=gray:s=1280x720 -f lavfi -i color=black:s=1280x720 -f lavfi -i color=white:s=1280x720 -filter_complex threshold,format=gray,scale=48:24:flags=area,crop=48:24 -pix_fmt rgb24 -c:v libx264rgb -preset veryslow -qp 0 -an bad-apple-h264.mp4
```

## For the lulz: Bad Apple BW with threshold (no antialiasing)

The threshold example looks quite boring:

```bash
ffmpeg -i input.mkv -f lavfi -i color=gray:s=48x24 -f lavfi -i color=black:s=48x24 -f lavfi -i color=white:s=48x24 -filter_complex scale=48:24:flags=area,crop=48:24,threshold -c:v libx264rgb -preset veryslow -qp 0 -an bad-apple-bw.mp4
```

But using a custom BW palette, the result looks quite interesting! Movements seem to be more fluid and the video is more enjoyable to watch.

```bash
ffmpeg -i input.mkv -i palette-bw.png -filter_complex "[v][1:v]paletteuse;[0:v]format=gray,scale=48:24:flags=lanczos,crop=48:24[v]" -c:v libx264rgb -preset veryslow -qp 0 -an bad-apple-bw-palette.mp4
```