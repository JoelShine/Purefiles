'''
This program is for making the developers work easier, that is this program will create a sample
program in the programming language that they want.
'''
import os
import sys

print("Welcome to \'Purefiles\'. What language do you choose ? [Press \'Ctrl+C\' or type \'exit\' to quit the program]\n\n")
print("Available Languages are : PYTHON, JAVA, HTML, C, C++ \n")

try:

	while True:
		lang = input('Your Language choice > \n').lower().strip()

		if lang == "python":
			print("What is the name of your python file ?\n")
			choice = input('> ')

			new_file = open(f"{choice}.py", 'w')

			new_file.write("\'\'\'\n")
			new_file.write("Creator Name        :\n")
			new_file.write("Project Name        :\n")
			new_file.write("Project Description :\n")
			new_file.write("\'\'\'\n")
			new_file.write("print(\"Hello World\")")
			new_file.close()

			print("")
			print("Successfully created your python file. Happy Coding in your favourite code editor.\n")

		elif lang == "java":
			print("What is the name of your java file ?\n")
			choice = input('> ')

			new_file = open(f"{choice}.java", 'w')

			new_file.write("/**\n")
			new_file.write("* Write a description of class hello here.\n")
			new_file.write("*\n")
			new_file.write("* @author (your name)\n")
			new_file.write("* @version (a version number or a date)\n")
			new_file.write("*/ \n\n")
			new_file.write("import java.util.*;\n\n\n")
			new_file.write(f"public class {choice}\n")
			new_file.write("{\n")
			new_file.write("	public static void main(String[]args)\n")
			new_file.write("	{\n")
			new_file.write("			System.out.println(\"Hello World\");\n")
			new_file.write("	}\n")
			new_file.write("}")
			new_file.close()

			print("")
			print("Successfully created your java file. Happy Coding in your favourite code editor.\n")

		elif lang == "html":
			print("What is the name of your html file ?\n")
			choice = input('> ')
			os.mkdir('js')
			os.mkdir('css')

			new_file = open(f"{choice}.html", 'w')

			new_file.write("<!doctype html>\n\n")

			new_file.write("<html lang=\"en\">\n")
			new_file.write("<head>\n")
			new_file.write("  <meta charset=\"utf-8\">\n\n")
			new_file.write(f"  <title>{choice}</title>\n")
			new_file.write(f"  <meta name=\"description\" content=\"{choice}\">\n")
			new_file.write(f"  <meta name=\"author\" content=\"{choice}\">\n\n")
			new_file.write(f"  <link rel=\"stylesheet\" href=\"css/styles.css?v=1.0\">\n\n")
			new_file.write("</head>\n\n")
			new_file.write("<body>\n")
			new_file.write("  <script src=\"js/scripts.js\"></script>\n")
			new_file.write("</body>\n")
			new_file.write("</html>")
			new_file.close()

			js_file = open(f"js/scripts.js", 'w')
			js_file.close()

			css_file = open(f"css/styles.css", 'w')
			css_file.close()

			print("")
			print("Successfully created your html file. Happy Coding in your favourite code editor.\n")

		elif lang == "c":
			print("What is the name of your c file ?\n")
			choice = input('> ')

			new_file = open(f"{choice}.c", 'w')

			new_file.write("#include <stdio.h>\n")
			new_file.write("#include <stdlib.h>\n\n")
			new_file.write("int main() {\n")
			new_file.write("	printf(\"Hello World.\\n\");\n")
			new_file.write("	return 0;\n")
			new_file.write("}")
			new_file.close()

			print("")
			print("Successfully created your c file. Happy Coding in your favourite code editor.\n")

		elif lang == "c++" or lang == "cpp":
			print("What is the name of your c++ file ?\n")
			choice = input('> ')

			new_file = open(f"{choice}.cpp", 'w')

			new_file.write("#include <iostream>\n")
			new_file.write("#include <string>\n")
			new_file.write("using namespace std;\n\n")
			new_file.write("int main() {\n")
			new_file.write("	cout << \"Hello World.\";\n")
			new_file.write("	return 0;\n")
			new_file.write("}")
			new_file.close()

			print("")
			print("Successfully created your c++ file. Happy Coding in your favourite code editor.\n")

		elif lang == "exit" or lang == "close" or lang == "quit":
			print("Thanks for trying out \'Purefiles\'. Happy Coding !!!")
			sys.exit()

		else:
			print("Invalid Language. Try again.")

except KeyboardInterrupt:
	print("Thanks for trying out \'Purefiles\'. Happy Coding !!!")
	sys.exit()
