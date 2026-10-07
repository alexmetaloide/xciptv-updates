"""Publish the staged, hash-checked public APK without replacing existing releases."""
import hashlib
import json
from pathlib import Path
import re
import subprocess

descriptor = json.loads(Path('release.json').read_text(encoding='utf-8'))
version = descriptor['version']
if not re.fullmatch(r'\d+\.\d+\.\d+(?:-[A-Za-z]+\.\d+)?', version):
    raise ValueError('Invalid version')
tag = f'android-v{version}'
name = f'MTPLAYER-Android-{version}.apk'
if descriptor['tag'] != tag or descriptor['apk'] != name:
    raise ValueError('Version, tag and APK name must match')
apk = Path('apks') / name
if hashlib.sha256(apk.read_bytes()).hexdigest() != descriptor['sha256']:
    raise ValueError('APK checksum mismatch')
checksum = apk.with_suffix('.apk.sha256')
checksum.write_text(f"{descriptor['sha256']}  {name}\n", encoding='utf-8')
notes = Path('release-notes.txt')
notes.write_text(descriptor['notes'], encoding='utf-8')
existing = subprocess.run(['gh', 'release', 'view', tag], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
if existing.returncode == 0:
    print(f'Release {tag} already exists; leaving its assets unchanged.')
else:
    command = ['gh', 'release', 'create', tag, str(apk), str(checksum),
               '--title', f'MTPLAYER Android/Android TV {version}',
               '--notes-file', str(notes)]
    if '-' in version:
        command.append('--prerelease')
    subprocess.run(command, check=True)
