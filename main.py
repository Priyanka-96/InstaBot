

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
import urllib   #importing package which fetch data from internet
import requests    #importing request package
from termcolor import colored   #import colored package

ACCESS_TOKEN="1572048031.23652d8.52bd5931f05b4c2f92fc6cc9a1e76378"         #my access token
BASE_URL = 'https://api.instagram.com/v1/'          #instagram base url


def self_info():

    """  This function retrieve the information of the admin/self and display it """
    print colored(self_info.__doc__,"magenta")

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



def get_self_name():

    """ This function return admin/self/own full name. This information is used in other function """
    print colored(get_self_name.__doc__,"magenta")

    try:
        request_url = (BASE_URL + "users/self/?access_token=%s") % (ACCESS_TOKEN)  # fetching your own data from instagram using "user/self" end point
        #print "The GET request url is %s" % (request_url)  # display the GET url
        user_info = requests.get(request_url).json()  # requesting to get the data from the url above mentioned using requests package and using json()
    except:
        print colored("GET request is not working properly", "red")  # print this when get request isn't correct
    try:
        if (user_info['meta']['code']) == 200:  # checking the status code of request. if 200 then it is accepted otherwise the else part will work
            if len(user_info['data']):  # checking if we have anything in data of user
                return user_info['data']['full_name']

            else:
                print colored("invalid user!", "red")  # work when  there is no data in our id
        else:
            print colored("The request url is not in accepted state","red")  # print when status is in "not accepted" state
    except:
        KeyError  # catching the keyerror of dictionary


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

    # this function getting friend's id of instagram
def get_media_id(user_id):
    try:
        request_url = (BASE_URL + "users/%s/media/recent?&access_token=%s") % (user_id, ACCESS_TOKEN)  # searching friend's id from instagram using "user/search" end point
        print "The GET request url is %s" % (request_url)  # display the GET url
        user_info = requests.get(request_url).json()  # requesting to get the data from the url above mentioned using requests package and using json()
    except:
        print colored("GET request isn't working properly", "red")  # print this when get request isn't correct

    try:
        if user_info['meta']['code'] == 200:  # checking the status code of request. if 200 then it is accepted otherwise the else part will work
            if len(user_info['data']):  # checking if we have anything in data of friend's if
                id = user_info['data'][0]['id']  # storing the id of friend in "id" variable
                return id  # returning the id
            else:
                return None
        else:
            print colored("The request url is not in accepted state","red")  # print when status is in "not accepted" state
    except:
        KeyError  # catching keyerror of dictionary user-info



def get_user_info(instaname):

    """ This function gets input as instagram username of your friend and check if that username exists or not.
      if the username exist then this function retrieve the information of that person and display it """
    print colored(get_user_info.__doc__,"magenta")

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



def get_own_post():

    """ This function check if you have any recent post on your id or not.
      if the post exist then this function downloads the recent post using urllib.urlretrieve() function """
    print colored(get_own_post.__doc__,"magenta")

    try:
        request_url=(BASE_URL + "users/self/media/recent/?access_token=%s") % (ACCESS_TOKEN)  #fetching your own data from instagram using "user/self" end point
        print "The GET request url is %s" %(request_url)            #display the GET url
        own_post= requests.get(request_url).json()             #requesting to get the data from the url above mentioned using requests package and using json()
    except:
        print colored("GET request is not working properly","red")     #print this when get request isn't correct
    try:
        if(own_post['meta']['code'])==200:     #checking the status code of request. if 200 then it is accepted otherwise the else part will work
            if len(own_post['data']):              #checking if we have anything in data of user
                image_name = own_post['data'][0]['id'] + '.jpeg'        #fetching post id from data and storing it in image_name with .jpeg extension
                image_url = own_post['data'][0]['images']['standard_resolution']['url'] #getting url of post and storing in image_url
                urllib.urlretrieve(image_url, image_name)           #retriving the image from image_url and saving in image_name
                print colored('Your image has been downloaded!',"green")  #SUCESS MESSASGE
            else:
                print colored('Post does not exist!',"red")   #print if no post in profile
        else:
            print colored("The request url is not in accepted state","red")        #print when status is in "not accepted" state
    except:
        KeyError        #catching the keyerror of dictionary





