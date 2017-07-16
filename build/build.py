################################################################################
# build.py
# 2017.07.16 - Base version                                                 aha
################################################################################
import shutil

def write_file(type, title, fileName, fout):
	with open(fileName) as fkeywords:
		fout.write(title)
		for keyword in fkeywords.readlines():
			keyword = keyword.strip()
			keyword = keyword.strip("\n")
			if keyword == "": continue
			fields = keyword.split("|")
			if type == "def":
				if len(fields) > 1:
					fout.write("[" + fields[0] + " | " + fields[1] + "]\n")
					fout.write(fields[0] + "\n")
				else: 
					fout.write("[" + keyword + " | " + keyword + "]\n")
					fout.write(keyword + "\n")
			else:
				if len(fields) > 1:
					keyword = fields[0]
				if len(keyword.split(".")) > 1: continue 
				fout.write(keyword + "=\n")

def main():
	with open("GLSL.DEF") as fin:
		with open("..\GLSL.DEF", "w") as fout:
			fout.write(fin.read())
			write_file("def", ";KeyWords\n", 	"keywords.txt", fout)
			write_file("def", ";Types\n",    	"types.txt",    fout)
			write_file("def", ";Built-In\n", 	"builtin.txt",	fout)
			write_file("def", ";Functions\n", 	"functions.txt",fout)
			
	with open("GLSL.INI") as fin:
		with open("..\GLSL.INI", "w") as fout:
			fout.write(fin.read())
			write_file("ini", "[KeyWords]\n",      "keywords.txt", fout)
			write_file("ini", "[ReservedWords]\n", "types.txt",    fout)
			write_file("ini", "[KeyWords2]\n",     "builtin.txt",  fout)
			write_file("ini", "[KeyWords3]\n", 	   "functions.txt",fout)
	
	
	shutil.copyfile("..\GLSL.DEF", "c:\Program Files (x86)\PSPad editor\Context\GLSL.DEF")
	shutil.copyfile("..\GLSL.INI", "c:\Program Files (x86)\PSPad editor\Syntax\GLSL.INI")
    

if __name__ == "__main__":
    main()
