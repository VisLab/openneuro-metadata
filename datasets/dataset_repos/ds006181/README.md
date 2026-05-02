This repository contains in vivo diffusion MRI data acquired on the Connectome 2.0 scanner (Siemens MAGNETOM Connectom.X, Erlangen, Germany) at the Athinoula A. Martinos Center for Biomedical Imaging. The Connectome 2.0 system features ultra high gradient strength (up to 500 mT/m) and advanced slew rates (600 mT/m/s) for high fidelity microstructural imaging.

All diffusion data were acquired with:

- Pulse width: 6 ms  
- Diffusion times (D): 13 ms and 30 ms  
  - At D= 13 ms, b values = 50, 350, 800, 1500, 2400, 3450, 4750, 6000 s/mm<sup>2</sup>
  - At D = 30 ms, b values = 200, 950, 2300, 4250, 6750, 9850, 13500, 17800 s/mm<sup>2</sup>
- Number of directions: 32 for b < 2300 s/mm<sup>2</sup>; 64 for b > 2300 s/mm<sup>2</sup>
- Echo time: 53 ms  
- Voxel size: 2 mm isotropic  
- GRAPPA = 2 
- SMS = 2  

The dataset includes:
- **Raw diffusion weighted images (DWIs)** and corresponding b=0 images  
- **Metadata** (b values, b vectors, phase encoding directions, pulse width, and diffusion time parameters)  
- **T1 weighted anatomical scan**  
- **Preprocessed DWIs** ([preprocessing scripts](https://github.com/connectome20/diffusion_preproc_C2))

Please note that subject privacy and IRB guidelines were strictly followed in collecting and sharing these data.