def get_user_post(instaname):

    """ This function gets input as instagram username of your friend and check if there is any recent post on his id.
      if the post exist then this function downloads the recent post using urllib.urlretrieve() function """
    print colored(get_user_post.__doc__,"magenta")

    user_id = get_user_id(instaname)  # calling get_user_id() fucntion and getting insta id
    if user_id == None:
        print "There is no data in this account"  # print when id is null
    else:
        try:
            request_url = (BASE_URL + "users/%s/media/recent/?access_token=%s") % (user_id, ACCESS_TOKEN)  # searching friend's id from instagram using "user/search" end point
            print "The GET request url is %s" % (request_url)  # display the GET url
            user_post = requests.get(request_url).json()  # requesting to get the data from the url above mentioned using requests package and using json()
        except:
            print colored("GET request is not working properly", "red")  # print when incorrect url
        try:
            if (user_post['meta']['code']) == 200:  # checking the status code of request. if 200 then it is accepted otherwise the else part will work
                if len(user_post['data']):  # checking if we have anything in data of friend's id
                    image_name = user_post['data'][0]['id'] + '.jpeg'        #fetching post id from data and storing it in image_name with .jpeg extension
                    image_url = user_post['data'][0]['images']['standard_resolution']['url']        #getting url of post and storing in image_url
                    urllib.urlretrieve(image_url, image_name)        #retriving the image from image_url and saving in image_name
                    print colored('Your image has been downloaded!',"green")      #SUCESS MESSASGE
                else:
                    print "There is no recent post!"
            else:
                print colored("The request url is not in accepted state","red")  # print when status is in "not accepted" state
        except:
            KeyError  # catching keyerror of dictionary user-info




def get_like_list(instaname):
    """ This function gets input as instagram username of your friend and get the list of people who has liked the recent post of friend  """
    print colored(get_like_list.__doc__,"magenta")

    user_id=get_user_id(instaname)
    if user_id == None:
        print "There is no data in this account"  # print when id is null
    else:
        media_id=get_media_id(user_id)
        if media_id == None:
            print "There is no media in this account"  # print when id is null
        else:
            try:
                request_url= (BASE_URL + "media/%s/likes?access_token=%s") %(media_id,ACCESS_TOKEN)
                print "The GET request url is %s" % (request_url)  # display the GET url
                user_likes= requests.get(request_url).json()

            except:
                print colored("GET request is not working properly", "red")  # print when incorrect url
            try:
                if(user_likes['meta']['code']) == 200:  # checking the status code of request. if 200 then it is accepted otherwise the else part will work
                    if len(user_likes['data']):  # checking if we have anything in data of friend's id
                        for i in range(len(user_likes['data'])):
                            print colored("The person who recently liked pic is %s","green")  % (user_likes['data'][i]['full_name'])
                            return user_likes['data'][i]['full_name']
                    else:
                        print colored("No likes!","blue")
                else:
                    print colored("The request url is not in accepted state","red")  # print when status is in "not accepted" state
            except:
                KeyError



def like_a_post(instaname):
    """ This function gets input as instagram username of your friend and then it check if you have already liked the post or not.
     if you have already liked then i will print "'OH! You have already liked this pic! :)"" otherwise it will like the post  """
    print colored(like_a_post.__doc__,"magenta")

    username=get_self_name()
    username1=get_like_list(instaname)
    if username==username1:
        print colored("OH! You have already liked this pic! :) ","green")
    else:
        user_id = get_user_id(instaname)
        if user_id == None:
            print "There is no data in this account"  # print when id is null
        else:
            media_id = get_media_id(user_id)
            if media_id == None:
                print "There is no media in this account"  # print when id is null
            else:
                try:
                    request_url = (BASE_URL + 'media/%s/likes') % (media_id)
                    payload = {"access_token": ACCESS_TOKEN}
                    print 'POST request url : %s' % (request_url)       # display the POST url
                    post_like = requests.post(request_url, payload).json()
                except:
                    print colored("POST request is not working properly", "red")  # print when incorrect url

                try:
                    if post_like['meta']['code'] == 200:
                        print colored("SUCESSFULLY LIKED THE POST","green")
                    else:
                        print colored("You couldn't like the POST :( ","red")
                except:
                    KeyError



