# 0x01. Shell Permissions

In this project, I learned about Linux file permissions and how to use commands: `chmod`, `sudo`, `su`, `chown`, `chgrp`, and more. 

## Tasks
- **_0. My name is Betty_**
	- [0-iam_betty](./0-iam_betty): script that switches current user to `betty`.

- **_1. Who am I_**
	- [1-who_am_i](./1-who_am_i): script that prints the username of the current user.

- **_2. Groups_**
	- [2-groups](./2-groups): script that prints all groups the user is a part of.

- **_3. New owner_**
	- [3-new_owner](./3-new_owner): script that changes the owner of the file `hello` to the user `betty`.

- **_4. Empty!_**
	- [4-empty](./4-empty): script that creates an empty file called hello.

- **_5. Execute_**
	- [5-execute](./5-execute): script that adds execute permission to the owner of the file `hello`

- **6. Multiple permissions_**
	- [6-multiple_permissions](./6-multiple_permissions): script that adds execute permission to the owner and the group owner, and read permission to other users, to the file `hello`.

- **_7. Everybody!_**
	- [7-everybody](./7-everybody): script that adds execute permission to the owner, the group owner and other users, to the file `hello`.

- **_8. James Bond_**
	- [8-James_Bond](./8-James_Bond): script that sets the permissions to the file `hello` as follows:
		- Owner: no permission at all
		- Group: no permission at all
		- Other users: all the permissions

- **_9. John Doe_**
	- [9-John_Doe](./9-John_Doe): script that sets the mode of the file hello to:
```
-rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello
```

- **_10. Look in the mirror_**
	- [10-mirror_permissions](./10-mirror_permissions): script that sets the mode of the file `hello` the same as `olleh`'s mode.

- **_11. Directories_**
	- [11-directories_permissions](./11-directories_permissions): script that adds execute permission to all subdirectories of the **current directory** for the owner, the group owner and all other users.

- **_12. More directories_**
	- [12-directory_permissions](./12-directory_permissions): script that creates a directory called `my_dir` with permissions 751 in the working directory.

- **_13. Change group_**
	- [13-change_group](./13-change_group): script that changes group owner to `school` for the file `hello`

- **_14. Owner and group_**
	- [100-change_owner_and_group](./100-change_owner_and_group): script that changes the owner to `vincent` and the group owner to `staff` for all the files and directories in the working directory.

- **_15. Symbolic links_**
	- [101-symbolic_link_permissions](./101-symbolic_link_permissions): script that changes the owner and the group owner of `_hello` to `vincent` and `staff` respectively.
		- The file `_hello` is a symbolic link

- **_16. If only_**
	- [102-if_only](./102-if_only): script that changes the owner of the file `hello` to `betty` only if it is owned by the user `guillaume`.

- **_17. Star Wars_**
	- [103-Star_Wars](./103-Star_Wars): script that plays the Star Wars IV episode in the terminal.
