These are the expected throughput curves for LSST.

They include the average value of expected losses over time.
These are generated from a version of SYSENG_THROUGHPUTS
(see https://github.com/lsst-pst/syseng_throughputs), indicated
in the header of each throughput curve.

The atmosphere files contain aerosols. The darksky file is zenith, dark sky,
already appropriately normalized.

The total_[ugrizy].dat files contain the total system throughput, including atmosphere
 (an X=1.2 atmosphere, including aerosols).
The hardware_[ugrizy].dat files contain the hardware throughput, without atmosphere.

If you need individual components, the files
detector.dat
lens1.dat
lens2.dat
lens3.dat
filter_[ugrizy].dat
m1.dat
m2.dat
m3.dat
describe each stage of the hardware. Combine them all to recreate the hardware_*.dat files.

Add atmos_std.dat (an X=1.2) atmosphere to recreate the total_[ugrizy].dat files.
The atmos_10.dat represents an X=1.0 atmosphere.
These two atmosphere files do contain aerosols.

-Lynne Jones @rhiannonlynne