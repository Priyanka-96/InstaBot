import requests    #importing request package
from termcolor import colored   #import colored package

ACCESS_TOKEN="1572048031.23652d8.52bd5931f05b4c2f92fc6cc9a1e76378"         #my access token
BASE_URL = 'https://api.instagram.com/v1/'          #instagram base url

#this function display own information
def self_info():
    try:
        request_url=(BASE_URL + "users/self/?access_token=%s") % (ACCESS_TOKEN)  #fetching your own data from instagram using "user/self" end point
        print "The GET request url is %s" %(request_url)            #display the GET url
        user_info= requests.get(request_url).json()             #requesting to get the data from the url above mentioned using requests package and using json()
    except:
        print colored("GET request is not working properly","red")     #print this when get request isn't correct
    try:
        if(user_info['meta']['code'])==200:     #checking the status code of request. if 200 then it is accepted otherwise the else part will work
            if len(user_info['data']):              #checking if we have anything in data of user
                print colored("ID: %s","green") % user_info['data']['id']              #printing id of self
                print colored("USERNAME: %s","green") % user_info['data']['username']        #printing username of self
                print colored("NO OF PEOPLE YOU ARE FOLLOWING: %s","green") % user_info['data']['counts']['follows']         #printing no of people i am following
                print colored("NO OF FOLLOWERS: %s","green") % user_info['data']['counts']['followed_by']            #printing number of followers
                print colored("NO OF POSTS: %s","green") % user_info['data']['counts']['media']          #printing no. of post
            else:
                print colored("invalid user!","red")               #work when  there is no data in our id
        else:
            print colored("The request url is not in accepted state","red")        #print when status is in "not accepted" state
    except:
        KeyError        #catching the keyerror of dictionary


#this function getting friend's id of instagram
def get_user_id(instaname):
    try:
        request_url= (BASE_URL + "users/search/?q=%s&access_token=%s") % (instaname,ACCESS_TOKEN)   #searching friend's id from instagram using "user/search" end point
        print "The GET request url is %s" % (request_url)       #display the GET url
        user_info=requests.get(request_url).json()          #requesting to get the data from the url above mentioned using requests package and using json()
    except:
        print colored("GET request isn't working properly","red")      #print this when get request isn't correct

    try:
        if user_info['meta']['code']==200:          #checking the status code of request. if 200 then it is accepted otherwise the else part will work
            if len(user_info['data']):                  #checking if we have anything in data of friend's if
                id= user_info['data'][0]['id']          #storing the id of friend in "id" variable
                return id           #returning the id
            else:
                return None
        else:
            print colored("The request url is not in accepted state","red")    #print when status is in "not accepted" state
    except:
        KeyError                    #catching keyerror of dictionary user-info



#this function display information of friend
def get_user_info(instaname):
    user_id=get_user_id(instaname)      #calling get_user_id() fucntion and getting insta id
    if user_id==None:
        print "There is no data in this account"        #print when id is null
    else:
        try:
            request_url = (BASE_URL + "users/search/?q=%s&access_token=%s") % (instaname,ACCESS_TOKEN)      #searching friend's id from instagram using "user/search" end point
            print "The GET request url is %s" % (request_url)               #display the GET url
            user_info = requests.get(request_url).json()            #requesting to get the data from the url above mentioned using requests package and using json()
        except:
            print colored("GET request is not working properly","red")         #print when incorrect url
        try:
            if (user_info['meta']['code']) == 200:      #checking the status code of request. if 200 then it is accepted otherwise the else part will work
                if len(user_info['data']):                  #checking if we have anything in data of friend's id
                    print colored("ID: %s","green") % user_id            #printing id of friend
                    print colored("USERNAME: %s","green") % user_info['data'][0]['username']     #printing username of friend
                    print colored("FULL NAME OF USER: %s","green") % user_info['data']['fullname']       #printing fullnaame of friend
                    print colored("BIODATA OF USER: %s","green") % user_info['data']['bio']          #printing biography of self
                    print colored("MORE WEBSITE : %s","green") % user_info['data']['website']        #printing more website linked to instagram
                else:
                    print colored("invalid user!","red")           #print when there is no data in friend's id
            else:
                print colored("The request url is not in accepted state","red")        #print when status is in "not accepted" state
        except:
            KeyError        #catching keyerror of dictionary user-info

#function contaning various menu option
def StartBot():
    while True:
        print colored("Welcome to InstaBot app","yellow")                         #   ***  WELCOMING INSTABOT USER ***
        print colored('Here are your menu options:',"red")                 #Printing various menu option
        print "a.Get your own details\n"
        print "b.Get details of a user by username\n"
        print "c.If you want to exit"
        choice = raw_input(colored("Enter you choice: ","yellow"))        #getting menu choice from user
        if choice == "a":
            self_info()         #if choice is "a" then self_info() called
        elif choice == "b":
            insta_username = raw_input(colored("Enter the username of the user: ","blue"))
            get_user_info(insta_username)     #if choice is "b" then get_user_info() called and friend's insta name is passed as parameter
        elif choice=="c":
            exit()              #exit the program
        else:
            print colored("wrong choice","red")   #if choice entered is wrong then print it

StartBot()

