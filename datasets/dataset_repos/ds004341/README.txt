# Loris Naspi, 22 October 2019

# List of relevant files

# behavioral_data          : data of behavioral task acquired during the encoding phase
# code                     : code for running anatomical normalisation and functional smoothing (over all participants)
# code_loris*              : temporary files that need deleting after preprocessing is finished. The different files are reduntant
                             but needed for running different batches of participants in parallel.
# derivatives              : the results of preprocessing in BIDS format
# pilot                    : participant "zero": it refers to the analisis run prior to starting testing
# sub-*                    : a copy of renamed raw data.
# dataset_description.json : it contains two mandatory fields: "Name": "semantic_encoding",
                                                               "BIDSVersion": "1.2.0",
                                         one optional field:   "Authors": "Loris Naspi", "Paul Hoffman", "Alexa Morcom".
# log_step1_prepareImages_10-Oct-2019.txt : Results of DICOM to NIFTI conversion from scanner, files have been renamed, stored in BIDS format, 
                                            3 dummy scans were removed
