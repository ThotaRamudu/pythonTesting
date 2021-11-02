import click
import sys
import os
import shutil
from git import Repo

@click.command()
@click.option("--repo_path", prompt="Path of the repository", help="Enter the downloaded location of your repository")
@click.option("--branch1", prompt="Enter the first branch name", help="Enter the first branch name")
@click.option("--branch2", prompt="Enter the second branch name", help="Enter the second branch name")
@click.option("--output_directory", prompt="Location to store the file", help="Location to store the changed file")

def diff_branch(repo_path,branch1,branch2,output_directory):
	repo = Repo(repo_path)
	os.makedirs(output_directory, exist_ok = True)
	diffs = repo.commit(branch1).diff(repo.commit(branch2))
	files_changed = [item.a_path for item in diffs]
	for x in files_changed:
		path = os.path.join(repo_path, str(x))
		shutil.copy2(path, output_directory)
		print(path)

if __name__ == '__main__':
    '''
    To start the file

    python diff.py --repo_path <repo_path> --branch1 <first branch name> --branch2 <second branch name> --output_directory <directory path>

    Ex: python diff.py --repo_path /tmp/sample-project --branch1 master --branch2 origin/test --output_directory /tmp/dd

    '''
    diff_branch()

