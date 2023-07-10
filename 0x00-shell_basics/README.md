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
	
