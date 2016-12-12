import os
import numpy as np

def shorten_wavelengthRange(logthreshold=-250.):
    """
    reads in the LSST 'total' bandpasses from the baseline directory
    and only keeps those (wavelength, transmission) values for which
    the transmission is below a given threshold

    Parameters
    ----------
    logthreshold : float, defaults to -250.
        threshold value such that wavlength, transmission pairs are dropped if
        the log10(transmission) is less than logthreshold
    .. note: This mostly deals with the many consecutive zeros in the lsst
    throughputs, a larger value of the logthreshold will make actual cuts
    """
    here = os.path.abspath(__file__)
    dirname = os.path.dirname(here)
    packageDir = os.path.split(dirname)[0]
    filedir = os.path.join(packageDir, 'baseline')
    for bn in 'ugrizy':
        fname = 'total_{}.dat'.format(bn)
        throughputfile = os.path.join(filedir, fname)
        outfileName = os.path.join(dirname, fname)
        arr = np.loadtxt(throughputfile)
        mask = np.log10(arr[:, 1]) > logthreshold
        minwave = arr[:, 0][mask].min()
        maxwave = arr[:, 0][mask].max()
        mask = (arr[:, 0] > minwave) & (arr[:, 0] < maxwave)
        arr = arr[mask]
        if os.path.abspath(outfileName) == os.path.abspath(throughputfile):
            raise ValueError('Not allowed to write to baseline throughputs')
        np.savetxt(outfileName, arr)


if __name__ == '__main__':
    shorten_wavelengthRange(logthreshold=-250.)
