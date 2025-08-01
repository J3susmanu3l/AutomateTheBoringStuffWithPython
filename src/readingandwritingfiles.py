def path_learning():
    from pathlib import Path
    windows_path = Path('spam') / 'bacon' / 'eggs'
    print(windows_path)
    windows_path_v02 = Path('spam') / Path('bacon/eggs')
    print(windows_path_v02)
    windows_path_v03 = Path('spam') / Path('bacon', 'eggs')
    print(windows_path_v03)

def Access_cwd_and_chdir():
    # in this part of the book it teaches me about how to access and change the current working directory to another location
    
    from pathlib import Path
    import os
    print(Path.cwd())
    os.chdir(Path(r'c:\Users\jesus\OneDrive\Escritorio\AutomateTheBoringStuffWithPython/src'))
    print(Path.cwd())
    # while testing I see that the file location in the terminal changes for the  os.chdir() function, but it actually doesn't 
    # change it in the system. Just in the terminal. It is making me wonder why this is used for.

def specifying_absolute_vs_relative_paths():
    # There are two paths:
    ## the absolut path: always starts with the root folder C: on the three main operating systems
    ## the relative path: which is relative to the program current directory
    pass

def creating_new_directories(): # or folders which is the same as directories. Just different words same meaning
    # I also jsut learned how to create new folders or directories
    
    import os 
    os.makedirs('')

def path_home():
    from pathlib import Path
    print(Path.home())


    














def main():
    Access_cwd_and_chdir():
    path_home()
















if __name__ == '__main__':
    main()