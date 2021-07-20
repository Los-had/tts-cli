from tts import speak, save_file
import sys

args = sys.argv[1::]
content = sys.argv[2]
#save = sys.argv[3]
#filename = sys.argv[4]

if args[0] == '-t':
    speak(content)
#elif args[1] == '':
#    speak(content)
#elif args[2] == '':
#    pass
#elif args[3] == '':
#    pass
else:
    pass