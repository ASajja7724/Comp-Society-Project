def read_error_msg():   # function to access terminal and print error message to file
  try:
    pass
  except ValueError:
    print("There was a value error")

def check_syntax(file_path):
  try:
    with open(file_path, "r") as f:
      code = f.read()
    compile(code, file_path, "exec")
    print("No syntax errors found.")
  except SyntaxError as e:
    print(f"Syntax error found:\n File\"{e.filename}\", line{e.lineno}\n{e.text.strip()}\n ")

check_syntax("README.py")
