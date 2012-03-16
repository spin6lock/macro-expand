#-*- coding:utf8 -*-
import argparse

mark = "#macro "
def unfold_macro(filename):
	with open(filename, 'r') as fh_in, \
		open(filename + '.out', 'w') as fh_out:
		lines = fh_in.readlines()
		for line in lines:
			pos = line.find(mark) 
			if pos == -1:
				fh_out.write(line)
				continue
			macro_filename = extract_macro_filename(pos, line)
			write_macro(fh_out, macro_filename, pos)	

def extract_macro_filename(pos, line):
	start = pos + len(mark)
	end_pos = line[start].find(" ")
	if end_pos == -1:
		filename = line[start:]
	else:
		filename = line[start:end_pos]
	return filename.strip()

def write_macro(fh_out, macro_filename, indent=0):
	indentation = " " * indent
	with open(macro_filename, 'r') as fh_in:
		lines = fh_in.readlines()
		lines = [indentation + line for line in lines]
		fh_out.writelines(lines)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='This is a \
		simple program to expand macro in python source code')
	parser.add_argument('sourcefile', action='store')
	namespace = parser.parse_args()
	unfold_macro(namespace.sourcefile)
