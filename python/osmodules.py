import os

# Get current Dir:
pwd = os.getcwd()
print(pwd)

# Change Dir:
os.chdir("/tmp")

# To list Dirs:
ls = os.listdir("/homes/patelax")
print(ls)

# To make Dirs:
os.mkdir("/tmp/test")

# To make recursively
os.makedirs("/tmp/test1/test2")

# Remove file
os.remove("/tmp/test.txt")

# Remove dir
os.rmdir("/tmp/test1/")

# Remove dir recursively
os.removedirs("/tmp/test1/test2")

# To rename file or dir
os.rename("/tmp/test1.txt","/tmp/test2.txt")

# To get env variable
os.environ

# To get current shell process ID
os.getpid()

# To run shell command
os.system("touch test1")

# Final component of a path
os.path.basename("/etc/test/test.txt")

# To get dir of a path
os.path.dirname("/etc/test/test.txt")

# Join two pathname
os.path.join("/etc/test/", "test.txt")

# Get size
os.path.getsize("/etc/test/test.txt")

# Path exits
os.path.exists("/etc/resolv.conf")

# Check if file exists
os.path.isfile("/etc/resolv.conf")

# pathname refers to an existing directory
os.path.isdir("/etc")

# Symbolic link
os.path.islink("/etc/localtime")

for rootpath, dirpath, filepath in os.walk("/tmp/test1"):
    print(rootpath)


# Search a file: 

path="/etc"
file_search=input("Please enter the filename to search: ")
for rootfile, dirname, filename in os.walk(path):
    for file in filename:
        if file == file_search:  
            print(os.path.join(rootfile, file))


# to join the top level directory with file
for rootfile, dirname, filename in os.walk(path):
    for file in filename:
        print(os.path.join(rootfile, file))


# To find a file:
filename = "Dockerfile"
for rootpath, dirpath, filepath in os.walk("/homes/patelax/pythonapi"):
    for file in filepath:
        if file == filename:
            final = os.path.join(rootpath,file)
            print(final)
            print(os.path.exists(final))
            print(os.path.isfile(final))


            