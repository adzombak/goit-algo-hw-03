import shutil
import sys
from pathlib import Path


def copy_files(source_dir: Path, dest_dir: Path):
    for item in source_dir.iterdir():
        if item.is_dir():
            copy_files(item, dest_dir)
        else:
            file_extension = item.suffix[1:]
            dest_subdir = dest_dir / file_extension
            dest_subdir.mkdir(parents=True, exist_ok=True)
            shutil.copy2(item, dest_subdir)


def main():
    if len(sys.argv) < 2:
        print("You should provide source and destination folder")

    source_dir = Path(sys.argv[1])
    dest_dir = Path('dist') if len(sys.argv) < 3 else Path(sys.argv[2])

    try:
        copy_files(source_dir, dest_dir)
        print("Files are copied")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == '__main__':
    main()
