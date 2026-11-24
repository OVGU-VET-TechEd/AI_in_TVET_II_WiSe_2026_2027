#!/usr/bin/env python3
"""Export the self-learning units as SCORM 1.2 packages for Moodle (elearning.ovgu.de).

  python3 tools/export_scorm.py                    every AI_in_TVET_II_WiSe_2026_2027/*/S*.md
  python3 tools/export_scorm.py path/S03_X.md ...  only these

Same settings as AI in TVET I and Fachdidaktik II: SCORM 1.2, Markdown embedded in the package, mastery score 0
(completion only – completing all 7 units is the pass requirement). Each unit is copied alone into a temporary
folder, because the exporter packs the whole folder of the input. Output: <unit>_SCORM.zip next to the .md file.
"""
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CACHED = Path.home() / ".npm/_npx/793f1c2b5b850f33/node_modules/.bin/liascript-exporter"
EXPORTER = [str(CACHED)] if CACHED.exists() else ["npx", "-y", "@liascript/exporter@3.4.2--2.1.0"]
ORGANIZATION = "OVGU Magdeburg – Ingenieurpädagogik und Didaktik der technischen Bildung"
DURATION = {"S03": "PT3H0M0S", "S06": "PT3H0M0S", "S04": "PT2H0M0S", "S05": "PT2H0M0S"}  # default 90 min


def export(md):
    md = md.resolve()
    target = md.parent / f"{md.stem}_SCORM"
    with tempfile.TemporaryDirectory() as tmp:
        shutil.copy(md, Path(tmp) / md.name)
        cmd = EXPORTER + ["-i", str(Path(tmp) / md.name), "-f", "scorm1.2",
                          "--scorm-embed", "--scorm-masteryScore", "0",
                          "--scorm-organization", ORGANIZATION,
                          "--scorm-typicalDuration", DURATION.get(md.stem[:3], "PT1H30M0S"),
                          "-o", str(target)]
        result = subprocess.run(cmd, capture_output=True, text=True)
    zip_path = target.with_suffix(".zip")
    if result.returncode or not zip_path.exists():
        sys.exit(f"export failed for {md.name}:\n{result.stdout[-2000:]}\n{result.stderr[-2000:]}")
    print(f"wrote {zip_path.relative_to(REPO)} ({zip_path.stat().st_size / 1e6:.1f} MB)")


def main():
    files = [Path(a) for a in sys.argv[1:]] or sorted(REPO.glob("AI_in_TVET_II_WiSe_2026_2027/0[1-7]_*/S0*.md"))
    for md in files:
        export(md)


if __name__ == "__main__":
    main()
