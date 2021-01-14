import os

def get_size(start_path = '.'):
    """
    Returns total size of a path in bytes
    """
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)

    return total_size

if __name__ == "__main__":
    try:
        search_path = input("Enter search path:")
        search_path = os.path.realpath(search_path)
        total = 0
        view_filter = input("Filter size (in MB):")
        view_filter = (int(view_filter) if view_filter else 0)
        print(f"{12*'---'}\n")
        for file in os.listdir(search_path):
            size_mb = get_size(os.path.join(search_path,file))/1000/1024
            if int(size_mb) >= view_filter:
                print(f"{file} [size: {(size_mb if size_mb < 1024 else size_mb/1024):.02f} {('GB' if size_mb >= 1024 else 'MB')}]")
            total += size_mb
        print(f"{12*'---'}\nTotal {(total if total < 1024 else total/1024):.02f} {('GB' if total >= 1024 else 'MB')}")
    except KeyboardInterrupt:
        print('\n')
        print("Goodbye".center(100))