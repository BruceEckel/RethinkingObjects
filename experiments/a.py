import io
import os
import sys

def app():
  print("Hello World!")

def a1_main():
  orig_stdout = sys.stdout
  test_output = io.StringIO()
  sys.stdout = test_output
  try:
    app()
  finally:
    sys.stdout = orig_stdout
  assert f"Hello World!{os.linesep}" == test_output.getvalue()

def a2_main():
  print("Running a2_main")
  assert True
