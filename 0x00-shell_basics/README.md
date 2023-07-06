# Shell basics

This project took me on an introductory crash course in the Shell. I learned how to navigate directories using `cd`, `pwd`, `ls`, how to look around using `ls`, `less`, and `file`, and how to manipulate files with `cp`, `mv`, `rm`, and how to create directories with `mkdir`. I also practiced working with the `type`, `whch`, `help`, and `man` commands, implementing wildcards, reading man pages, creating links with `ln`, and using keyboard shortcuts in Bash.

## Tasks

- **_0. Where am I?_**
	- [0-current_working_directory](./0-current_working_directory): Bash script that prints the absolute pathname of the current working directory.

- **_1. What's in there?_**
	- [1-listit](./1-listit): Bash script that displays the content list of the current directory.

- **_2. There is no place like home_**
	- [2-bring_me_home](./2-bring_me_home): Bash script that changes the working directory to the user's home directory:wq
.

- **_3. The long format_**
	- [3-listfiles](./3-listfiles): Bash script that displays current directory contents in a long format.

- **_4. Hidden files_**
	- [4-listmorefiles](./4-listmorefiles): Bash script that displays current directory contents, including hidden files (starting with `.`) in a long format.

- **_5. I love numbers_**
	- [5-listfilesdigitonly](./5-listfilesdigitonly): Bash script that displays current directory contents
		- Long format
		- User and group IDs displayed numerically
		- Hidden files 

- **_6. Welcome_**
	- [6-firstdirectory](./6-firstdirectory): script that creates a directory named `my_first_directory` in the /tmp/ directory.

- **_7. Betty in my first directory_**
	- [7-movethatfile](./7-movethatfile): script that moves the file betty from `/tmp/` to `/tmp/my_first_directory`.

- **_8. Bye bye Betty_**
	- [8-firstdelete](./8-firstdelete): script that deletes the file `betty`.
		- The file `betty` is in `/tmp/my_first_directory`.

- **_9. Bye bye My first Directory_**
	- [9-firstdirdeletion](./9-firstdirdeletion): script that deletes the directory `my_first_directory` that is in `/tmp` directory.

- **_10. Back to the future_**
	- [10-back](./10-back): script that changes the working directory to the previous one.

- **_11. Lists_**
	- [11-lists](./11-lists): script that lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the `/boot` directory (in this order), in long format.

- **_12. File type_**
	- [12-file_type](./12-file_type): script that prints the type of the file named `iamafile`. The file `iamafile` will be in the temporary `/tmp` when we run your script.

- **_13. We are symbols, and inhabit symbols_**
	- [13-symbolic_link](./13-symbolic_link13-symbolic_link): this script creates a symbolic link to `/bin/ls`, named `__ls__`. The symbolic link should be created in the current working directory
	
- **_14. Copy HTML files_**
	- [14-copy_html](./14-copy_html): this script copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer thzn the versions in the parent of the working directory.

- **_15. Let's move_**
	- [100-lets_move](./100-lets_move): bash script that moves all files beginning with an uppercase letter to the directory `/tmp/u`.
	- Assume that the directory `/tmp/u` will exist when we run your script.

- **_16. Clean Emacs_**
	- [101-clean_emacs](./101-clean_emacs): bash script that deletes all files in the current working directory that end with the character `~`.

- **_17. Tree_**
	- [102-tree](./102-tree): bash script that creates the directories `welcome/`, `welcome/to/`, `welcome/to/school` in the current directory.

- **_18. Life is a series of commas, not periods_**
	- [103-commas](./103-commas): bash script that lists all the files and directories of the current directory, separated by commas (`,`).
		- Directory names should end with a slash (`/`)
		- Files and directories starting with a dot (`.`) should be listed
		- The listing should be alpha ordered, except for the directories `.` and `..` which should be listed at the very beginning
		- Only digits and letters are used to sort; Digits should come first
		- You can assume that all the files we will test with will have at least one letter or one digit
		- The listing should end with a new line

- **_19. File type: School_**
	- [school.mgc](./school.mgc): bash script that creates a magic file `school.mgc` that can be used with the command `file` to detect `School` data files. `School` data files always contain the string `SCHOOL` at offset 0.
