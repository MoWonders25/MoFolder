# Shot list for "What If You Got Trapped in the Deepest Cave on Earth for 30 Days?"
# Each shot = one Seedance 2.0 clip (10 s, 1080p, 16:9). 60 shots = 10:00.
STYLE = ("Photorealistic cinematic documentary footage, shot on ARRI Alexa, 35mm lens, natural "
         "headlamp lighting in deep darkness, realistic skin and textures, shallow depth of field, "
         "subtle handheld camera, film grain. Consistent caver: man in his 30s, short dark beard, "
         "orange caving suit, scuffed yellow helmet with LED headlamp, blue backpack. "
         "No text, no logos, no subtitles. ")

SHOTS = [
 # 0:00 HOOK
 "Caver dangles on a rope inside a vast dark vertical cave shaft, headlamp flickering, camera slowly pushes in on worried face",
 "Close-up of the rope fraying strand by strand, then snapping; caver drops out of frame into darkness",
 "Drone shot sinking down into an enormous dark vertical cave shaft, walls dripping, scale emphasized by a tiny headlamp far below",
 "Caver sits on a rock ledge holding a dead radio, shakes it, sparks, sighs; tiny pile of food bars beside them",
 "Extreme close-up of a wristwatch with a cracked face, second hand stopped, water droplets on the glass",
 "Dramatic slow zoom into black cave mouth on a mountain, eerie glow inside",
 # 0:60 SETUP
 "Aerial drone footage over the jagged Caucasus mountains near the Black Sea, clouds below the peaks",
 "Caving team rappelling down a deep wet limestone shaft, headlamps glowing in mist, camera tracks downward",
 "Cavers resting in a hammock camp deep underground, steam rising from a tiny stove",
 "Caver lands at the very bottom of the cave, looks up at a tiny dot of light far above",
 # 1:40 DAY 1 DARK
 "Caver clicks off headlamp; frame falls to near-total black, only faint breath vapor catching a sliver of light",
 "Caver waves hand in front of face in total darkness, rim-lit faintly, confused expression",
 "Close-up of gloved hands checking a headlamp and a single spare battery on wet rock",
 "Thermometer on cave wall drops to cold, frost appears on caver's eyebrows, water droplets on jacket",
 "Caver sits on backpack and wraps in shiny silver emergency blanket, crinkling, shivering stops",
 "Cozy wide shot: small caver wrapped in silver blanket in huge dark cavern, single dim lamp",
 # 2:40 DAY 3 WATER FOOD
 "Macro shot of water drip falling from a stalactite into caver's cupped hands, splash in slow motion",
 "Caver collects drips into a bottle, ignoring a murky stagnant puddle",
 "Underground river flows through a glowing blue cavern, caver watches from a ledge",
 "Caver breaks an energy bar into tiny pieces and lines them up neatly on a rock",
 "Close-up of the caver's gaunt face chewing slowly, eyes tired, headlamp glow",
 "Caver takes a tiny nibble of snack, warm glow radiates from chest showing body heat",
 "Caver looks up thoughtfully toward the darkness above, droplets falling through the headlamp beam",
 # 3:50 DAY 7 TIME
 "Time-lapse feel: headlamp beam sweeping a still cave chamber, shadows stretching, no sense of day or night",
 "1960s-style archival-look footage: bearded geologist in a small tent beside a blue underground glacier, ice chunks falling nearby, notebooks and a lamp",
 "Scientist emerges from cave into daylight, blinking in daylight, stunned, team members around him",
 "Caver scratches tally marks on cave wall, marks begin to blur and wiggle",
 "Caver wakes in a sleeping bag in total darkness, fumbles for headlamp, disoriented",
 "Caver drops a pebble into a pocket after waking, pocket bulges slightly, satisfied nod",
 # 5:00 DAY 10 SILENCE
 "Perfectly still underground lake, not a ripple, absolute silence, headlamp reflection",
 "Extreme close-up of the caver's ear and neck, pulse visibly beating, heavy breathing",
 "Caver whips head around at a faint sound, headlamp beam darting across empty rock",
 "Caver sits hugging knees, quietly humming with eyes closed, breath vapor in the light",
 "Caver makes hand shadows on the cave wall with the headlamp, a tired smile",
 "Caver traces shapes in wet mud with a finger, lost in thought",
 # 6:00 DAY 14 CREATURES
 "Headlamp clicks on and reveals a tiny translucent creature crawling across the rock",
 "Close-up of eyeless cave shrimp and tiny springtails, cute, glowing translucent bodies",
 "A perfectly still underground pool, a single drop falls from a stalactite sending slow ripples across the black surface, no animals",
 "Macro shot of an olm, a pale blind cave salamander, moving slowly in clear water",
 "Caver unfolds an empty energy-bar wrapper, looks inside, sighs and smiles wryly",
 # 6:50 DAY 18 FLOOD
 "Low rumble: small stones vibrate on the cave floor, caver's eyes widen",
 "Surface footage: heavy storm rain pours onto a mountain, water streams into a cave entrance",
 "Water level rises fast along a cave wall, swirling and muddy, dramatic lighting",
 "Caver scrambles up a rocky slope to a high ledge, water splashing behind",
 "Headlamp beam highlights old mud lines high on the cave wall, caver points at them",
 "Water stops just below the caver's boots on the ledge, caver exhales in relief",
 "Water slowly recedes, leaving shiny wet rock, calm music mood",
 # 8:00 DAY 25 BODY
 "Caver's gaunt, pale face with overgrown beard lit by a dim headlamp, hollow eyes",
 "Close-up of the caver's pale, waxy skin and cracked lips under headlamp light",
 "Caver squints painfully as the weak headlamp feels as bright as a stadium light",
 "Caver sits with head in hands, then slowly lifts head with determination",
 "Caver stubbornly stacks pebbles into a small tower, determined expression",
 # 8:50 DAY 30 RESCUE
 "Far above, a tiny light moves along the shaft; faint echoing voices; caver looks up hopeful",
 "Rescue team in red helmets rappels down toward the caver, many headlamps forming a line",
 "Rescuer greets caver, caver proudly shows handful of pebbles; rescuer laughs and shakes head",
 "Close-up of a caver's hand-written log book with tally marks, pages damp and warped",
 # 9:30 EXIT + OUTRO
 "Caver exits cave mouth into bright sunlight, rescuer places sunglasses on their face",
 "Doctor hands caver a small bowl of soup instead of a giant feast, gentle humor",
 "Wide aerial shot of the mountains at golden hour, cave entrance a tiny dark spot",
 "Caver stands on a sunlit mountain ridge, wrapped in a blanket, camera pulls back to wide sky",
]

# 5-minute cut: 30 shots x 10 s = 5:00, matched to narration_5min.txt
SHOTS_5MIN = [SHOTS[i] for i in (
    0, 1, 2, 4,          # hook
    6, 7, 9,             # setup
    10, 13, 14,          # day 1
    16, 19, 22,          # day 3
    23, 24, 28,          # day 7
    35, 37, 39,          # day 14
    40, 42, 43, 45,      # day 18
    47, 49, 51,          # day 25
    52, 54, 56, 59,      # day 30 + outro
)]
