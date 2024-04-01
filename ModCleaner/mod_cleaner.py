from pathlib import Path


def main():
    root = Path('D:/soft/GoG-Game/Cyberpunk 2077')
    to_remove = [
        'archive/pc/mod',
        'bin/x64/plugins',
        'bin/x64/global',
        'bin/x64/LICENSE',
        'bin/x64/version.dll',
        'bin/x64/winmm.dll',
        'engine/config/base/scripts',
        'engine/tools',
        'r6/cache/modded',
        'r6/config/cybercmd',
        'r6/config/redsUserHints',
        'r6/scripts',
        'r6/tweaks',
        'red4ext'

    ]
    for it in to_remove :
        remove(root / it)

def remove(target: Path):
    """
    Delete "target" (and children).
    CAUTION:  This is dangerous! For example, if target == Path('/'),
    it could delete all of your files.
    """
    if not target.exists() :
        print(f"nothing to remove {target}")
    elif target.is_dir():
        for  i in target.iterdir():        
            remove(i)
        print(f"remove {target}")
        target.rmdir()
    else:
        print(f"remove {target}")
        target.unlink()

if __name__ == "__main__" :
    main()