def check_syntax(file_path): # Function to run program and check for error message
  try: # Tries to run code by compiling it
    with open(file_path, "r") as f:
      code = f.read()
    compile(code, file_path, "exec")
    print("No syntax errors found.")
  except SyntaxError as e: # Checks if they compilation returns an error value then saves the line with the error to a variable
    print(f"Syntax error found:\n File\"{e.filename}\", line{e.lineno}\n{e.text.strip()}\n ")
    error = e.text.strip()
  return error

def check_keyword(error):
  print(error)

error_line = check_syntax("README.py")
check_keyword(error_line)
