# https://youtu.be/g1hm8tr-5KY
import os
file_path ="/var/log/syslog"
file_stat = os.stat(file_path)
print(f"File mode: {file_stat.st_mode}" )
print(f"File inode: {file_stat.st_ino}")
major = os.major(file_stat.st_dev)
minor = os.minor(file_stat.st_dev)
print(f"Device ID: {file_stat.st_dev}")
print(f"\tMajor: {major}")
print(f"\tMinor: {minor}")
print(f"Number of hard links: {file_stat.st_nlink} ")
print(f"Owner User ID: {file_stat.st_uid}")
print(f"Group ID: {file_stat.st_gid}")
print(f"File Size: {file_stat.st_size}")
print(f"Is a symlink: {os.path.islink(file_path)}")
print(f"Absolute Path: {os.path.abspath(file_path)}")
print(f"File exists: {os.path.exists(file_path)}")
print(f"Parent directory: {os.path.dirname(file_path)}")
