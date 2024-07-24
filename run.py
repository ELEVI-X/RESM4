import os,platform,sys
os.system('cls' if 'win' in sys.platform.lower() else 'clear')
print('Checking Updates');os.system('git pull -q')
bit = platform.architecture()[0]
if bit == '32bit':
    print(f'32Bit coming soon ');exit()
elif bit == '64bit':
    import MFBC
else: print("Tool not supported");exit()
