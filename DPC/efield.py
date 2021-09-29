#%%
import matplotlib.pyplot as plt
import dm4reader
import scipy.ndimage as ndimage
import numpy as np

class Circular:
    periodic = True

    def __init__(self, r):
        self.radius = r
        self.fil = np.zeros((2*r+1, 2*r+1))
        a, b = np.arange(-r,r+1,1), np.arange(-r,r+1,1)
        for i in a:
            for j in b:
                if np.sqrt(i**2 + j**2) <= r:
                    self.fil[i+ r,j + r] = 1

    def filtering(self, arr):
        if self.periodic:        
            result = np.zeros([arr.shape[0], arr.shape[1]],dtype=float)
            new_arr = np.concatenate([arr[-self.radius:,:], arr, arr[:self.radius,:]])
            new_arr = np.transpose(new_arr)
            new_arr = np.concatenate([new_arr[-self.radius:,:], new_arr, new_arr[:self.radius,:]])
            new_arr = np.transpose(new_arr)
            for i in range(result.shape[0]):
                for j in range(result.shape[1]):
                    result[i, j] = np.sum(self.fil * new_arr[i:i+2 * self.radius + 1, j:j+2 * self.radius + 1])
        else:
            result = np.zeros([arr.shape[0] - 2 * self.radius, arr.shape[1] - 2 * self.radius],dtype=float)     
            for i in range(result.shape[0]):
                for j in range(result.shape[1]):
                    result[i, j] = np.sum(self.fil * arr[i:i+2 * self.radius + 1, j:j+2 * self.radius + 1])
        
        return result
    
c = Circular(2)


dm4_x = dm4reader.DM4File.open("comx.dm4")
dm4_y = dm4reader.DM4File.open("comy.dm4")
dm4 = [dm4_x, dm4_y]
tags = dm4_x.read_directory()

image_data_tag = tags.named_subdirs['ImageList'].unnamed_subdirs[0].named_subdirs['ImageData']
image_tag = image_data_tag.named_tags['Data']

XDim = dm4_x.read_tag_data(image_data_tag.named_subdirs['Dimensions'].unnamed_tags[0])
YDim = dm4_x.read_tag_data(image_data_tag.named_subdirs['Dimensions'].unnamed_tags[1])
dat = []
for dm in dm4:
    dats = np.array(dm.read_tag_data(image_tag), dtype=np.float)
    dats = np.reshape(dats, (YDim, XDim))
    # Z2 = ndimage.gaussian_filter(dats, sigma=2., order=0)
    dats -= int(np.max(dats) / 2)
    dats = c.filtering(dats)
    plt.imshow(dats, interpolation='gaussian')
    dat.append(dats)
    # dats = np.where(np.abs(dats) < np.max(dats) / 5, 0, dats)
    # plt.imshow(dats, cmap='hot')
    plt.show()
# %%
def ampNphase(dat):
    u = np.array(dat[0], dtype=np.float)
    v = np.array(dat[1], dtype=np.float)
    amp =np.sqrt(u ** 2 + v ** 2)
    # u, v = u / np.max(amp), v / np.max(amp)
    phase = np.arctan(v / u)
    phase[u < 0] = phase[u < 0] + np.pi 
    phase -= np.pi / 2
    return amp, phase

a, p = ampNphase(dat)
plt.imshow(a, cmap='hsv_r')
plt.show()
plt.imshow(p, cmap='hsv_r')
# %%
factor = 2
from matplotlib import cm

a /= np.max(a)

def hsv_plot(rgb, alpha):
    cmap_hsv = cm.get_cmap('hsv')
    new = np.zeros([rgb.shape[0], rgb.shape[1], 4])
    for i in range(rgb.shape[0]):
        for j in range(rgb.shape[1]):
            new[i, j] += cmap_hsv(rgb[i, j] / (2 * np.pi) + 0.5)
            if alpha[i, j] > 1 / factor:
                new[i, j, 3] = 1
            else:
                new[i, j, 3] = factor * alpha[i, j]
    return new

hsv = hsv_plot(p, a)
# %%
plt.imshow(hsv)


#%%

def divergence(field):
    "return the divergence of a n-D field"
    arr = np.gradient(field)
    return np.sum([arr[0][0], arr[1][1]],axis=0)

div = divergence(dat)
# %%
plt.imshow(div)
# %%
