# NextBrain: A probabilistic histological atlas of the human brain for MRI segmentation

NextBrain is a probabilistic atlas of the human brain using histological sections of five full human hemispheres with manual segmentations.

In this repository, we present the 3D histology reconstructions of the 5 human brain hemispheres using two different stains (LFB and H&E) and the corresponding labelmaps at 0.2mm isotropic resolution. Each stain contains RGB colormaps.

We include the original ex vivo MRI and a look-up-table for visualization (freeview format). From the root directory, you can open a single case in Freeview with the command:

freeview -v sub-001/ses-01/anat/sub-001_ses-01_T2w.nii.gz derivatives/manual_segmentation/sub-001/ses-01/sub-001_ses-01_desc-manual_dseg.nii.gz:colormap=lut:lut=derivatives/manual_segmentation/sub-001/sub-001_lut.txt

For more information about the NextBrain project, please check the project's webpage: https://github-pages.ucl.ac.uk/NextBrain/home