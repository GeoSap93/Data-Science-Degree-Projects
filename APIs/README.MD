### 1. Empty __inti__.py file
It's an empty file.

### 2. File config.py
This file has my credentials (host, user, password) so that the API connects
to the SQL workbench.

### 3. File app.py
Installing and importing flask so that we start creating the APIs. Created 3 endpoints, the homepage
to get the joined dates for each Bingham member, to add a different room and
delete member's booking.

### 4. File main.py
Importing requests and json, I created functions and the run() function at the end to stimulate the 
interaction with the API for the user, displaying the slots available and being able to interact 
and book a place in the MembersClub.

### 5. File db_utils.py

Installing and importing the "mysql.connector" and the important information we keep in the config.py file so that we successfully connect to the SQL benchwork.
Using different queries to retrieve data from the database we created.

!!! Please run the "app.py" document and then while the file is running, go to the "main.py" and run the file so that you interact with the interface and book your slot with Bingham!