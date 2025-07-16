# data-engineering-toolkit

Project on Using Git Hub 

This project aims to empower an individual to learn and implement basic skills and knowledge of using github for version control, continuous development and integration.

This involves creating a repository, cloning the repository to a local machine. Setting up global development environment features to efficient version control.

Documentation- Github has numerous commands and rulesets necessary for version control, continuous development integration.
For this project, you can create the main repository on github and clone the repository to the a local machine using Git clone https://github.com/Bunmi-J/data-engineering-toolkit (replace the url with your giturl)
Configure the Git ignore file - You can create a .gitignore file in your repository's root directory to tell Git which files and directories to ignore when you make a commit. To share the ignore rules with other users who clone the repository, commit the .gitignore file in to your repository.

Set up branch protection rules on GitHub for the main branch to require pull requests before merges. On Github , navigate to your repository seettings, under code and automation, select branches. Then click on Add branch Ruleset, configure which rules to apply. By default, Block force pushes and restrict deletions are automatically ticked. You can tick a pull request before merging and other rules to apply.

Create a pull request to make contribution - You can create a pull request to propose or merge changes you have made to a branch or fork and ask someone to review the proposed changes.


The project adopted branching strategy using Gitflow model. This involves creating ‘Main’ branch for stable, production-ready code. ‘Develop’ branch for integration and sFeature branches (feature/branch-name) for new features or scripts.
Branches in this projects are Main, Develop, feature branches (cleansing, transformation and loadscripts branch) for functions to cleanse, transform and load.


