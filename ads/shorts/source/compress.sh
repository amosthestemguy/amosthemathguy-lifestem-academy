#!/bin/bash
# compress.sh <in.mp4> <out.mp4> : Drive-sized copy (< 2.9 MB) for upload and Posty
in=$1; out=$2
[ -s "$out" ] && exit 0
for crf in 28 31 34; do
  ffmpeg -nostdin -hide_banner -loglevel error -y -i "$in" -c:v libx264 -crf $crf -preset slow -c:a aac -b:a 96k -movflags +faststart "$out"
  [ $(stat -c%s "$out") -lt 3000000 ] && exit 0
done
