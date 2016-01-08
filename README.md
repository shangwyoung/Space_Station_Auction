# Space Station Auction
This is intended as a contest a la the critter tournament, except it would be open to all students, not just 150, and I like the idea of moving away from a combat-oriented contest.  

The game will involve an a sequence of auctions in which each player attempts to acquire modules (cards) with which to build the best starbase in the galaxy. (The starbase theme is pretty irrelevant.  We can make it about making an awesome amusement park, or robot butler, or whatever you folks want.)  

Bidding agents will be written in Python.  That keeps it open to students who have only had 150 (or even 140, if we get around to offering that again).  

## Oberlin College Winter Term 2016
Tom Wexler  
Jun Li  
Nicholas Music  
Sage Vouse  
Aaron Young  
Luxing Zhang  

## Version Control

#### Get Started
To get started, clone this repository on your local machine:

        git clone https://github.com/aarony422/Space_Station_Auction.git

#### Branching
Please do not commit directly to the master branch, unless it's absolutely necessary and ok to do so.

Start a feature branch and do enough testing. When you're done, submit a pull request on github.

Use the following command to make a new branch:

        git checkout -b [new-branch-name]
        
You can also checkout a branch someone else created:

        git checkout [branch-name]

#### Status
Check the status of your working directory:

        git status
        
to see the status of the files in your working directory.

#### Staging and Committing Changes Locally
After you've made changes and want to stage your changes:

        git add [filename]
        
or if you want to stage all files changed:

        git add -A
        
To commit your changes locally:

        git commit -m "[commit message]"

#### Pushing to Remote Repository
To push your changes to the branch you created remotely to origin (github):

        git push origin [branch-name]

#### Submitting a Pull Request
After you've done enough testing to the code you've written on a separate branch, and believe it's ready to be committed to origin/master, you first need to merge the up-to-date version of master into your branch.

To merge changes in master to your current branch, checkout your branch and do:

        git pull
        git merge master

To see the differences between the current branch you are on and origin/master, do:

        git diff origin/master
        
To view difference between two branches, do:

        git diff [branch1] [branch2]

For example, you can do:

        git diff origin/master origin/[my-branch]

If merge conflicts exist, fix them manually. Then, test your branch again to make sure every works perfectly now with master merged in.

When you're done committing all your changes, and pushed the changes to your branch remotely, you can go to github and submit a merge request by pressing the button

#### Other Useful Commands
###### git revert
If you committed changes, and decided you didn't want them anymore, do the following to revert the changes you just committed:

        git revert HEAD

This is considered a "safe" undo because the changes you reverted is still preserved in your project history.

###### git reset 
The reset command has many uses, and can potentially cause you to lose your work. So use with care!

To remove files from staging area, but leave the working directory unchanged:

        git reset [filename]

or use the following to remove ALL files from staging area:

        git reset
        
**Danger Zone**  
To reset the staging area and working directory to match most recent commit:

        git reset --hard
        
This erases ALL uncommitted changes! (Which might be something you'd like to do)

#### Suggestions
###### Pull first
Always make sure you are working with the most up-to-date version of your branch. Others might have made changes and pushed remotely when you were gone! So pull potential changes from origin before working.

###### Commit often
Once you have written and tested a working portion of your feature, you should commit the code locally and remotely

###### Never push directly to origin/master
Submit a pull request for any changes you want committed to the master branch so people can review your code!

