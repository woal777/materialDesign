#!/opt/miniconda3/bin/python
import os

buf = os.popen('qstat -u "*"')
out: str = buf.read()
arr = [r.split()[7:9] for r in out.split('\n')][2:-1]
a = {'6142.q@node05':64,'7501.q@node04': 64, '2695v3.q@node01': 28, '2695v3.q@node02': 28,
     '8870v3.q@node03': 72, 'master.q@JKL-PNU1':4}
arr = [r for r in arr if len(r) >1]

for i, j in arr:
    a[i] -= int(j)

print(a)
