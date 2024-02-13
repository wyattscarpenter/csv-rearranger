CSV-REARRANGER
by Wyatt S Carpenter
for Kitanda

A CSV file is a bunch of values, seperated by commas. It is commonly used as a format for spreadsheets. Each line of a CSV file is a row of the spreadsheet. The commas in the row seperate the columns of the spreadsheet.

Csv-rearranger is a program that rearranges one csv (input.csv) file into another (output.csv), based on a specification csv file (transform.csv).

You can use this program by putting a csv file called "input.csv" into this folder, then running rearranger.py (click on it).
A file called output.csv will be produced according to the specification in transform.csv.

transform.csv describes where the cells will be in the output file.
A cell id consists of the row number and the column letter, like 1A, 2F, or 37AAA.
If the value of a cell in transform.csv is a valid cell id, the corresponding cell in input.csv will be copied into output.csv.
If the value of a cell in transform.csv is NOT a valid cell id, the value will be copied directly into output.csv. This can be useful if you would like to include in output.csv a constant value (such as a price or formula) that is not included in input.csv.

THIS PROGRAM REQUIRES YOU TO HAVE PYTHON INSTALLED ON YOUR COMPUTER.
IF YOU DO NOT HAVE PYTHON INSTALLED, PLEASE VISIT https://www.python.org/getit/
IF YOU AREN'T SURE, TRY RUNNING THE PROGRAM AND SEE IF ANYTHING HAPPENS.

EXAMPLE:

the example input.csv provided with this project is
	1,2,3,
	4,5,6,

the example transform.csv provided with this project is
	2C,2B,
	2A,1C,
	1B,1A,

when rearranger.py is run, output.csv will be produced. It will be:
	6,5,
	4,3,
	2,1,
