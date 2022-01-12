


with open("mypapers.md") as file:
    lines = file.readlines()
    out = []
    prev = ""
    for l in lines:
        if l.startswith("http") and not prev.startswith("http") and not prev.startswith("[") and prev.strip():
            out += f"[{prev.strip()}]({l.strip()})\n"
            prev = ""
        else:
            out += prev
            prev = l
    if prev.strip():
        out += prev

    with open("mypapers.parsed.md", "w+") as fout:
        for l in out:
            fout.write(l)



