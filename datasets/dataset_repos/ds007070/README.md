# ds005256 - fMRIPrep derivatives

This is a BIDS Derivatives dataset resulting from running fMRIPrep on [ds005256](https://openneuro.org/datasets/ds005256).

## Methods

fMRIPrep documentation can be found on <https://fmriprep.readthedocs.io/>.

A containerized version of fMRIPrep is stored in code/containers/fmriprep_25_1_4.sif. This container was built using

```shell
apptainer build code/containers/fmriprep_25_1_4.sif docker://nipreps/fmriprep:25.1.4
```

Products were generated with the [Slurm](https://slurm.schedmd.com/overview.html) script [`code/run`](code/run). That script uses [Slurm arrays](https://slurm.schedmd.com/job_array.html) to process participants in parallel (one participant per job). Slurm logs (combined `stdout` and `stderr`) are stored in `logs/$SLURM_ARRAY_TASK_ID.log`. Running all participants would entail setting the `array` argument during the call to `sbatch`.

```shell
sbatch --array=0-116 code/run
```

Derivatives were saved in the dataset with `git/git-annex` using [`code/save`](code/save). For example, to save sub-0133, run the following.

```shell
# NOTE: the argument (116) is the SLURM_ARRAY_TASK_ID, not the participant_label
./code/save 116
```

### Defacing

To acheive the highest quality derivatives possible, these derivatives were generated on the raw (that is, not defaced) structural scans (sha: 86007170141050f875acfd6daf802d93bd9a7dac). This processing was committed to branch `main-w-faces`. After all participants were added, a new branch was created,  `main-w-faces-defacing`, and the defaced images were committed to there (see [`code/remove_faces`](code/remove_faces)). The main branch contains references to only defaced files.

### Environment

```shell
$ apptainer --version
apptainer version 1.2.2-2.el8
```

### Caveats

At the time of writing, most fMRIPrep products are not covered by BIDS, and so most of this dataset is covered by a [`.bidsignore`](.bidsignore).