def unlike_a_post(instaname):
    """ This function gets input as instagram username of your friend and unlike the recent post of your friend """
    print colored(unlike_a_post.__doc__,"magenta")

    user_id = get_user_id(instaname)
    if user_id == None:
        print "There is no data in this account"  # print when id is null
    else:
        media_id = get_media_id(user_id)
        if media_id == None:
            print "There is no media in this account"  # print when id is null
        else:
            try:
                request_url = (BASE_URL + 'media/%s/likes?access_token=%s') % (media_id,ACCESS_TOKEN)
                post_del = requests.delete(request_url).json()
            except:
                print colored("DELETE request is not working properly", "red")  # print when incorrect url

            try:
                if post_del['meta']['code'] == 200:
                    print colored("SUCESSFULLY UNLIKED THE POST", "green")
                else:
                    print colored("You couldn't unlike the POST :( ", "red")
            except:
                KeyError




def get_comment_list(instaname):
    """ This function gets input as instagram username of your friend . After that it checks the recent comments of self on that person's recent post and it displays comments """
    print colored(get_comment_list.__doc__,"magenta")
    user_id = get_user_id(instaname)
    if user_id == None:
        print "There is no data in this account"  # print when id is null
    else:
        media_id = get_media_id(user_id)
        if media_id == None:
            print "There is no media in this account"  # print when id is null
        else:
            try:
                request_url = (BASE_URL + "media/%s/comments?access_token=%s") % (media_id, ACCESS_TOKEN)
                print "The GET request url is %s" % (request_url)  # display the GET url
                user_comment = requests.get(request_url).json()

            except:
                print colored("GET request is not working properly", "red")  # print when incorrect url
            try:
                if (user_comment['meta']['code']) == 200:  # checking the status code of request. if 200 then it is accepted otherwise the else part will work
                    if len(user_comment['data']):  # checking if we have anything in data of friend's id
                        for comnt in range(len(user_comment['data'])):
                            print colored(" Comment : %s \n Posted by : %s", "green") % (user_comment['data'][comnt]['text'],user_comment['data'][comnt]['from']['full_name'])
                    else:
                        print colored("There is no recent comment!", "red")
                else:
                    print colored("The request url is not in accepted state","red")  # print when status is in "not accepted" state
            except:
                KeyError


def comment_on_post(instaname):
    user_id = get_user_id(instaname)
    if user_id == None:
        print "There is no data in this account"  # print when id is null
    else:
        media_id = get_media_id(user_id)
        if media_id == None:
            print "There is no media in this account"  # print when id is null
        else:
            try:
                comment = raw_input("Enter you comment= ")
                payload = {"access_token": ACCESS_TOKEN, "text": comment}
                request_url = (BASE_URL + 'media/%s/comments') % (media_id)
                print "POST request url : %s" % (request_url)
                post_comment = requests.post(request_url, payload).json()
            except:
                print colored("Incorrect URL!","red")
            try:

                if post_comment['meta']['code'] == 200:
                    print colored("Sucessfully posted the comment! :)","green")
                else:
                    print colored("Failed to post!:( TRY AGAIN","red")
            except:
                KeyError



