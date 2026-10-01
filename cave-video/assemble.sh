#!/usr/bin/env bash
# Stitch clips + voiceover (+ optional music.mp3) into final video
set -e
CLIPS=clips; VO=voiceover.mp3; OUTF=final_1080p.mp4
if [ "$1" = "--5min" ]; then CLIPS=clips_5min; VO=voiceover_5min.mp3; OUTF=final_5min_1080p.mp4; fi
if [ "$1" = "--5min" ]; then
  # Fit voiceover to exactly 300 s with a subtle tempo change (warns if > 8%)
  D=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$VO")
  T=$(python3 -c "print(round($D/300,4))")
  python3 -c "import sys; t=$T; sys.exit(0 if 0.92<=t<=1.08 else print(f'WARNING: voiceover is {$D:.0f}s, tempo {t}x; consider editing narration'))" || true
  ffmpeg -y -i "$VO" -af "atempo=$T,apad" -t 300 vo_fit.m4a
  VO=vo_fit.m4a
fi
ls $CLIPS/*.mp4 | sort | sed "s/^/file '/;s/$/'/" > list.txt
ffmpeg -y -f concat -safe 0 -i list.txt \
  -vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,fps=30" \
  -c:v libx264 -preset slow -crf 18 -an video.mp4
if [ -f music.mp3 ]; then
  ffmpeg -y -i video.mp4 -i $VO -stream_loop -1 -i music.mp3 \
    -filter_complex "[2:a]volume=0.12[m];[1:a][m]amix=inputs=2:duration=first[a]" \
    -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k -shortest $([ "$1" = "--5min" ] && echo "-t 300") $OUTF
else
  ffmpeg -y -i video.mp4 -i $VO -map 0:v -map 1:a -c:v copy -c:a aac -b:a 192k -shortest $([ "$1" = "--5min" ] && echo "-t 300") $OUTF
fi
echo "Done: $OUTF"
