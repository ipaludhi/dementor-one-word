import os

WORD = "dementor"

# Gate self-check (1-30 chars, exactly one word, no whitespace): entry text unchanged.
assert 1 <= len(WORD) <= 30 and WORD.split() == [WORD] and WORD == WORD.strip()

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/tmp/makefun-out")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(WORD)
