# 0x03. Shell, init files, variables and expansions

## Learning Objectives in this project:

### General

- What happens when you type `$ ls -l *.txt`.

### Shell Initialization Files

- What are the `/etc/profile` file and the `/etc/profile.d` directory.
- What is the `~/.bashrc` file.

### Variables

- What is the difference between a local and global variable.
- What is a reserved variable.
- How to create, update and delete shell variables.
- What are the roles of the following reserved variables: HOME, PATH, PS1.
- What are special parameters.
- What is the special parameter `$?`?

### Expansions

- What is expansion and how to use it.
- What is the difference between single and double quotes and how to use them properly.
- How to do command substitution with `$()` and backticks.

### Shell Arithmetic

- How to perform arithmetic operations with the shell.

### The `alias` Command
- How to create an alias
- How to list aliases
- How to temporarily disable an alias.

## Tasks

- **_0. <o>_**
	- [0-alias](./0-alias): Bash script that creates an alias.
				- Name: `ls`
				- Value: `rm *`

- **_1. Hello you_**
	- [1-hello_you](./1-hello_you): Bash script that prints `hello user`, where is the current Linux user.

- **_2. The path to success is to take massive, determined action_**
	- [2-path](./2-path): Bash script that adds `/action` to the `PATH`. `/action` should be the last directory the shell looks into when looking for a program.

- **_3. If the path be beautiful, let us not ask where it leads_**
	- [3-paths](./3-paths): Bash script that counts the number of directories in the `PATH`.

- **_4. Global variables_**
	- [4-global_variables](./4-global_variables): Bash script that lists environment variables.

- **_5. Local variables_**
	- [5-local_variables](./5-local_variables): Bash script that lists all local variables and environment variables, and functions.

- **_6. Local variable_**
	- [6-create_local_variable](./6-create_local_variable): Bash script that creates a new local variable.
								- Name: `BEST`	
								- Value: `School`

- **_7. Global variable_**
	- [7-create_global_variable](./7-create_global_variable): Bash script that creates a new global variable.
								- Name: `BEST`
								- Value: `School`

- **_8. Every addition to true knowledge is an addition to human power_**
	- [8-true_knowledge](./8-true_knowledge): Bash script that prints the result of the addition of 128 with the value stored in the environmental variable `TRUEKNOWLEDGE`, followed by a new line.

- **_9. Divide and rule_**
	- [9-divide_and_rule](./9-divide_and_rule): Bash script that prints the result of `POWER` divided by `DIVIDE`, followed by a new line.
						    - `POWER` and `DIVIDE` are environment variables

- **_10. Love is anterior to life, posterior to death, initial of creation, and the exponent of breath_**
	- [10-love_exponent_breath](./10-love_exponent_breath): Bash script that displays the result of `BREATH` to the power `LOVE`
								- `BREATH` and `LOVE` are environment variables
								- The script should display the result, followed by a new line

- **_11. There are 10 types of people in the world -- Those who understand binary, and those who don't_**
	- [11-binary_to_decimal](./11-binary_to_decimal): Bash script that converts a number from base 2 to base 10.
							  - The base 2 number will be stored in the environment variable `BINARY`.
							  - The script should display the number in base 10, followed by a new line.

- **_12. Combination_**
	- [12-combinations](./12-combinations): Bash script that prints all possible combinations of two letters, except `oo`.
						- Letters are lower case, from `a` to `z`
						- One combination per line
						- The output should be alpha ordered, starting with `aa`
						- Do not print `oo`
						- Your script file should contain maximum 64 characters

- **_13. Floats_**
	- [13-print_float](./13-print_float): Bash script that prints a number with two decimal places, followed by a new line.
					      - Number will be stored in environmental variable `NUM`

- **_14. Decimal to Hexadecimal_**
	- [100-decimal_to_hexadecimal](./100-decimal_to_hexadecimal): Bash script that converts a number from base 10 to base 16.
								      - The number in base 10 is stored in the environmental variable `DECIMAL`
								      - The script should display the number in base 16, followed by a new line

- **_15. Everyone is a proponent of strong encryption_**
	- [101-rot13](./101-rot13): Bash script that encodes and decodes text using the rot13 encryption. Assume ASCII.

- **_16. The eggs of the brood need to be an odd number_**
	- [102-odd](./102-odd): Bash script that prints every other line from the input, starting with the first line.

- **_17. I'm an instant star. Just add water and stir._**
	- [103-water_and_stir](./103-water_and_stir): Bash script that adds the two numbers stored in the environment variables `WATER` and `STIR` and prints the result.
						      - `WATER` is base `water`
						      - `STIR` is in base `stir`
						      - The result should be in base `bestchol`
