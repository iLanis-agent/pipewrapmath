import json, math

def jsnum(x):
    return int(x) if isinstance(x, float) and x == int(x) else x
def plural(n, word, form=None): return str(jsnum(n)) + " " + (word if n == 1 else (form or word + "s"))
def fmt(x): return str(jsnum(x))
def round1(x): return jsnum(math.floor(x * 10 + 0.5) / 10)

TUBE_M = 1
TAPE_W_M = 7
DRIP_L_H = 0.18

def wrap_plan(lengthM):
    if not (lengthM > 0):
        return {"error": "the length must be positive"}
    tubes = math.ceil(lengthM / TUBE_M)
    if lengthM <= 2: verdict = "a faucet-sock job"
    elif lengthM <= 10: verdict = "a crawlspace afternoon"
    else: verdict = "a whole-house wrap"
    return {"tubes": tubes, "verdict": verdict}

def tape_plan(lengthM):
    if not (lengthM > 0):
        return {"error": "the length must be positive"}
    watts = round1(lengthM * TAPE_W_M)
    if lengthM <= 5: verdict = "a faucet run"
    elif lengthM <= 20: verdict = "a wall run"
    else: verdict = "a perimeter run"
    return {"watts": watts, "verdict": verdict}

def drip_plan(faucets, hours):
    if not (faucets > 0) or not (hours > 0):
        return {"error": "the faucets and the hours must be positive"}
    liters = round1(faucets * hours * DRIP_L_H)
    if liters <= 2: verdict = "a kettle's worth"
    elif liters <= 10: verdict = "a bucket's worth"
    else: verdict = "a tub's worth"
    return {"liters": liters, "verdict": verdict}

def render_wrap(r, lengthM):
    return ("Your " + fmt(lengthM) + " m of pipe at a labeled " + fmt(TUBE_M) + " m a tube asks "
            + plural(r["tubes"], "tube") + " of foam - " + r["verdict"] + ".")

def render_tape(r, lengthM):
    return ("Your " + fmt(lengthM) + " m of pipe at a labeled " + fmt(TAPE_W_M) + " W per meter draws "
            + fmt(r["watts"]) + " W of heat tape - " + r["verdict"] + ".")

def render_drip(r, faucets, hours):
    return ("Your " + plural(faucets, "faucet") + " dripping over " + fmt(hours) + " hours at a labeled "
            + fmt(DRIP_L_H) + " L an hour each " + ("lets" if faucets == 1 else "let") + " " + fmt(r["liters"]) + " L through - " + r["verdict"] + ".")

cases = []
def add(fn, f, rf, args):
    r = f(*args)
    c = {"fn": fn, "args": args, "result": r}
    if "error" not in r: c["render"] = rf(r, *args)
    cases.append(c)

for a in [[3],[1],[2],[12],[8],[0.5],[25],[10],[0],[6]]:
    add("wrapPlan", wrap_plan, render_wrap, a)
for a in [[3],[0.5],[10],[20],[30],[5],[15],[1],[0],[25]]:
    add("tapePlan", tape_plan, render_tape, a)
for a in [[1,8],[2,8],[1,12],[4,8],[6,10],[1,4],[10,12],[3,6],[0,8],[2,0]]:
    add("dripPlan", drip_plan, render_drip, a)
json.dump(cases, open("expected.json", "w"), separators=(",", ":"))
print(len(cases), "cases")
