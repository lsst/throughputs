import numpy as np
from lsst.sims.photUtils import BandpassDict


def shorten_wavelengthRange(logthreshold=-250.):
    """
    """
    bandpassdict = BandpassDict.loadTotalBandpassesFromFiles()
    
    for bn in bandpassdict.keys():
        b = bandpassdict[bn]
        mask = np.log10(b.sb) > logthreshold
        minwave = b.wavelen[mask].min()
        maxwave = b.wavelen[mask].max()
        mask = (b.wavelen > minwave) & (b.wavelen < maxwave)
        waves = b.wavelen[mask]
        sb = b.sb[mask]
        fname = 'total_{}.dat'.format(bn)
        print(fname)
        arr = np.zeros(shape=(len(waves), 2))
        arr[:, 0] = waves
        arr[:, 1] = sb
        np.savetxt(fname, arr)
    


if __name__ == '__main__':
    shorten_wavelengthRange(logthreshold=-250.)
