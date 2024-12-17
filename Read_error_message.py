def read_error_msg():   # function to access terminal and print error message to file
  try:
    pass
  except ValueError:
    print("There was a value error")

def check_syntax(file_path):
  try:
    with open(file_path, "r") as file:
      code = file.read()
    compile(code, file_path, "exec")
    print("No syntax errors found.")
  except SyntaxError as error:
    print(f"Syntax error found:\n File\"{error.filename}", line{error.lineno}\n{error.text.strip()}\n {'^':>{error.offset}}")

check_syntax("README.md")
