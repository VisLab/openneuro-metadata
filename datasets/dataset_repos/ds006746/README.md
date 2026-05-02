# Raw MR data from 'Reconfiguration of brain-wide neural activity after early life adversity'.

# Overview
This dataset contains 3D RARE Mn(II)-enhanced MR images of 24 mice (12 C57BL/6J with standard rearing at JAX; 12 C57BL/6J with limited bedding and nesting at Caltech) from across a series of longitudinal conditions. Images were acquired on an 11.7T Bruker Avance DRX500 across variousscanning sessions/conditions: 1) before MnCl<sub>2</sub> injection (0.3 mmol/kg, IP) (pre-Mn); 4) ~23h after after injection and before an acute threat exposure (pre-TMT); 3) ~24-26h after injection and 30min to 2h after acute threat exposure (post-TMT); 4) 8 days after threat exposure and before a second MnCl<sub>2</sub> injection (0.3 mmol/kg, IP) (D9pre-Mn); and 5) ~24h after the second injection (D9-post). Please see [Uselman et al. (2025) _bioRxiv_](https://doi.org/10.1101/2023.09.10.55705) for experimental procedure and the associated [Bearer Lab GitHub Repo](https://github.com/bearerlab/memri-ela-vs-std) for code used in processing and analysis.

Image Info: Raw Bruker files were converted to NIfTI (.nii) via the [NIfTI](https://imagej.net/ij/plugins/nifti.html) plug-in in ImageJ (1.54g [DOI](10.1038/nmeth.2089)). Header information (voxel units and geometry) from a template in the data set were copied to all other images using _fslcpgeom_ from [FSL](https://web.mit.edu/fsl_v5.0.10/fsl/doc/wiki/FSL.html) (_fslcpgeom_). For upload to OpenNeuro, NII images were converted to NII_GZ via _fslchfiletype_. Scan metadata (json files) were created manually from Bruker files (Paravision 4.0).


__Authors__: Taylor W. Uselman, Russell E. Jacobs, Elaine L. Bearer<sup>*</sup>

_*Corresponding Author_: 
-   Email: elaine.bearer@gmail.com
-   ORCID: https://orcid.org/0000-0002-8390-8529


__How to Acknowledge:__ Please cite our papers [Uselman et al. (2025)](https://doi.org/10.1101/2023.09.10.55705) and [Uselman, Barto et al. (2020) _NeuroImage_](https://doi-org/10.1016/j.neuroimage.2020.116975). Also see the [Bearer Lab GitHub Repo](https://github.com/bearerlab/memri-ela-vs-std) for additional methodological details on image processing and analysis. 

Not all images from Uselman, Barto et al. (2020) are provided in this dataset. Please email the authors to request access to those additional images.

__Acknowledgements:__ The authors acknowledge the scientific and technical assistance provided by students, staff, and faculty at the Biological Imaging Center and Beckman Institute at California Institute of Technology. Data collection was supported by NIH R01MH096093, the Beckman Institute at Caltech, and the Harvey Family Endowment at the University of New Mexico. 