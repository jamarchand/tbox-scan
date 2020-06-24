#Tbox-scan
#Version 1.0.0.
#Updated June 24, 2020
#By Merrick Pierson Smela and Jorge A. Marchand
#Harvard Medical School - Department of Genetics
#George M. Church Lab


#Input flags
infernal_out='INFERNAL.txt'
model='RF00230.cm'
input_file=''
log_file='tbox-scan_log.txt'
output_file='out.csv'
verbose='False'
silence='False'

#User help message
print_usage() {
  printf "
  
  tbox-scan v1.0.0 (June 2020)

  Usage: tbox-scan -f <Input FASTA file> [-options]

  Scan a fasta sequence file for T-boxes and predict specifier & T-box sequence.
            -- Default: Will use INFERNAL with RFAM00230 covariance model with basic output
            -- Example: tbox-scan  -f input.fa -o output_file.csv -v
  Dependencies: INFERNAL, cmsearch, python3, pandas.

            
  Options
    -f <file>  : input FASTA <file>
    -o <file>  : save final results in <file> as .csv
    -i <file>  : save INFERNAL output predictions to .txt <file>
                    default: INFERNAL.txt
    -l <file>  : save a .txt log <file> of pipeline output
    -m <model> : search for mitochondrial tRNAs
                    default: RF00230.cm (RFAM)
    -v         : save verbose output
    -s         : silence console output
    -h         : print out summary of available options


"

}


#Flag handling
while getopts 'f:o:ilmvsh' flag; do
  case "${flag}" in
    f) input_file="${OPTARG}" ;;
    o) output_file="${OPTARG}" ;;
    i) infernal_out="${OPTARG}" ;;
    l) log_file="${OPTARG}" ;;
    m) model="${OPTARG}" ;;
    v) verbose='True' ;;
    s) silence='True' ;;
    h) print_usage
        exit 1 ;;
    *) print_usage
       exit 1 ;;
  esac
done


#Try running using either python or python3
python3 tboxscnr.py $input_file $output_file $model $infernal_out $log_file $verbose $silence || python tboxscnr.py $input_file $output_file $model $infernal_out $log_file $verbose $silence || echo Error: T-box scanning pipeline failed. Check proper usage, dependencies, and auxilliary files. && print_usage
