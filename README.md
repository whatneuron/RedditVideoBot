# RedditVideoBot
This is a small project to automate the reddit videos that just steal content.
It's run by just me feel free to add to it if you want to just create a pull request i think that's how it works.
Im sure there are much better implementations. Its also not documented in the slightest. 

The design is a bit flawed in that it doesnt look like reddit but that could easily be added Im going to look into it over the coming weeks. I just wanted something fully functional first.

##dependancies
Right now it depends on all of these libraries:

mutagen

moviepy

praw - view library setup to configure correctly

google cloud api - again view library setup to configure

selenium - to use with firefox which is the default geckodriver must be installed

##environment configuration
It is built for arch linux but it should run on all other distros and operating systems. If you do come across an os specific error please open an issue.

By default the project runs using environment variables to get password secrets and the like. 
It is not 100% necessary but if you are going to do any committing or sharing of your work i highly recommend it. on linux you can create them with EXPORT password=thisismypassword. 
I'm not entirely sure about how it works on windows and macos but if you are using an ide most of them allow you to set environment variables within them.

Here is a list of all the required enviroment variables

GOOGLE_APPLICATION_CREDENTIALS get this at https://cloud.google.com/docs/authentication/getting-started

user_agent, client_id, client_secret all of these are for the reddit api. Open a reddit api at https://www.reddit.com/prefs/apps/. 
Set the redirect uri to http://localhost:8080. Then set the user_agent to your username and get the rest from the app you have created.  

google_email, google_password this self explanatory you can look at the code i do nothing with this data other than log you in.

you need to either have 32 gigs of ram or have a swap + total ram of over 20 gig. This is due to a glitch with subrocess.Popen that moviepy uses to encode with ffmpeg. It never actually uses the swap but it doesnt crash due to it thinking it has more ram.
Google how to create a swap its not that hard and wont impact performance.

##Example channel
https://www.youtube.com/channel/UCkuWijM9I1V9eRqw12sJfzw

This cannel is an example of a basic use all the videos were generated over around one hour. As you can see its not perfect but its a proof of concept Im sure someone else can make it look much more like the other people's videos.