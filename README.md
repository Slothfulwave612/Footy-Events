# Footy-Events

## Overview:

* This project *Footy Events* focusses on scrapping user's team fixtures and adding the fixture as an event in user's Google calendar.

* The website we are using for scrapping the content is: https://www.skysports.com/

* If you want fixture for *FC Barcelona* the site from where the data will be scrapped is: https://www.skysports.com/barcelona-fixtures

* The following is the basic prototype of our project:
  ![Capture](https://user-images.githubusercontent.com/33928040/76706273-3bdf9b80-670c-11ea-8a1a-092a082fd8f6.PNG)

## Modules Used(Python):

1. **Python**: 3.7.5 (default, Oct 31 2019, 15:18:51) [MSC v.1916 64 bit (AMD64)]
2. **requests**: 2.22.0
3. **bs4**: 4.8.1
4. **apiclient**: 1.7.11
5. **google_auth_oauthlib**: 0.4.1
6. **pickle**: 4.0
7. **re**: 2.2.1

## Running Process:

* For running the program run the *main_menu.py* file.

* On running it you will be shown some options and have to make a choice.
  ![Capture](https://user-images.githubusercontent.com/33928040/76706254-194d8280-670c-11ea-86b1-5e198b568277.PNG)

* There are four choices:
  1. **Enlist Your Team**: In this option you can add your team names or can delete them.
  2. **Enlist Your Competitions**: In this option you can add you competitions.
  3. **Run The Process**: This option will run the whole process of scrapping and adding the content to your google calendar.
  4. **Exit**: To exit the program.
  
* On picking the first option(i.e. entering 1 in *Enter You Choice:- *), the user will be shown the following options:
  ![Capture](https://user-images.githubusercontent.com/33928040/76706354-d809a280-670c-11ea-8bc7-2f532b16451f.PNG)
  
  1. **Add a Team**: 
     * On choosing this option, you will be asked to enter the team name.
     * Here you can do two things, either you can enter a single team name or multiple team names.
     * On entering team names a file named *footy_teams.txt* will be created which will contain all teams you have listed.
     
     *For adding single team*
     ![Capture](https://user-images.githubusercontent.com/33928040/76706479-c07ee980-670d-11ea-9ccf-3a0e1271405c.PNG)
      
      *For adding multiple teams*
     ![Capture](https://user-images.githubusercontent.com/33928040/76706665-359eee80-670f-11ea-92af-faf12030b8f1.PNG)
     
     *footy_teams.txt*
     ![Capture](https://user-images.githubusercontent.com/33928040/76706672-4e0f0900-670f-11ea-8db8-ee2d253b6218.PNG)
     
  2. **Preview Added Teams**:
      * This option will display all the teams user has added to footy_teams.txt.
      
      *Preview Added Teams*
      ![Capture](https://user-images.githubusercontent.com/33928040/76706677-64b56000-670f-11ea-9e3f-b6076108c77b.PNG)
      
  3. **Delete Added Teams**:
      * This option will help users to delete the team names they listed.
      * Either the user can delete one team at a time or multiple teams at a time.
      * If the user want to delete all the team names, then can specify del_all when asked for the team name this will delete footy_teams.txt as well.
      
      *For deleting single team*
      ![Capture](https://user-images.githubusercontent.com/33928040/76706696-93333b00-670f-11ea-97e3-7607bbd389d8.PNG)

      *For deleting multiple teams*
      ![Capture](https://user-images.githubusercontent.com/33928040/76706724-cb3a7e00-670f-11ea-8e11-afd8a256fbc2.PNG)
      
      *For deleting all the teams*
      ![Capture](https://user-images.githubusercontent.com/33928040/76706855-9975e700-6710-11ea-92f7-4bc127a1d32c.PNG)
  
  4. **Back**:
      * For going back to the main menu.

* One entering the second option the user will be shown the following options:
  ![Capture](https://user-images.githubusercontent.com/33928040/76706904-05584f80-6711-11ea-951a-4e30c844b910.PNG)

  1. **Add a Competiton**:
      * Here the user can add the competition's name.
      * The adding can be done in three ways.
      * If the user want to add only few teams featuring in that particular competiton.(1)      
      * If the user want to add only few teams featuring in multiple competitions.(2)
      * If the user want to add all the teams featuring in that particular competiton.(3)
      
      *For (1)*
      ![Capture](https://user-images.githubusercontent.com/33928040/76707143-dc38be80-6712-11ea-98ad-7bd7af0d129e.PNG)

      *For (2)*
      ![Capture](https://user-images.githubusercontent.com/33928040/76707284-ced00400-6713-11ea-8bba-a508c291804f.PNG)

      *For (3)*
      ![Capture](https://user-images.githubusercontent.com/33928040/76707294-f2934a00-6713-11ea-9332-d920412bddbb.PNG)
  
  2. **Preview Added Competition**:
      * This option will display all the competitions the user has listed.
      ![Capture](https://user-images.githubusercontent.com/33928040/76707333-469e2e80-6714-11ea-8da5-33e2ce2b473f.PNG)
  
  3. **Delete Added Competition**:
      * This option will delete the added competiton.
      * The user can perform three actions here.
      * If the user want to delete some teams from a particular competitions.(1)
      * If the user want to delete the competitions.(2)
      * If the user want to delete all competitions.(3)
      
      *For (1)*
      ![Capture](https://user-images.githubusercontent.com/33928040/76707887-e1007100-6718-11ea-82f3-e6a355432300.PNG)

      *For (2)*      
      ![Capture](https://user-images.githubusercontent.com/33928040/76707958-5b30f580-6719-11ea-85b9-c9c56f85e71f.PNG)
      
      *For (3)*
      ![Capture](https://user-images.githubusercontent.com/33928040/76707981-7c91e180-6719-11ea-9031-2f97317cb346.PNG)
  
  4. **Back**:
      * To go back to main menu.
  
* The third option is for adding/updating event in the user's google calendar.

* The user will be asked to enter the username so that the user's calendar info can be saved by that particular user name.

* Then the user will be given a link from where the user will allow the program the access for his/her google calendar, so that the program can add or update event.

* The process is shown in the following images:
  
  ![Capture](https://user-images.githubusercontent.com/33928040/76708167-caf3b000-671a-11ea-9cc6-df1a18845c41.PNG)

  ![Capture](https://user-images.githubusercontent.com/33928040/76708318-ead7a380-671b-11ea-9418-c46852f78e83.PNG)

  ![Capture](https://user-images.githubusercontent.com/33928040/76708353-1b1f4200-671c-11ea-9eaa-f820dade8ecb.PNG)

  ![Capture](https://user-images.githubusercontent.com/33928040/76708366-3722e380-671c-11ea-8700-6c1d057ed22c.PNG)

  ![Capture](https://user-images.githubusercontent.com/33928040/76708389-62a5ce00-671c-11ea-823b-426de8d37450.PNG)

  ![Capture](https://user-images.githubusercontent.com/33928040/76708398-75200780-671c-11ea-85ff-b994890ef357.PNG)
  
  ![Capture](https://user-images.githubusercontent.com/33928040/76708408-92ed6c80-671c-11ea-8a0f-bae031e1d251.PNG)

* **NOTE**: Cannot display further process because due to corona virus outbreak, all the football matches have been postponed and because we don't have any further updates about the dates of the fixtures you just cannot add the event to your calendar. As soon as the dates are listed the furter process images will be inserted. Thank You.
  
