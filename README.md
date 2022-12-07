# gitpractice

Procedure
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


Note: any error about being out of sync with local and remote try `git pull origin main --rebase`