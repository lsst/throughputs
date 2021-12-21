import os
import numpy as np

def shorten_wavelengthRange(logthreshold=-250., savefile=True):
    """
    reads in the LSST 'total' bandpasses from the baseline directory
    and only keeps those (wavelength, transmission) values for which
    the transmission is below a given threshold. If the transmission values
    drop below the threshold at wavelengths between the min and max wavelength
    where the transmission is above the threshold, such (wavelength, transmission)
    points are included as well.

    Parameters
    ----------
    logthreshold : float, defaults to -250.
        threshold value such that wavelength, transmission pairs are dropped if
        the log10(transmission) is less than logthreshold
    .. note: This mostly deals with the many consecutive zeros in the lsst
    throughputs, a larger value of the logthreshold will make actual cuts
    """
    here = os.path.abspath(__file__)
    dirname = os.path.dirname(here)
    packageDir = os.path.split(dirname)[0]
    filedir = os.path.join(packageDir, 'baseline')

    throughputs = []
    for bn in 'ugrizy':
        fname = 'total_{}.dat'.format(bn)
        throughputfile = os.path.join(filedir, fname)
        outfileName = os.path.join(dirname, fname)
        arr = np.loadtxt(throughputfile)
        mask = np.log10(arr[:, 1]) > logthreshold
        minwave = arr[mask][:, 0].min()
        maxwave = arr[mask][:, 0].max()

        # prevents patchy wavelengths
        mask = (arr[:, 0] >= minwave) & (arr[:, 0] <= maxwave)
        arr = arr[mask]
        throughputs.append(arr)
        if savefile:
            if os.path.abspath(outfileName) == os.path.abspath(throughputfile):
                raise ValueError('Not allowed to write to baseline throughputs')
            np.savetxt(outfileName, arr)

    return throughputs

if __name__ == '__main__':
    shorten_wavelengthRange(logthreshold=-250.)
