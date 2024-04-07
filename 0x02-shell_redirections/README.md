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
		- One file per line
		- Sorted from newest to the oldest.

- **_13. Being unique is better than being perfect_**
	- [13-unique](./13-unique): Bash script that takes a list of words as input and prints only words that appear exactly once.
		- Input format: One line, one word
		- Output format: One line, one word
		- Words should be sorted

- **_14. It must be in that file_**
	- [14-findthatword](./14-findthatword): Bash script that displays lines containing the pattern "root" from the file `/etc/passwd`.

- **_15. Count that word_**
	- [15-countthatword](./15-countthatword): Bash script that displays the number of lines that contain the pattern "bin" in the file `/etc/passwd`.

- **_16. What's next?_**
	- [16-whatsnext](./16-whatsnext): Bash script that displays lines containing the pattern "root" and 3 lines after them in the file `/etc/paswd`.

- **_17. I hate bins_**
	- [17-hidethisword](./17-hidethisword): Bash script that displays all the lines in the file `/etc/passwd` that do not contain the pattern “bin”.

- **_18. Letters only please_**
	- [18-letteronly](./18-letteronly): Bash script that displays all lines of the file `/etc/ssh/sshd_config` starting with a letter.
		- Include capital letters as well

- **_19. A to Z_**
	- [19-AZ](./19-AZ): Bash script that replaces all characters `A` and `C` from input to `z` and `e` respectively.

- **_20. Without C, you would live in hiago_**
	- [20-hiago](./20-hiago): Bash script that removes all letters `c` and `C` from input.

- **_21. esreveR_**
	- [21-reverse](./21-reverse): Bash script that reverses its input.

- **_22. DJ Cut Killer_**
	- [22-users_and_homes](./22-users_and_homes): Bash script that displays all users and their home directories, sorted bu users.
		- Based on the `/etc/passwd` file

- **_23. Empty casks make the most noise_**
	- [100-empty_casks](./100-empty_casks): Bash script that finds all empty files and directories in the current directory and all sub-directories.
		- Only the names of the files and directories should be displayed (not the entire path)
		- Hidden files should be listed
		- One file name per line
		- The listing should end with a new line
		- You are not allowed to use `basename`, `grep`, `egrep`, `fgrep` or `rgrep`

- **_24. A gif is worth ten thousand words_**
	- [101-gifs](./101-gifs): Bash script that lists all the files with a `.gif` extension in the current directory and all its sub-directories.
		- Hidden files should be listed
		- Only regular files (not directories) should be listed
		- The names of the files should be displayed without their extensions
		- The files should be sorted by byte values, but case-insensitive (file `aaa` should be listed before file `bbb`, file `.b` should be listed before file `a`, and file `Rona` should be listed after file `jay`)
		- One file name per line
		- The listing should end with a new line
		- You are not allowed to use `basename`, `grep`, `egrep`, `fgrep` or `rgrep`

- **_25. Acrostic_**
	- [102-acrostic](./102-acrostic): Bash script that decodes acrostics that use the first letter of each line.
		- The ‘decoded’ message has to end with a new line
		- You are not allowed to use `grep`, `egrep`, `fgrep` or `rgrep`

- **_26. The biggest fan_**
	- [103-the_biggest_fan](./103-the_biggest_fan): Bash script that parses web servers logs in TSV format as input and displays the 11 hosts or IP addresses which did the most requests.
		- Order by number of requests, most active host or IP at the top
		- You are not allowed to use `grep`, `egrep`, `fgrep` or `rgrep`
