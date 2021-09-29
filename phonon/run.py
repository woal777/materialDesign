import subprocess

for i in range(1, 49):
    subprocess.check_output(
        ['mpirun', '-n 32', ''], stderr=subprocess.STDOUT)