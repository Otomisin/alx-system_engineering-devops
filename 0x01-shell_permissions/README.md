## Shell, permissions
			
0	 A Script that changes your user ID to betty	 = >	su betty
			
1	 id -un Print the effective user ID of current user. Other alternative is whoami	 = >	id -un
			
2	 id -Gn Prints all the groups the current user is part of.	 = >	id -Gn
			
3	Changes the owner of the file hello to the user betty	 = >	chown betty
			
4	Create an empty file called hello	 = >	touch hello
			
5	Add execute permission to the owner of the file hello	 = >	chmod u
			
6	Add execute permission to user and group owner, and read permission to others for file hello	 = >	 chmod ug+x,o+r hello 
			
7	Add execution permission to all for file hello.	 = >	 chmod ugo+x Hello
			
8	Set permissions for file hello so owner and group don't have any permissions and other users have all permissions.	 = >	chmod 007 hello
			
9	Set permissions so owner has all permissions, group has read and execute permissions and others have write and execute permissions.	 = >	chmod 753 hello
			
10	Copies the mode of file olleh to file hello.	 = >	chmod --reference=olleh Hello
			
11	Add execute permission to all subdirectories of the current directory for the everyone. Regular files should not be changed.	 = >	chmod -R +X  or  chmod ugo+x */ or chmod a+x */
			
12	Create a directory called dir_holberton with permissions 751 in the working directory. User has all read, write, and execute permissions. Group has read and execute permissions. Others have just execute permission.	 = >	mkdir -m 751 my_dir
			
13	Write a script that changes the group owner to school for the file hello	 = >	chgrp school
			
14	Write a script that changes the owner to vincent and the group owner to staff for all the files and directories in the working directory.	 = >	chown vincent:staff *
			
15	Changes the owner and group owner of file _hello to betty and holberton respectively.	 = >	sudo chown -h vincent:staff _hello
			
16	Change owner of the file hello to betty only if it is currently owned by guillaume	 = >	chown --from=guillaume betty hello
			
17	Play the Star Wars IV episode in the terminal. This is a premade script provided online.	 = >	telnet towel
