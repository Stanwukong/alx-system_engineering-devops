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
