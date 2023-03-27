# Back-End_CA3
Repository for the third project of my Back-End semester.


The goal of this presentation was to create tests for the application created in the two previous presentations. So I added 3 test files. One for tests on the models, and more precisely the one of my clothing model. In this one, I simply test all the functionalities that can be done on an object, like creating it, destroying it, or editing it. I didn't add any other tests because I didn't know what else to create tests on. The second file is a test file for views and the third one for urls. These two files are a bit similar, because in the first one we're going to see if the views of my main pages work well, and in the second one if the urls are not wrong. I have added negative tests in each of these files, even if these negative tests are not very elaborate.


For the security part now:


First, for the authentication, I had already since the last defense, a redirection system at the level of my index page with a check if the user has authenticated himself.


Then, I added a security at the level of the passwords, by using an algorithm to hash them. This modification can be found in the settings file.
For the mis-configurations, I don't have much to add because I was already using "os.join" at the very beginning of my project.


Then, as I made my repo public, I had to change my secret key, which I replaced by a secret key that is automatically generated at each launch of the application.
I also had to set the debug mode to False, and so add in the localhost field a correct ip.
Finally, I changed the path to access the admin page, because it was enough to put /admin to access it, which made my application particularly vulnerable.
