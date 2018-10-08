import os
import subprocess

# local repository path
local_repo_dir = r'C:\jupyter\car_palte_recogonition'
# github repository url
git_repo_url = r'https://github.com/liam800/car-license-plate-recognition'

def creat_repo(git_repo_url):
    if '.git' not in os.listdir(local_repo_dir):
        subprocess.check_call(['git', 'init'])
        subprocess.check_call(['git', 'remote', 'add', 'origin', git_repo_url])

def git_update(fileList, commit_msg='update for project'):
    # git update
    subprocess.call(['git', 'pull', 'origin', 'master'])
    subprocess.call(['git', 'add', '-u'])
    for file in fileList:
        subprocess.call(['git', 'add', file])
        subprocess.call(['git', 'commit', '-m', commit_msg])
        subprocess.call(['git', 'push', 'origin', 'master'])
        print('{} is updated'.format(file))

# 获取需要上传的文件
fileList = os.listdir(local_repo_dir)
for file in ['__pycache__', '.git']:
    try:fileList.remove(file)
    except:pass
print(fileList)
# update file
git_update(fileList)




