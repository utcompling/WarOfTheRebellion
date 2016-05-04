import subprocess
import os

replace_dir = "/Users/grant/devel/corpora/wotr/devtest1"

source_dir = "/Users/grant/devel/corpora/wotr/test"

for f in os.listdir(replace_dir):
	replace_fp = os.path.join(replace_dir, f)
	source_fp = os.path.join(source_dir, f)
	subprocess.call(['cp', source_fp, replace_fp])

print "Finished Copying"

