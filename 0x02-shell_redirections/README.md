# Shell, I/O Redirections and filter

## Learning Objectives in this project: 

### Shell, I/O Redirection
- I familiarized myself with the commands `head`, `tail`, `find`, `wc`, `sort`, `uniq`, `grep`, and `tr`.
- I learned how to redirect standard output to a file.
- How to get standard input from a file instead of the keyboard.
- How to send the standard output from one peogram to the input of another program.
- How to combine commands and filters with redirections.

### Special Characters
- I learned about special characters.
- I familiarized myself with white spaces, single quotes, doubles quotes, backslash, comments, pipe, command separator, tilde and how and when to use them

### Man Pages
- I learned how to display a line of text.
- How to concantenate files and print on the standard output.
- How to reverse a string
- How to remove sections from each line of files.
- What is the `/etc/passwd` file and what is its format.
- What is the `/etc/shadow` file and what is its format.

# Tasks
- **_0. Hello World_**
	- [0-hello_world](./0-hello_world): Bash script that prints “Hello, World”, followed by a new line to the standard output.

- **_1. Confused smiley_**
	- [1-confused_smiley](./1-confused_smiley): Bash script that displays a confused smiley `"(Ôo)'`.

- **_2. Let's display a file_**
	- [2-hellofile](./2-hellofile): Bash script that displays the content of the `/etc/passwd` file.

- **_3. What about 2?_**
	- [3-twofiles](./3-twofiles): Bash script that displays the content of `/etc/passwd` and `/etc/hosts`.

- **_4. Last lines of a file_**
	- [4-lastlines](./4-lastlines): Bash script that displays the last 10 lines of `/etc/passwd`.

- **_5. I'd prefer the first ones actually_**
	- [5-firstlines](./5-firstlines): Bash script that displays the first 10 lines of `/etc/passwd`.

- **_6. Line #2_**
	- [6-third_line](./6-third_line): Bash script that displays the third line of the file `iacta`.

- **_7. It is a good file that cuts iron without making a noise_**
	- [7-file](./7-file): Bash script that creates a file named exactly `\*\\'"Best School"\'\\*$\?\*\*\*\*\*:)` containing the text `Best School` ending by a new line.

- **_8. Save current state of directory_**
	- [8-cwd_state](./8-cwd_state): Bash script that writes into the file `ls_cwd_content` the result of the command `ls -la`. If the file `ls_cwd_content` already exists, it should be overwritten. If the file `ls_cwd_content` does not exist, create it.

- **_9. Duplicate last line_**
	- [9-duplicate_last_line](./9-duplicate_last_line): Bash script that duplicates the last line of the file `iacta`
		- The file `iacta` will be in the working directory

- **_10. No more javascript_**
	- [10-no_more_js](./10-no_more_js): Bash script that deletes all the regular files (not the directories) with a `.js` extension that are present in the current directory and all its subfolders.

- **_11. Don't just count your directories, make your directories count_**
	- [11-directories](./11-directories): Bash script that counts the number of directories and sub-directories in the current working directory.
		- The current and parent directories should not be taken into account
		- Hidden directories should be counted

- **_12. What’s new_**
	- [12-newest_files](./12-newest_files): Bash script that displays the 10 newest files in the current directory.
	Requirements:
		- One file per line
		- Sorted from newest to the oldest
