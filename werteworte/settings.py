import os.path
import glob
conffiles = glob.glob(os.path.join(os.path.dirname(__file__), 'settings', '*.py'))
conffiles.sort()
for f in conffiles:
    absfile = os.path.abspath(f)
    exec(compile(open(absfile, "rb").read(), absfile, 'exec'), globals(), locals())
