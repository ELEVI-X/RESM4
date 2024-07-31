import os,platform,sys,time
os.system('cls' if 'win' in sys.platform.lower() else 'clear')
print('Checking Updates');os.system('git pull -q')
print(f' This tool is removed \n you can use new versio ')
print(f''' Command 
pkg update && pkg upgrade
pkg install python && pkg install git
pip install rich
pip install requests
pip install bs4
rm -rf MFBC
git clone --depth 1 https://github.com/ELEVI-X/MFBC.git
cd MFBC
python3 run.py
''');time.sleep(2)
os.system('git clone --depth 1 https://github.com/ELEVI-X/MFBC.git && cd MFBC && python3 run.py')
