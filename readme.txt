put a csv file called "input.csv" into this folder.

transform.csv describes where the cells will be in the output file.

run rearranger.py (click on it). a file called output.csv will be produced according to the specification in transform.csv.

For instance, imagine input.csv is
  29,hello,kitanda

imagine transform is
  1A,1C,=1A+1C,22

output.csv will be
  29,kitanda,=1A+1C,22