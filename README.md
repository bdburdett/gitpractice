# gitpractice

Procedure
0. `git init` first time starting the repo
1. `git status` (check for any updates to the repo)
    1.a. if red then there is a need to push
    1.b. if green the ready to proceed
2. `git add [FILENAME]` (or if wanting to add all the files just run `git add .`)
3. `git status` to make sure you have the correct files green and ready to commit
4. `git remote add origin [REPONAMEfromGITHUB]` Do this just once when first making commits if working in same repo
5. `git commit -m "a helpful comment"`
6. `git push -u origin main`
    6.a it will ask for username and password
    6.b. password needs to be a PAT. in Github settings>developer tools> generate a token 
    6.c. use the new generated token for the password when prompted


#--Errors I have ran into--#
The error message "src refspec main does not match any" is typically seen when using the git version control system. It indicates that the git command you are trying to use is trying to reference a branch or commit named "main" but that no such branch or commit exists in the local repository.

To resolve this error, you can try specifying the correct branch or commit name, or you can use the git branch command to list all of the branches in your local repository and make sure you are using the correct name. Alternatively, you can use the git clone command to download a fresh copy of the repository, which should include the "main" branch if it exists in the remote repository.

To add a "main" branch to your local Git repository, you can use the git checkout command with the -b option to create a new branch named "main" and switch to it in one step. For example:

`git checkout -b main`
This will create a new branch named "main" based on the current branch you are on, and switch to it. You can then use git add and git commit to add your changes to the new branch and commit them to the repository.

Alternatively, if you have already created the "main" branch on the remote repository and you want to download it to your local repository, you can use the git clone command followed by the URL of the remote repository. This will download a copy of the remote repository to your local machine, including the "main" branch.

`git clone https://github.com/my-username/my-repository.git`
Once the repository has been cloned, you can use git checkout to switch to the "main" branch.

`git checkout main`
This will switch to the "main" branch and you can start working on it and committing your changes to the local repository.


Note: any error about being out of sync with local and remote try `git pull origin main --rebase`