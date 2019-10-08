import os


def main():
    with open('md.gin') as f:
        cart = False
        velo = False
        n = 1
        over = []
        with open('new.gin', 'w') as g:
            for l in f:
                if cart:
                    if 'temp' in l:
                        cart = False
                        g.write(l)
                        continue
                    if float(l.split()[4]) > 50:
                        over.append(n)
                        n += 1
                        continue
                    n += 1
                if velo:
                    if '#' in l:
                        velo = False
                        g.write(l)
                        continue
                    if int(l.split()[0]) in over:
                        continue
                    else:
                        print(sum(i < int(l[:7]) for i in over), l[:7], over)
                        l = f'{int(l[:7]) - sum(i < int(l[:7]) for i in over)}' + l[7:]
                if 'cart' in l:
                    cart = True
                if 'velo' in l:
                    velo = True
                g.write(l)


if __name__ == '__main__':
    os.chdir(
        '/home/jinho93/oxides/perobskite/lanthanum-aluminate/slab/nvt.para.6/step/1.5and0.5/nve/3.nve_maxtemp/again')
    main()
