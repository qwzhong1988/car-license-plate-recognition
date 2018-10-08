import git

class git_repo(git.Repo):
    def __init__(self, path, url=None):
        super(git_repo, self).__init__(path)
        try:
            self.remote()
        except:
            print('creating remote add named "origin"!')
            self.create_remote(name='origin', url=url)

    def add_file(self, file_list, commit_msg=':'):
        self.index.add(file_list)
        self.index.commit(commit_msg)
        self.remote().pull()
        self.remote().push()

    def remove_file(self, file_list, commit_msg=';'):
        self.index.remove(file_list, working_tree=False)
        self.index.commit(commit_msg)
        self.remote().pull()
        self.remote().push()

    def untracked_files(self):
        untracked_files = super(git_repo, self).untracked_files
        print(untracked_files)
        return untracked_files

    def update_modified(self, commit_msg=';'):
        self.git.add('-u')    # using git command sytanx directly
        self.index.commit(commit_msg)
        self.remote().pull()
        self.remote().push()



local_repo_dir = r'C:\jupyter\car_palte_recogonition'
git_repo_url = r'https://github.com/liam800/car-license-plate-recognition'

repo = git_repo(local_repo_dir, git_repo_url)
# repo.add_file(['git_python.py'], commit_msg='update files for project')
repo.update_modified('update modification for this file')



