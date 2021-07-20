from tts import speak, save_file
import sys

args = sys.argv[1::]
content = sys.argv[2]
filename = sys.argv[4]
if len(args) < 2:
  print("Insuficient number of arguments")
else:
  if args[0] == '-t':
    speak(content)
  elif args[2] == '-s':
    save_file(content, filename)
  else:
    print("Error! invalid or insuficient arguments.")
