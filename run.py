import os, platform
os.system('cls' if 'win' in sys.platform.lower() else 'clear')
print('Checking Updates');os.system('git pull')
bit = platform.architecture()[0]
if bit == '32bit':
    print(f'32Bit coming soon ');exit()
elif bit == '64bit':
    import HENTAI
else: print("Tool not supported");exit()