def delete_negative_comment(instaname):
    user_id = get_user_id(instaname)
    if user_id == None:
        print "There is no data in this account"  # print when id is null
    else:
        media_id = get_media_id(user_id)
        if media_id == None:
            print "There is no media in this account"  # print when id is null
        else:
            request_url = (BASE_URL + 'media/%s/comments/?access_token=%s') % (media_id, ACCESS_TOKEN)
            print 'GET request url : %s' % (request_url)
            comment_info = requests.get(request_url).json()

            if comment_info['meta']['code'] == 200:
                if len(comment_info['data']):
                    for cmnt in range(len(comment_info['data'])):
                        comment_list=comment_info['data'][cmnt]['text']
                        comment_id=comment_info['data'][cmnt]['id']
                        blob = TextBlob(comment_list, analyzer=NaiveBayesAnalyzer())
                        if (blob.sentiment.p_neg > blob.sentiment.p_pos):
                            print colored("Your comment is %s :(" ,"red") %comment_list
                            try:
                                request_url = (BASE_URL + 'media/%s/comments/%s/?access_token=%s') %(media_id,comment_id,ACCESS_TOKEN)
                                print "Delete request url :%s" % (request_url)
                                del_info= requests.delete(request_url).json()
                            except:
                                print colored("Request URL not coorect!","red")
                            try:
                                if del_info['meta']['code'] == 200:
                                    print colored("Comment deleted :) ","green")
                                else:
                                    print colored("Unable to delete comment :(","red")
                            except:
                                KeyError

                        else:
                            print colored("%s is a Positive comment :) ","green") % (comment_list)
                else:
                    print colored("No comments present on this post","red")
            else:
                print colored("The request url is not in accepted state","red")  # print when status is in "not accepted" state



def choose_post():
    print colored("Choose one of the following option: ","green")
    print colored("a.Choose post with minimum likes of user","yellow")
    print colored("b.Choose any recent post by tag of user","yellow")
    choice=raw_input("Enter your choice: ")
    if choice=='a':
        instaname=raw_input("Enter the username")
        user_id=get_user_id(instaname)
        if user_id==None:
            print colored("Invalid username :(",'red')
        else:
            request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, ACCESS_TOKEN)
            print "Get url is: %s" % (request_url)
            user_media = requests.get(request_url).json()
            if user_media['meta']['code'] == 200:
                if len(user_media['data']):
                    like_list=[]
                    for i in range(len(user_media['data'])):
                        likes=user_media['data'][i]['likes']['count']
                        like_list.append(likes)
                    min_count=min(like_list)
                    for i in range(len(user_media['data'])):
                        if user_media['data'][i]['likes']['count']==min_count:
                            get_id=user_media['data'][i]['id']
                            image_name = get_id + '.jpeg'
                            image_url = user_media['data'][i]['images']['standard_resolution']['url']
                    urllib.urlretrieve(image_url, image_name)
                    print colored('Your image has been downloaded! :)', 'green')
    elif choice=='b':
        tag_name=raw_input("Enter the tagname without using #")
        request_url = (BASE_URL + 'tags/%s/media/recent?access_token=%s') % (tag_name,ACCESS_TOKEN)
        print "GET request url: %s" % (request_url)
        media_list = requests.get(request_url).json()
        if media_list['meta']['code']==200:
            if len(media_list['data']):
                image_name=media_list['data'][0]['id']+'.jpeg'
                image_url = media_list['data'][0]['images']['standard_resolution']['url']
                urllib.urlretrieve(image_url, image_name)
                print colored('Your image has been downloaded!', 'green')
            else:
                print colored("No data available!",'red')
        else:
            print colored("The request url is not in accepted state","red")
    else:
        print colored("Choose either a or b !",'red')



