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

#### Committing Changes To origin/master
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

