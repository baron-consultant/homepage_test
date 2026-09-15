"""Create a web-sized home video without changing the source asset."""
from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / '.perf-tools'))
import imageio_ffmpeg

output = root / 'assets/media'
output.mkdir(exist_ok=True)
ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
source = str(root / 'assets/img/index.mp4')
subprocess.run([ffmpeg, '-hide_banner', '-y', '-i', source, '-an',
                '-c:v', 'libx264', '-preset', 'slow', '-crf', '24',
                '-maxrate', '4M', '-bufsize', '8M', '-pix_fmt', 'yuv420p',
                '-movflags', '+faststart', '-threads', '4',
                str(output / 'index-web.mp4')], check=True)
subprocess.run([ffmpeg, '-hide_banner', '-y', '-ss', '0.5', '-i', source,
                '-frames:v', '1', '-q:v', '3', '-update', '1',
                str(output / 'index-poster.jpg')], check=True)
