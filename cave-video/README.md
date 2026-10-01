# Cave Survival video: Seedance 2.0 production kit (10 min, 1080p)

1. `pip install requests edge-tts`
2. `export FAL_KEY=your_fal_key` (Seedance 2.0 on fal.ai; set `SEEDANCE_MODEL` if the endpoint id differs)
3. `python generate.py`: renders 60 × 10 s clips into `clips/` and creates `voiceover.mp3` (resumable)
4. Optional: drop a royalty-free `music.mp3` in this folder
5. `./assemble.sh` → `final_1080p.mp4`

Edit `shots.py` to change any prompt; delete that clip and rerun to regenerate only it.
Tip: if your Seedance plan supports image reference, add a fixed character image for consistency across shots.

## 5-minute version
30 shots plus `narration_5min.txt` (~770 words ≈ 5:00):
`python generate.py --5min && ./assemble.sh --5min` → `final_5min_1080p.mp4`

## Rendered 5-min version (Higgsfield, Seedance 2.5, photoreal)
Final 1080p file: https://d2ol7oe51mr4n9.cloudfront.net/user_3K4hocMIWll0AjZb7crtHRLfdYD/0a82c666-5dd0-4e2e-ad4e-00c5cadf2cab.mp4
Clip/voiceover source IDs and the assembly script: `higgsfield_assemble.sh`.
