import numpy as np
with open('/home/jinho93/slab/LAO/nvt/old/md.trg', 'rb') as f:
    dump = np.fromfile(f, dtype=np.float32, count=32)
    print(dump)

