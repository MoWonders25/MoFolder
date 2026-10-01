# Shot list for "What If You Got Trapped in the Deepest Cave on Earth for 30 Days?"
# Each shot = one Seedance 2.0 clip (10 s, 1080p, 16:9). 60 shots = 10:00.
STYLE = ("Bright, colorful 2D flat cartoon explainer animation, thick clean outlines, "
         "saturated colors, simple expressive character with big eyes, smooth motion, "
         "consistent character: young explorer in orange jacket, yellow helmet with headlamp, "
         "blue backpack. No text, no logos, no subtitles. ")

SHOTS = [
 # 0:00 HOOK
 "Explorer dangles on a rope inside a vast dark vertical cave shaft, headlamp flickering, camera slowly pushes in on worried face",
 "Close-up of the rope fraying strand by strand, then snapping; explorer drops out of frame into darkness",
 "Cutaway diagram: five skyscrapers stacked vertically beside a cave shaft that goes even deeper, camera tilts down",
 "Explorer sits on a rock ledge holding a dead radio, shakes it, sparks, sighs; tiny pile of food bars beside them",
 "Calendar pages flip rapidly from 1 to 30 floating in darkness, ending with a glowing question mark",
 "Dramatic slow zoom into black cave mouth on a mountain, eerie glow inside",
 # 0:60 SETUP
 "Cartoon globe spins and zooms into the Caucasus mountains near the Black Sea",
 "Side cutaway of a mountain revealing a giant branching cave going extremely deep, camera tracks downward",
 "Team of cartoon cavers rappelling down a long shaft over several days, sun and moon icons cycling",
 "Explorer lands at the very bottom of the cave, looks up at a tiny dot of light far above",
 # 1:40 DAY 1 DARK
 "Explorer switches off headlamp; screen goes almost completely black with only two blinking cartoon eyes visible",
 "Explorer waves hand in front of face in total darkness, rim-lit faintly, confused expression",
 "Three flashlights shown side by side, two fade away leaving one headlamp and a spare battery glowing",
 "Thermometer on cave wall drops to cold, frost appears on explorer's eyebrows, water droplets on jacket",
 "Explorer sits on backpack and wraps in shiny silver emergency blanket, crinkling, shivering stops",
 "Cozy wide shot: small explorer wrapped in silver blanket in huge dark cavern, single dim lamp",
 # 2:40 DAY 3 WATER FOOD
 "Macro shot of water drip falling from a stalactite into explorer's cupped hands, splash in slow motion",
 "Explorer collects drips into a bottle beside a murky puddle marked with a cartoon germ",
 "Underground river flows through a glowing blue cavern, explorer watches from a ledge",
 "Explorer breaks an energy bar into tiny pieces and lines them up neatly on a rock",
 "Animated stomach character grumbling and growing smaller day by day, playful",
 "Explorer takes a tiny nibble of snack, warm glow radiates from chest showing body heat",
 "Explorer looks directly at camera and holds up a question mark sign, inviting the viewer, playful",
 # 3:50 DAY 7 TIME
 "A sun icon fades out and a cartoon clock on the cave wall begins to melt like wax",
 "1960s scientist cartoon with beard sits in a tent inside a cave surrounded by notebooks and a lamp",
 "Scientist emerges from cave into daylight, holding calendar showing a much earlier date, shocked face",
 "Explorer scratches tally marks on cave wall, marks begin to blur and wiggle",
 "Explorer yawns and sleeps, wakes up, unsure; floating clocks show 6h, 16h, 30h spinning",
 "Explorer drops a pebble into a pocket after waking, pocket bulges slightly, satisfied nod",
 # 5:00 DAY 10 SILENCE
 "A sound waveform line across the cave gradually goes completely flat",
 "Close-up of explorer's chest with an animated cartoon heart thumping, sound rings visible",
 "Faint ghostly musical notes float through the cavern and pop like soap bubbles, explorer looks around nervously",
 "Explorer sings with eyes closed, colorful notes fill the dark cave",
 "Explorer acts out a movie scene with hand shadows on cave wall using the headlamp, fun",
 "Explorer draws a dream house in the mud with a stick, thought bubble of a sunny house",
 # 6:00 DAY 14 CREATURES
 "Headlamp clicks on and reveals a tiny translucent creature crawling across the rock",
 "Close-up of eyeless cave shrimp and tiny springtails, cute, glowing translucent bodies",
 "Pale blind cave fish swimming slowly in clear dark water, ripples of light",
 "Cave fish wearing a tiny birthday hat with '100' candles, comedic",
 "Explorer looks at own empty food wrapper, then enviously at the calm fish",
 # 6:50 DAY 18 FLOOD
 "Low rumble: small stones vibrate on the cave floor, explorer's eyes widen",
 "Surface view: storm clouds pour heavy rain onto mountain, water streams into cave entrance",
 "Water level rises fast along a cave wall, swirling and muddy, dramatic lighting",
 "Explorer scrambles up a rocky slope to a high ledge, water splashing behind",
 "Headlamp beam highlights old mud lines high on the cave wall, explorer points at them",
 "Water stops just below the explorer's boots on the ledge, explorer exhales in relief",
 "Water slowly recedes, leaving shiny wet rock, calm music mood",
 # 8:00 DAY 25 BODY
 "Split screen: healthy explorer on day 1 versus pale, thinner explorer with messy hair on day 25",
 "Cartoon vitamin D sun particles fade from the explorer's skin",
 "Explorer squints painfully as the weak headlamp feels as bright as a stadium light",
 "Explorer's mood shown as weather cloud above head switching between sun and rain",
 "Explorer stubbornly stacks pebbles into a small tower, determined expression",
 # 8:50 DAY 30 RESCUE
 "Far above, a tiny light moves along the shaft; faint echoing voices; explorer looks up hopeful",
 "Rescue team in red helmets rappels down toward the explorer, many headlamps forming a line",
 "Rescuer greets explorer, explorer proudly shows handful of pebbles; rescuer laughs and shakes head",
 "Cartoon body clock dial stretching from 24 to 48 hours, gears turning",
 # 9:30 EXIT + OUTRO
 "Explorer exits cave mouth into bright sunlight, rescuer places sunglasses on their face",
 "Doctor hands explorer a small bowl of soup instead of a giant feast, gentle humor",
 "Earth cutaway with a tiny dotted line from the surface barely scratching toward the glowing core",
 "Happy explorer waves goodbye at sunny mountain top, camera pulls back to wide sky",
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
