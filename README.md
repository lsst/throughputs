## LSST Throughputs repository ##

The overall version number of the throughputs repo is tied to the
version number of `lsst-pst/syseng_throughputs` which is the
source of the Rubin/LSST throughput curves. Major/minor updates match
the version number there.
Patch updates here indicate changes in throughputs curves other than the
LSST curves, such as adding more reference bandpasses from other surveys.

This repository contains reference throughput curves from various
surveys (Megacam, WISE, SDSS, Johnson UBV and various other telescopes),
together with the expected performance throughput curves for LSST.

The LSST throughput curves are in [baseline](./baseline), with more
information on the curves available there in that [README.md](./baseline/README.md).
If you are only concerned with calculating expected magnitudes for LSST
in various bandpasses, then you should use the 'baseline' throughputs.

The files in 'phosim' are related to the throughputs used in the phosim
simulations. The 'goal' directory holds the throughputs used as goals
for phosim development at the time of tagging (of this SVN directory),
and the 'actual' directory holds the phosim actual throughputs, at the
time of the simulations. These have not been updated since 2010, but are
preserved for historical purposes.

The directory 'atmos' contains various airmass atmospheres, both
without and with (the files ending with _aerosol.dat) aerosols.

More information is available in README files within each directory.


