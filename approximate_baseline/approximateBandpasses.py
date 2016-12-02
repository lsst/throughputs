import os
import numpy as np
from lsst.utils import getPackageDir

def shorten_wavelengthRange(logthreshold=-250.):
    """
    reads in the LSST 'total' bandpasses from the baseline directory
    and only keeps those (wavelength, transmission) values for which
    the transmission is below a given threshold

    Parameters
    ----------
    logthreshold : float, defaults to -250.
        threshold value such that if the log10(transmission) is less
        than logthreshold
    .. note: This mostly deals with the many consecutive zeros in the lsst
    throughputs, a larger value of the logthreshold will make actual cuts
    """
    filedir = os.path.join(getPackageDir('throughputs'), 'baseline')

    for bn in 'ugrizy':
        fname = 'total_{}.dat'.format(bn)
        throughputfile = os.path.join(filedir, fname)
        arr = np.loadtxt(throughputfile)
        mask = np.log10(arr[:, 1]) > logthreshold
        minwave = arr[:, 0][mask].min()
        maxwave = arr[:, 0][mask].max()
        mask = (arr[:, 0] > minwave) & (arr[:, 0] < maxwave)
        arr = arr[mask]
        np.savetxt(fname, arr)
    


if __name__ == '__main__':
    shorten_wavelengthRange(logthreshold=-250.)
