# Processing report

The script `bismark2report` uses a Bismark alignment report, and optionally further reports of the Bismark suite such as deduplication, methylation extractor (splitting) or M-bias reports to generate a graphical HTML report page.

If several Bismark reports are found in the same folder, a separate report will be generated for each of these, whereby the output filename is derived from the Bismark alignment report file.

`bismark2report` attempts to find optional reports automatically based on the file basename.

!!! abstract "Example reports"

    You can see an example [single-end report](http://www.bioinformatics.babraham.ac.uk/projects/bismark/SE_report.html) and [paired-end report](http://www.bioinformatics.babraham.ac.uk/projects/bismark/PE_report.html).

## Usage

```
bismark2report [options]
```

### Options

- `-o/--output <filename>` (optional)

Name of the output file. If not specified explicitly, the output filename will be derived from the Bismark alignment report file. Specifying an output filename only works if the HTML report is to be generated for a single Bismark alignment report (and potentially additional reports).

- `--dir <directory>` (optional)

Output directory. Default: current directory.

- `--alignment_report FILE` (optional)

If not specified, `bismark2report` attempts to find Bismark report file(s) in the current directory and produces a separate HTML report for each mapping report file. Based on the basename of the Bismark mapping report, `bismark2report` will also attempt to find the other Bismark reports (see below) for inclusion into the HTML report.

!!! note

    Although the option is optional (as bismark can try to detect the filename automatically), including a Bismark alignment report file is mandatory.

- `--dedup_report FILE` (optional)

If not specified, `bismark2report` attempts to find a deduplication report file with the same basename as the Bismark mapping report (generated by `deduplicate_bismark`) in the current working directory.

Including a deduplication report is optional, and using the FILE `none` will skip this step entirely.

- `--splitting_report FILE` (optional)

If not specified, `bismark2report` attempts to find a splitting report file with the same basename as the Bismark mapping report (generated by the Bismark methylation extractor) in the current working directory.

Including a splitting report is optional, and using the FILE `none` will skip this step entirely.

- `--mbias_report FILE` (optional)

If not specified, `bismark2report` attempts to find a single M-bias report file with the same basename as the Bismark mapping report (generated by the Bismark methylation extractor) in the current working directory.

Including an M-Bias report is optional, and using the FILE `none` will skip this step entirely.

- `--nucleotide_report FILE` (optional)

If not specified, `bismark2report` attempts to find a single nucleotide coverage report file with the same basename as the Bismark mapping report (generated by Bismark with the option `--nucleotide_coverage`, or `bam2nuc` directly) in the current working directory.

Including a nucleotide coverage statistics report is optional, and using the FILE `none` will skip this report entirely.
