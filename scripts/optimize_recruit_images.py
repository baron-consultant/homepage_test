"""Create web-sized recruit images; retain all original files."""
from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / '.perf-tools'))
import imageio_ffmpeg

output = root / 'assets/media'
output.mkdir(exist_ok=True)
for i in range(1, 5):
    subprocess.run([imageio_ffmpeg.get_ffmpeg_exe(), '-hide_banner', '-y',
        '-i', str(root / f'assets/img/recruit/recruit_intro_img{i:02}.jpg'),
        '-vf', r'scale=min(1600\,iw):-2', '-c:v', 'libwebp', '-quality', '82',
        '-frames:v', '1', str(output / f'recruit-intro-{i:02}.webp')], check=True)