def display_pie_chart(instaname):
    user_id = get_user_id(instaname)
    if user_id == None:
        print "There is no data in this account"  # print when id is null
    else:
        media_id = get_media_id(user_id)
        if media_id == None:
            print "There is no media in this account"  # print when id is null
        else:
            request_url = (BASE_URL + 'media/%s/comments/?access_token=%s') % (media_id, ACCESS_TOKEN)
            print 'GET request url : %s' % (request_url)
            comment_info = requests.get(request_url).json()

            if comment_info['meta']['code'] == 200:
                if len(comment_info['data']):
                    list=[]
                    for cmnt in range(len(comment_info['data'])):
                        comment_list = comment_info['data'][cmnt]['text']
                        list.append(comment_list)

                    comment = ''.join(list)
                    blob = TextBlob(comment, analyzer=NaiveBayesAnalyzer())
                    values = [blob.sentiment.p_pos, blob.sentiment.p_neg]
                    labels = ['Positive\nComments', 'Negative\nComments']

                    fig = plt.figure()
                    fig.patch.set_facecolor('pink')
                    fig.patch.set_alpha(0.7)

                    col = ['blue', 'yellow']
                    plt.pie(values, labels=labels, startangle=90, autopct='%1.1f%%', colors=col, shadow=True,explode=(0, 0.1))
                    plt.title("Negative VS Positive Comments \n (Percentage Comparison)")
                    plt.legend()
                    plt.show()
                    StartBot()

                else:
                    print colored("No comments present on this post", "red")
            else:
                print colored("The request url is not in accepted state","red")  # print when status is in "not accepted" state


#function contaning various menu option
def StartBot():
    while True:
        print colored("Welcome to InstaBot app","yellow")                         #   ***  WELCOMING INSTABOT USER ***
        print colored('Here are your menu options:',"red")                 #Printing various menu option
        print "a.Get your own details\n"
        print "b.Get details of a user by username\n"
        print "c.Get your own recent post\n"
        print "d.Get user's recent post by username\n"
        print "e.Get list of people who has liked your posts\n"
        print "f.Like the post of your friend\n"
        print "g.Unlike the post of your friend\n"
        print "h.Get the list of recent comment on your post\n"
        print "i.Comment on post\n"
        print "j.Delete negative comments \n"
        print "k.Display pie chart comparing negative and positive comments on a post \n"
        print "l.To choose post by minimum likes or tag\n"
        print "m.Exit the application"
        choice = raw_input(colored("Enter you choice: ","yellow"))        #getting menu choice from user
        if len(choice)>0 and len(choice)<2 and choice.isalpha()==True and choice.isspace()==False :
            if choice == "a":
                self_info()         #if choice is "a" then self_info() called
            elif choice == "b":
                insta_username = raw_input(colored("Enter the username of the user: ","blue"))
                get_user_info(insta_username)     #if choice is "b" then get_user_info() called and friend's insta name is passed as parameter
            elif choice == "c":
                get_own_post()      #if choice is "c" then get_own_post() called
            elif choice == "d":
                insta_username = raw_input(colored("Enter the username of the user: ", "blue"))
                get_user_post(insta_username)  # if choice is "b" then get_user_post() called and friend's insta name is passed as parameter
            elif choice=="e":
                insta_username = raw_input(colored("Enter the username of the user: ", "blue"))
                get_like_list(insta_username)
            elif choice=="f":
                insta_username = raw_input(colored("Enter the username whose post you want to like: ", "blue"))
                like_a_post(insta_username)
            elif choice == "g":
                insta_username = raw_input(colored("Enter the username whose post you want to unlike: ", "blue"))
                unlike_a_post(insta_username)
            elif choice == "h":
                insta_username = raw_input(colored("Enter the username whose comment you want to see on recent post: ", "blue"))
                get_comment_list(insta_username)
            elif choice == "i":
                insta_username = raw_input(colored("Enter the username whose post you want to comment on: ", "blue"))
                comment_on_post(insta_username)
            elif choice=="j":
                insta_username = raw_input(colored("Enter the username on whose id u want to delete the comments:" , "blue"))
                delete_negative_comment(insta_username)
            elif choice=="k":
                insta_username = raw_input(colored("Enter the username whose comments-comparison pie chart you want to see : " , "blue"))
                display_pie_chart(insta_username)
            elif choice=="l":
                choose_post()
            elif choice=="m":
                exit()              #exit the program
            else:
                print colored("You have entered a wrong choice","red")
        else:
            print colored("You have entered a wrong choice !Try Again","red")


StartBot()

