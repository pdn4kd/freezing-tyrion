#Converting 4 FITS images to 400x400 PNGs.
ds9 pnyu28101_DR7.fits -width 400 -height 400 -zoom to fit -zscale -colorbar no -saveimage png apnyu28101_DR7.png -exit
ds9 residual.pnyu28101_DR7_a.fits -width 400 -height 400 -zoom to fit -zscale -colorbar no -saveimage png apnyu28101_DR7_r.png -exit
ds9 pnyu28101_S82.fits -width 400 -height 400 -zoom to fit -zscale -colorbar no -saveimage png apnyu28101_S82.png -exit
ds9 residual.pnyu28101_S82_a.fits -width 400 -height 400 -zoom to fit -zscale -colorbar no -saveimage png apnyu28101_S82_r.png -exit
cp apnyu*png ~/plotting
