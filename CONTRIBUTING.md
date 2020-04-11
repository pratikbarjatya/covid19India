# How To: Fork a GitHub Repository & Submit a Pull Request

## 1. Forking the Repository
Assuming you’re using GitHub, this step is easy. 
Just find the repository you’re contributing to and press the Fork button in the upper Right. 
This will create an exact copy of the repository (and all of its branches) under your own username.

## 2. Clone your new fork locally
GitHub will automatically redirect you to the forked repository under your username. 
This is the repository you need to clone to your local development environment, not the original. 
Grab the URL GitHub provides under the green “Clone or Download” button and plug it into the command below.

## 3. Track the original repository as a remote of the fork
Once you’ve forked a repository, changes to the original (or “upstream”) repository are not pushed to your fork. 
We need to tell the new repository to follow changes made upstream to keep it fresh via something called a remote.

Switch directories to the forked repository you just cloned and run the following commands. 
Replace the last part of the first line with the original repository clone URL 
— similar to the how you grabbed the URL in step 2, but this isn’t the one with your username.

This links the fork back to the original repository as a remote, which we’ll name upstream, and then fetch it.

```git remote add --track master upstream git@github.com:pratikbarjatya/covid19India.git```

```git fetch upstream```

## 4. Create a new branch for your changes
It’s possible to make changes directly to the master branch, but this might break things down the road for complicated reasons.
It’s best to checkout a new branch for each change/improvement you want to make

```git checkout -b <branch_name> upstream/master```

## 5. Make your changes!
This is either the easiest part or the hardest part, depending on how you look at it. 
At this point, you’re isolated in the new branch you just created, and it’s safe to open whatever text editor or IDE you use and go wild.

## 6. Add, commit, and push the changes
You’re probably used to these commands. Add the files you’ve changed and commit them with a descriptive message.

```git add .```

```git commit -m "Fix/Add new changes to bla bla file"```

The one difference is the branch you’re pushing to. You likely usually push to master, 
but in this case, we’re pushing to the branch with the name you created in step 4.

```git push -u origin <branch_name>```

## 7. Submit your pull request
You’re now all ready to submit the improvement you’ve made to the project’s maintainers for approval.
Head over to the original repositories Pull Requests tab,
and you should see an automatic suggestion from GitHub to create a pull request from your new branch.
