"""Render all shots with Seedance 2.0 via fal.ai's queue API, then build voiceover.

Usage:
  pip install requests edge-tts
  export FAL_KEY=...            # your fal.ai key
  export SEEDANCE_MODEL=...     # optional: override the endpoint id if fal renames it
  python generate.py          # 10-min version
  python generate.py --5min   # 5-min version
"""
import os, re, sys, time, json, asyncio, pathlib, requests
from shots import STYLE, SHOTS, SHOTS_5MIN

FIVE = "--5min" in sys.argv

MODEL = os.environ.get("SEEDANCE_MODEL", "bytedance/seedance-2.0/text-to-video")
KEY = os.environ["FAL_KEY"]
HDR = {"Authorization": f"Key {KEY}", "Content-Type": "application/json"}
OUT = pathlib.Path("clips_5min" if FIVE else "clips"); OUT.mkdir(exist_ok=True)

def render(i, prompt):
    dst = OUT / f"{i:03d}.mp4"
    if dst.exists():
        return
    body = {"prompt": STYLE + prompt, "resolution": "1080p",
            "aspect_ratio": "16:9", "duration": "10", "generate_audio": False}
    job = requests.post(f"https://queue.fal.run/{MODEL}", headers=HDR, json=body).json()
    while True:
        s = requests.get(job["status_url"], headers=HDR).json()
        if s["status"] == "COMPLETED":
            break
        if s["status"] not in ("IN_QUEUE", "IN_PROGRESS"):
            sys.exit(f"shot {i} failed: {s}")
        time.sleep(10)
    res = requests.get(job["response_url"], headers=HDR).json()
    dst.write_bytes(requests.get(res["video"]["url"]).content)
    print(f"shot {i:03d} done")

async def voiceover():
    import edge_tts
    if FIVE:
        text = pathlib.Path("narration_5min.txt").read_text()
        await edge_tts.Communicate(text, "en-US-GuyNeural").save("voiceover_5min.mp3")
        print("voiceover_5min.mp3 done")
        return
    md = pathlib.Path("../brightside-video-script.md").read_text()
    lines = re.findall(r"^NARRATOR: (.*)$|^(?!\*|\[|#|\||-|NARRATOR)([A-Z].*)$",
                       md.split("## Part 2")[1].split("### Production notes")[0], re.M)
    text = " ".join(a or b for a, b in lines if (a or b) and not (a or b).startswith(("Title", "Alt", "Thumbnail", "Target")))
    await edge_tts.Communicate(text, "en-US-GuyNeural", rate="+5%").save("voiceover.mp3")
    print("voiceover.mp3 done")

if __name__ == "__main__":
    for i, p in enumerate(SHOTS_5MIN if FIVE else SHOTS):
        render(i, p)
    asyncio.run(voiceover())
