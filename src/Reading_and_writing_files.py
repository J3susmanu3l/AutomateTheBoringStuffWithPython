#Reading and writing Files:

# File paths are different for different operating systems like windows, linux and macos
# to specify the file path in directory we use \ for windows and / for linux and macos
# ALthough we can use / for windows also but it is not recommended
# it is better to use the path() function to specify the file path
# path() function returns a string that is good for all operating systems


from pathlib import Path
file_path = Path('spam', 'bacon', 'eggs')
print(file_path)







