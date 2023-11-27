# mplot
A custom made gnuplot based plotter for scientific data and image diffs

### Requirements:
* gnuplot
* python3

### Usage:
<code>mplot -a|--argument [value] ...<br>
Arguments:<br>
-i|--input [value] - input file containing data to be plotted<br>
-a|--axes - enable axis labels (XYZ)<br>
-d|--diff - special mode for image diffing, requires files: reference, first, [second]. Computes MSE, PSNR, SSIM, MAE and relMSE<br>
-s|--save [file] - save output to file as PNG<br>
-p|--psave [file] - save output to file as PNG and leave window open<br>
-m|--mode [value] - plotter mode, select one of the following:<br>
</code>

#### Modes:
* simple2d - standard plot<br>
* heat2d - 2D heat map, requires 3 columns<br>
* vector2d - 2D vector plot from 3D coords, (a, b): xa,ya,za,xb,yb,zb, aka two points<br>
* vecdist2d - 2D vector plot from 3D coords, as vector2d, with distance label, file format: x1,y1,z1,x2,y2,z2,dist<br>
* simple3d - standard splot<br>
* simpal3d - 3D colored point plot, requires x,y,z,c<br>
* vector3d - 3D vector plot, requires (a, direction) aka point and vector direction<br>
* vecpal3d - 3D colored vector plot, requires (a, direction, c) aka point, vector direction and single value<br>
* heat3d - 3D heat map, requires 4 columns sorted by X value with blank lines between different values<br>

