__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'

def clean_cache():
    import os
    import shutil
    
    path = os.getcwd()
    directory = 'cache'
    path_dir = os.path.join(path, directory)
    if os.path.exists(path_dir):
        shutil.rmtree(path_dir)
    os.mkdir(path_dir)

def cache_zip(path_zip_file, cache_dir):
    from zipfile import ZipFile
    
    ZipFile(path_zip_file).extractall(cache_dir)

def cached_files():
    import os

    list_files= []

    for root, dirs, files in os.walk('cache'):
        for file in files:
            p=os.path.join(root,file)
            list_files.append((os.path.abspath(p)))
    return list_files
        
def find_password(list_files):
    for item in list_files:
        with open(item, 'r') as read_obj:
            for line in read_obj:
                if 'password' in line:
                    return line[10:-1]
    return False

            