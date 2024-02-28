#Check my data through Colab :)

#Import the library to mount Google Drive
from google.colab import drive

#Mount Google Drive to access files there
drive.mount('/content/drive')

!sudo apt-get install -y bcftools
!sudo apt-get install -y vcftools
!sudo apt-get install -y samtools

#Set the directory for the outputs
output_dir = "/content/drive/My Drive/Path/to/project/"

#Check...
!ls "/content/drive/My Drive/"

#Defining the name of the COVID data file for analysis
my_data = "variant_data.vcf.gz"
!echo {my_data}

#Check summary statistics
!bcftools stats {my_data} > {my_data}_stats.txt

#Filtering and saving specific information from the generated statistics
grep "number of records:" {my_data}_stats.txt > {my_data}_stats.records.txt
grep "number of SNPs:" {my_data}_stats.txt > {my_data}_stats.SNPs.txt
grep "number of indels:" {my_data}_stats.txt > {my_data}_stats.indels.txt

#Assess mapping qualities and coverage
samtools flagstat {my_data} > {my_data}_flagstat.txt
samtools coverage -m -o {my_data}_coverage.txt {my_data}