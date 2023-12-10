import os
import sys

input_bismark = sys.argv[1]  # 输入trimmed_fastq文件的文件夹的路径
output_bismark = sys.argv[2]  # 输出文件的路径

for file in os.listdir(input_bismark):
    if file.endswith("_folder"):  # 选择基因组文件
        genome_file = os.path.join(input_bismark, file)
        print("The genome folder is"f"{genome_file}")
        # 对原本的基因组文件进行预处理
        cmd = (f"bismark_genome_preparation "
               f"--path_to_aligner=/System/Volumes/Data/Users/guojiayi/DMR_prediction/bowtie2-2.5.2-macos-x86_64"
               f" --verbose {genome_file}")
        os.system(cmd)

for trimmed_file in os.listdir(input_bismark):
    if trimmed_file.endswith("_1.fq") and trimmed_file.replace("_1", "_2") in os.listdir(input_bismark):
        data_2 = trimmed_file.replace("_1", "_2")  # 生成配对文件路径
        input_data1 = os.path.join(input_bismark, trimmed_file)
        input_data2 = os.path.join(input_bismark, data_2)
        # 调用Bismarck进行分析
        cmd = f"bismark -1 {input_data1} -2 {input_data2} {genome_file} -o {output_bismark}"
    elif trimmed_file.endswith(".fastq"):  # 单端测序
        input_data = os.path.join(input_bismark, trimmed_file)
        cmd = f"bismark -fastq -L 30 -N 1 --non_directional {genome_file} {input_data} -o {output_bismark}"
        os.system(cmd)
print("bismark has completed please check" f"{output_bismark}")