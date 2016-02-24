# v1.0 atmospheres from David Burke, MODTRAN, March 1, 2010.

The files here without _aerosol do NOT contain aerosols.
The files ending with _aerosol.dat do include aerosols, added using
the python script  lsst-pst/syseng_throughputs/python/addAerosols.py. 

The atmospheres here were produced with MODTRAN by David Burke to
conform to typical conditions expected at LSST's site at Cerro Pachon.
Each atmosphere has similar ratios of water vapor, ozone, and scattering components,
but different airmasses --- the airmass is represented by the number at the end
of the filename.
For example: atmos_10.dat is a 1.0 airmass atmosphere, while atmos_25.dat is a 2.5 X atmos.

atmos_12_hiwater.dat and atmos_12_lowater.dat are attempts (by Lynne Jones) to take the
modtran outputs from David Burke and use these to munge a 30% higher and lower water component.
These were created by taking the 1.0 and 1.6 airmass atmospheres and using the water components
from those atmospheres instead of the water component from the 1.2 airmass atmosphere.
(this should probably be redone properly with MODTRAN).

-Lynne Jones @rhiannonlynne