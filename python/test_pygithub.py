''' Youtube Channel : Asim Code
PyGithub repository example in Python
https://youtu.be/gJPV8-vHDIE
'''
from github import Github
my_git = Github("your_token")
for repo in my_git.get_user().get_repos():
    print(repo.name)

code_repo = my_git.get_repo("asimcode2050/Asim-Code-Youtube-Channel-Code")
contents = code_repo.get_contents("")
for content_file in contents:
    print(content_file)
    

