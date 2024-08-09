import os,platform
bit = platform.architecture()[0]
if bit == '32bit':
    pass
elif bit == '64bit':
    import RESM64
else:print(f' Rerun command again')
