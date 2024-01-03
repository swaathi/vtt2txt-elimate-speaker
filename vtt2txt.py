import webvtt
import re

SPEAKER_PATTERN = r"KAKARLA, SWAATHI \(PGT\)"
    
def is_swaathi_speaking(caption):
    re.search(SPEAKER_PATTERN, caption.raw_text, re.IGNORECASE)

with open('fulltext/rohini_fulltext.txt', 'w') as file:
  for caption in webvtt.read('vtt/rohini.vtt'):
    if not is_swaathi_speaking(caption):
      file.write(str(caption.text) + '\n')
