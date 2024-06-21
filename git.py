import os
def git_push():
    os.system('git add .')
    os.system('git commit -m deploy')
    os.system('git push -u origin main')
git = git_push()
print(git)