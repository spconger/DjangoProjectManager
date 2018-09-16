# DjangoProjectManager
This is a project in which I am learning to use Django. The program tracks project ideas and the time spent on them. The web site will ultimately allow multiple users to each manage their own projects and keep a log of their time and hours spent.
The project uses a postgresql database.
The app folder is called task.
The first commit is after the app has been initialized, the model has been created and migrated, I have created and index view which lists the projects and a detail view that displays all the info for a particular project. I have also created templates for each view and a base template with the surrounding html structure. The urls are still at the project level. (I have problems making the include work--something I will work on.)
#Second commit
For the second commit I added forms for adding a new project and tracking time. Both views display, but only the project one saves. Not sure why. Also moved Urls from project level to application level.
