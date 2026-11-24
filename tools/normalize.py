#!/usr/bin/env python3
"""House-keeping for the LiaScript files of this course (idempotent).

- Quiz attribute comments (<!-- data-hint-button … -->) must stand directly above the quiz itself
  (first option line or matrix header), not above the question paragraph (Templates/CONVENTIONS.md §5).
- The Mermaid import is removed from files that contain no Mermaid block.
"""
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
QUIZ = re.compile(r"^(- \[[(\[][^\]]*[)\]]\]|\[\s*\(.+\)\s*\]\s*$)")
ATTR = re.compile(r"^<!-- data-(hint|solution|show|randomize)[^>]*-->\s*$")
MERMAID_IMPORT = "import:    https://raw.githubusercontent.com/LiaTemplates/mermaid_template/0.1.4/README.md"


def fix(text):
    lines = text.split("\n")
    out, i = [], 0
    while i < len(lines):
        if ATTR.match(lines[i]):
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            if j < len(lines) and not QUIZ.match(lines[j]):
                # find the quiz within the next lines (question paragraph + blank line)
                k = j
                while k < len(lines) and k < j + 8 and not QUIZ.match(lines[k]):
                    k += 1
                if k < len(lines) and QUIZ.match(lines[k]):
                    attr = lines[i]
                    block = lines[i + 1:k]
                    while block and not block[-1].strip():
                        block.pop()
                    out.extend(block)
                    out.append("")
                    out.append(attr)
                    i = k
                    continue
        out.append(lines[i])
        i += 1
    text = "\n".join(out)
    if "```mermaid" not in text:
        text = text.replace("\n" + MERMAID_IMPORT + "\n", "\n").replace("\n\n-->", "\n-->")
    return text


def main():
    files = [Path(a) for a in sys.argv[1:]] or sorted(REPO.glob("AI_in_TVET_II_WiSe_2026_2027/0[1-7]_*/[PS]*.md"))
    for f in files:
        old = f.read_text(encoding="utf-8")
        new = fix(old)
        if new != old:
            f.write_text(new, encoding="utf-8")
            print("fixed", f.relative_to(REPO))


if __name__ == "__main__":
    main()
