For "normal" LSST baseline evaluations, use the files in "baseline".

 Note that while this is our current baseline performance,
 it represents our current idealized view of LSST behavior.
 It does include an average degradation over time due to
 contaminants on the surfaces.

The files in 'imsim' are related to the throughputs used in the imsim
simulations. The 'goal' directory holds the throughputs used as goals
for imsim development at the time of tagging (of this SVN directory),
and the 'actual' directory holds the imsim actual throughputs, at the
current time. Take these with a grain of salt; they could be outdated.

Megacam and sdss should be self-explanatory, but hold total system
throughputs for megacam and SDSS, as published by those telescopes.

The directory 'atmos' contains various airmass atmospheres, both
without and with (the files ending with _aerosol.dat) aerosols.

More information is available in README files within each directory.

If you are only concerned with calculating expected magnitudes for LSST
in various bandpasses, then you should use the 'baseline' throughputs.

