import glob, os, random, secrets

PEOPLE = ["Ota", "Ivana", "Bára", "Ondra", "Mirka", "Babí Hela", "Jitka", "Miloš", "Dan", "Áňa"]
COUPLES = [("Ota", "Ivana"), ("Ondra", "Mirka"), ("Jitka", "Miloš"), ("Dan", "Áňa")]
BASE_URL = "https://dan-sprucek.github.io/secret-santa/"

FORBIDDEN = {(a, b) for a, b in COUPLES} | {(b, a) for a, b in COUPLES}

def ok(giver, receiver):
    return giver != receiver and (giver, receiver) not in FORBIDDEN

while True:
    receivers = random.sample(PEOPLE, len(PEOPLE))
    if all(ok(g, r) for g, r in zip(PEOPLE, receivers)):
        break

here = os.path.dirname(os.path.abspath(__file__))
for old in glob.glob(os.path.join(here, "????.html")):
    os.remove(old)

codes = set()
for giver, receiver in zip(PEOPLE, receivers):
    code = secrets.token_hex(2)
    while code in codes:
        code = secrets.token_hex(2)
    codes.add(code)
    with open(os.path.join(here, f"{code}.html"), "w", encoding="utf-8") as f:
        f.write(
            '<!doctype html><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1">'
            '<body style="font:2em sans-serif;text-align:center;margin-top:30vh">'
            f"Kupuješ dárek pro: {receiver}\n"
        )
    print(f"{giver:10} -> {receiver:10} {BASE_URL}{code}.html")
