For each subject (seventeen in total), there are five files given:
1) Data.nii.gz: the dMRI data after preprocessing including topup, eddy, and skule removing.
2) bvecs: bvecs after preprocessing
3) bvals: b values of the dMRI data
4) mrtrix_peaks.nii.gz: the peaks of fiber orientation maps extracted from dMRI
5) bundle_masks_10.nii.gz: the annotation of ten white matter tracts, and the list of these tracts is:
    bundles = ['CST_left', 'CST_right', 'FPT_left', 'FPT_right', 'OR_left', 'OR_right', 'POPT_left', 'POPT_right', 'UF_left', 'UF_right']
