Open diffusion MRI and connectivity data for epilepsy and surgery: The IDEAS II release

Epileptic seizures are generated in cerebral networks that propagate ictal and interictal activity. The structure of cerebral networks underpinning epileptic activity can be inferred from diffusion-weighted MRI (DWI). However, publicly available DWI data in individuals with epilepsy are scarce, and processing is technically challenging due to scan-specific artifacts, limiting research progress. Here, we release raw DWI data from 216 individuals with epilepsy and 98 healthy controls. Subject identifiers align with our previous data release (IDEAS), which includes T1-weighted and FLAIR MRI, surgical details, and long-term seizure outcomes after surgery. Preprocessing reduced distortions and artifacts, while fully processed data include diffusion metric maps in native and template space. We also provide parcellated structural connectomes using multiple atlases and connectivity measures. To illustrate the utility of this IDEAS II data, we replicated ENIGMA consortium findings, observing widespread reductions of fractional anisotropy, particularly ipsilateral to the area of seizure onset. We further demonstrate localised abnormality, and network connectivity using streamline tractography in a patient who subsequently underwent temporal lobe resection. This open dataset offers a comprehensive resource to advance research on structural connectivity and surgical outcomes in epilepsy.

Link to preprint: https://arxiv.org/abs/2602.09852 (Accepted publication in press at Epilepsia). 

This release on OpenNeuro includes only raw T1w, FLAR and diffusion MRI scans. The key difference in the IDEAS II data, compared to IDEAS I is the addition of diffusion MRI. Fully processed data, including resection masks and other demographic information can be found at the following locations: https://www.cnnp-lab.com/ideas-data Below, is a unified list of all data available across the two IDEAS data releases.

•	Raw T1w, FLAIR and diffusion MRI scans organised in BIDS format. Nifti and json descriptors included: https://figshare.com/s/4ec743d20cf1c41ed01d 

•	Resection masks in native space of the T1w scan. https://figshare.com/s/476b37fd883c14f50324 

•	Raw T1w and FLAIR data, additional to minimally processed diffusion MRI data. https://figshare.com/s/e8c80939dafc5eead4b1 

•	Raw T1w and FLAIR data, additional to fully processed diffusion MRI data. Fully processed data includes tensor maps in native space, MNI-152 space, and connectomes. https://figshare.com/s/2dbae1fbfe72f7e66e1a 

•	Freesurfer surface and volumetric reconstructions derived from the shared T1w scan https://figshare.com/s/b13b8bb41390d3f7a088 

•	Freesurfer thickness, volume, and surface areas for the Desikan-Kiliany parcellation https://figshare.com/s/010142dd51e37ba4e4e2

•	Clinical and demographic metadata  https://figshare.com/s/bab70268afeb1071202b 

•	Table indicating the percentage of each brain region in the Desikan-Kiliany atlas subsequently resected by surgery. https://figshare.com/s/097ba0e254e36f0eee52  

•	Freesurfer thickness, volume, and surface areas for the Desikan-Kiliany parcellation, z-scored against normative controls post-combat. https://figshare.com/s/8c086fc295a75f85e628 

For updates please subscribe to the mailing list: https://www.jiscmail.ac.uk/cgi-bin/wa-jisc.exe?SUBED1=IDEAS-DATA&A=1

If you use T1w or FLAIR scans, please cite the following publication:
Taylor, Peter N., et al. "The imaging database for epilepsy and surgery (IDEAS)." Epilepsia 66.2 (2025): 471-481.

If you use the diffusion MRI scans, please cite the following publication:
Taylor, Peter N., et al. “Open diffusion MRI and connectivity data for epilepsy and surgery: The IDEAS II release.” Epilepsia [in press] (2026)

If you use the resection masks please cite the following publication:
Simpson, Callum., et al. “Automated generation of epilepsy surgery resection masks: The RAMPS pipeline” Imaging Neuroscience. (2025) 3 IMAG.a.147
