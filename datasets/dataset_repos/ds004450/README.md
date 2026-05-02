
# Executive Function
To find out more about this study, you can examine the documentation and scan protocols[here](https://pennlinc.github.io/executivefunction/).

This repository contains a set of
[BIDS-compatible](https://bids.neuroimaging.io/) datasets with T1s, two rest runs
and corresponding functional maps for three subjects. Both .nii.gz and .json
files are available for each of these, along with a dataset_description.json, as well as their 
fMRIPrep derivatives.


### Information about Files: 
|FileType                                                              |Counts|EchoTime|EffectiveEchoSpacing|FlipAngle|HasFieldmap|KeyGroupCount|Modality|MultibandAccelerationFactor|NSliceTimes|ParallelReductionFactorInPlane|PartialFourier|PhaseEncodingDirection|RepetitionTime|TotalReadoutTime|UsedAsFieldmap|
|----------------------------------------------------------------------|------|--------|--------------------|---------|-----------|-------------|--------|---------------------------|-----------|------------------------------|--------------|----------------------|--------------|----------------|--------------|
|datatype-anat_suffix-T1w                                              |3     |0.0029  |                    |8        |FALSE      |3            |anat    |                           |0          |2.0                           |1             |                      |2.5           |                |FALSE         |
|acquisition-fMRIdistmap_datatype-fmap_direction-AP_fmap-epi_suffix-epi|3     |0.08    |0.00051             |90       |FALSE      |3            |fmap    |                           |60         |                              |1             |j-                    |7.03          |0.045           |TRUE          |
|acquisition-fMRIdistmap_datatype-fmap_direction-PA_fmap-epi_suffix-epi|3     |0.08    |0.00051             |90       |FALSE      |3            |fmap    |                           |60         |                              |1             |j                     |7.03          |0.045           |TRUE          |
|datatype-func_run-1_suffix-bold_task-restbold                         |3     |0.03    |0.00051             |52       |TRUE       |3            |func    |6.0                        |60         |                              |1             |j                     |0.8           |0.045           |FALSE         |
|datatype-func_run-2_suffix-bold_task-restbold                         |3     |0.03    |0.00051             |52       |TRUE       |3            |func    |6.0                        |60         |                              |1             |j                     |0.8           |0.045           |FALSE         |

### Provenance: 

These files were obtained from Flywheel, defaced and run through fMRIPrep. 
