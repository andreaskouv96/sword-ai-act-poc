
import pandas as pd

REQUIRED_SHEETS = [
    "Cover Page",
    "Intro-Instructions",
    "Entity Demographics",
    "Systems Description",
    "Systems Verification",
    "Configuration",
]

def load_workbook(path_or_fileobj):
    xls = pd.ExcelFile(path_or_fileobj)
    return xls

def validate_sheets(xls):
    missing = [s for s in REQUIRED_SHEETS if s not in xls.sheet_names]
    return missing

def load_core_frames(xls):
    frames = {}
    for name in ["Entity Demographics", "Systems Description", "Systems Verification"]:
        try:
            frames[name] = pd.read_excel(xls, name)
        except Exception as e:
            import pandas as pd
            frames[name] = pd.DataFrame({"_error": [str(e)]})
    return frames
