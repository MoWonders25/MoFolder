# Cave Survival video: Seedance 2.0 production kit (10 min, 1080p)

1. `pip install requests edge-tts`
2. `export FAL_KEY=your_fal_key` (Seedance 2.0 on fal.ai; set `SEEDANCE_MODEL` if the endpoint id differs)
3. `python generate.py`: renders 60 × 10 s clips into `clips/` and creates `voiceover.mp3` (resumable)
4. Optional: drop a royalty-free `music.mp3` in this folder
5. `./assemble.sh` → `final_1080p.mp4`

Edit `shots.py` to change any prompt; delete that clip and rerun to regenerate only it.
Tip: if your Seedance plan supports image reference, add a fixed character image for consistency across shots.
