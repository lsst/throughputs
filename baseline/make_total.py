from lsst.sims.catalogs.measures.photometry.Bandpass import Bandpass

common_components = ['detector.dat', 'm1.dat', 'm2.dat', 'm3.dat', 
                     'lens1.dat', 'lens2.dat', 'lens3.dat', 'atmos.dat']

filterlist = ['u', 'g', 'r', 'i', 'z', 'y3', 'y4']

for f in filterlist:
    bandpass = Bandpass(wavelen_max=1200)
    components = common_components + ['filter_' + f + '.dat',]
    bandpass.readThroughputList(components)
    bandpass.writeThroughput('total_' + f + '.dat')

