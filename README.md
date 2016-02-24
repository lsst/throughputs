## LSST Throughputs repository##

This repository contains reference throughput curves from various
surveys (Megacam, WISE, SDSS, Johnson UBV and various other telescopes),
together with the expected performance throughput curves for LSST.

The LSST throughput curves are in [baseline](./baseline), with more
information on the curves available there in that [README.md](./baseline/README.md).
If you are only concerned with calculating expected magnitudes for LSST
in various bandpasses, then you should use the 'baseline' throughputs.

The files in 'imsim' are related to the throughputs used in the imsim
simulations. The 'goal' directory holds the throughputs used as goals
for imsim development at the time of tagging (of this SVN directory),
and the 'actual' directory holds the imsim actual throughputs, at the
current time. Please take these with a grain of salt; they could be outdated.

The directory 'atmos' contains various airmass atmospheres, both
without and with (the files ending with _aerosol.dat) aerosols.

More information is available in README files within each directory.


