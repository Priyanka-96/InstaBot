

import matplotlib.pyplot as plt         #importing matplot lib for pie chart
from textblob import TextBlob       #import Textblob for semantic analyse of a sentence
from textblob.sentiments import NaiveBayesAnalyzer          #import Textblob for semantic analyse of a sentence
import urllib                             #importing package which download the data from given url
import requests                               #importing request package
from termcolor import colored                    #import colored package



ACCESS_TOKEN="1572048031.23652d8.52bd5931f05b4c2f92fc6cc9a1e76378"         #my access token
BASE_URL = 'https://api.instagram.com/v1/'          #instagram base url


def self_info():

    """
    This function retrieve the information of the admin/self and display it
    :return: ---
    """

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
        print KeyError      #printing the keyerror



def get_self_name():

    """
     :return: Self full name
    """

    try:
        request_url = (BASE_URL + "users/self/?access_token=%s") % (ACCESS_TOKEN)    # fetching your own data from instagram using "user/self" end point
        user_info = requests.get(request_url).json()    # requesting to get the data from the url above mentioned using requests package and using json()
    except:
        print colored("GET request is not working properly", "red")      # print this when get request isn't correct
    try:
        if (user_info['meta']['code']) == 200:       # checking the status code of request. if 200 then it is accepted otherwise the else part will work
            if len(user_info['data']):       # checking if we have anything in data of user
                return user_info['data']['full_name']       #returning the self fullname to other functions

            else:
                print colored("invalid user!", "red")       # work when  there is no data in self id
        else:
            print colored("The request url is not in accepted state","red")         # print when status is in "not accepted" state
    except:
        KeyError  # catching the keyerror of dictionary
        print KeyError         #printing keyerror



def get_user_id(instaname):
    """

    :param instaname: this is the username of instagram which client use to login into instagram
    :return: id : return the id of the respective instaname
    """
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
                return None     #if no data in corresponding instaname then return none
        else:
            print colored("The request url is not in accepted state","red")    #print when status is in "not accepted" state
    except:
        KeyError                    #catching keyerror of dictionary user-info
        print  KeyError     #printing the key error



def get_media_id(user_id):
    """

    :param user_id: user_id is the id in numeric of the user. It is unique of every user of instagram
    :return:media_id : this function returns the recent media id of corresponding user_id.
    """

    try:
        request_url = (BASE_URL + "users/%s/media/recent?&access_token=%s") % (user_id, ACCESS_TOKEN)  #fetching the recent media of user using user_id and acesstoken
        print "The GET request url is %s" % (request_url)       # display the GET url
        user_info = requests.get(request_url).json()        # requesting to get the data from the url above mentioned using requests package and using json()
    except:
        print colored("GET request isn't working properly", "red")  # print this when get request isn't correct

    try:
        if user_info['meta']['code'] == 200:       # checking the status code of request. if 200 then it is accepted otherwise the else part will work
            if len(user_info['data']):       # checking if we have anything in data of friend's if
                id = user_info['data'][0]['id']        # storing the id of friend in "id" variable
                return id           # returning the id
            else:
                return None         #if no data in corresponding instaname then return none
        else:
            print colored("The request url is not in accepted state","red")  # print when status is in "not accepted" state
    except:
        KeyError  # catching keyerror of dictionary user-info
        print KeyError      #printing key error



def get_user_info(instaname):

    """
    This function gets input as instagram username of your friend and check if that username exists or not.
      if the username exist then this function retrieve the information of that person and display it

    :param instaname: this is the username of instagram which client use to login into instagram
    :return: --
    """
    user_id=get_user_id(instaname)      #calling get_user_id() fucntion and getting insta id
    if user_id==None:
        print colored("ID dont exist","red")        #print when id is null
    else:
        try:
            request_url = (BASE_URL + "users/%s/?access_token=%s") % (user_id,ACCESS_TOKEN)      #searching friend's id from instagram using "user/search" end point
            print "The GET request url is %s" % (request_url)               #display the GET url
            user_info = requests.get(request_url).json()            #requesting to get the data from the url above mentioned using requests package and using json()
        except:
            print colored("GET request is not working properly","red")         #print when incorrect url
        try:
            if (user_info['meta']['code']) == 200:      #checking the status code of request. if 200 then it is accepted otherwise the else part will work
                if len(user_info['data']):                  #checking if we have anything in data of friend's id
                    print colored("USERNAME: %s","green") % user_info['data']['username']     #printing username of friend
                    print colored("No. of followers: %s","green") % user_info['data']['counts']['followed_by']       #printing followers  of friend
                    print colored("No of people you  are following : %s","green") % user_info['data']['counts']['follows']      #printing no of people follows by friend
                    print colored("No. of posts are  : %s","green") % user_info['data']['counts']['media']        #printing no of psots of friend
                else:
                    print colored("invalid user!","red")           #print when there is no data in friend's id
            else:
                print colored("The request url is not in accepted state","red")        #print when status is in "not accepted" state
        except:
            KeyError        #catching keyerror of dictionary user-info
            print KeyError    #printing keyerror



def get_own_post():

    """
    This function check if you have any recent post on your id or not.
    if the post exist then this function downloads the recent post using urllib.urlretrieve() function

    :return: --
    """
    try:
        request_url=(BASE_URL + "users/self/media/recent/?access_token=%s") % (ACCESS_TOKEN)  #fetching your own recent media from instagram using "user/self" end point
        print "The GET request url is %s" %(request_url)            #display the GET url
        own_post= requests.get(request_url).json()             #requesting to get the data from the url above mentioned using requests package and using json()
    except:
        print colored("GET request is not working properly","red")     #print this when get request isn't correct
    try:
        if(own_post['meta']['code'])==200:     #checking the status code of request. if 200 then it is accepted otherwise the else part will work
            if len(own_post['data']):                 #checking if we have anything in data of user
                image_name = own_post['data'][0]['id'] + '.jpeg'          #fetching post id from data and storing it in image_name with .jpeg extension
                image_url = own_post['data'][0]['images']['standard_resolution']['url']     #getting url of post and storing in image_url
                urllib.urlretrieve(image_url, image_name)            #retriving the image from image_url and saving in image_name with jpeg extension
                print colored('Your image has been downloaded!',"green")     #SUCESS MESSASGE
            else:
                print colored('Post does not exist!',"red")   #print if no post in profile
        else:
            print colored("The request url is not in accepted state","red")        #print when status is in "not accepted" state
    except:
        KeyError        #catching the keyerror of dictionary
        print KeyError



def get_user_post(instaname):
    """
     This function gets input as instagram username of your friend and check if there is any recent post on his id.
      if the post exist then this function downloads the recent post using urllib.urlretrieve() function

    :param instaname: this is the username of instagram which client use to login into instagram
    :return: --
    """

    user_id = get_user_id(instaname)  # calling get_user_id() fucntion and getting insta id
    if user_id == None:
        print "There is no data in this account"  # print when id is null
    else:
        try:
            request_url = (BASE_URL + "users/%s/media/recent/?access_token=%s") % (user_id, ACCESS_TOKEN)  # getting users media list from "user/user_id/media/recent" end point
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
                    print colored("There is no recent post!","red")        #print if no recent post
            else:
                print colored("The request url is not in accepted state","red")  # print when status is in "not accepted" state
        except:
            KeyError  # catching keyerror of dictionary user-info
            print KeyError    #printing keyerror



def get_like_list(instaname):
    """
     get the list of people who has liked the recent post of user
    :param instaname: this is the username of instagram which client use to login into instagram
    :return: no. of likes on friend's post
    """

    user_id=get_user_id(instaname)      # calling get_user_id() fucntion and getting insta id
    if user_id == None:
        print "There is no data in this account"  # print when id is null
    else:
        media_id=get_media_id(user_id)      # calling get_media_id() fucntion and getting media id of corresponding user-id
        if media_id == None:
            print "There is no media in this account"  # print when id is null
        else:
            try:
                request_url= (BASE_URL + "media/%s/likes?access_token=%s") %(media_id,ACCESS_TOKEN)     #fetching number of likes on recent post of correspoding user_id
                print "The GET request url is %s" % (request_url)  # display the GET url
                user_likes= requests.get(request_url).json()        # requesting to get the data from the url above mentioned using requests package and using json()

            except:
                print colored("GET request is not working properly", "red")  # print when incorrect url
            try:
                if(user_likes['meta']['code']) == 200:  # checking the status code of request. if 200 then it is accepted otherwise the else part will work
                    if len(user_likes['data']):  # checking if we have anything in data of friend's id
                        list=[]
                        for i in range(len(user_likes['data'])):
                            print colored("Your post is liked by %s","green")  % (user_likes['data'][i]['full_name'])       #print the name who like your recent pic
                            list.append(user_likes['data'][i]['full_name'])  #appending list
                        return list     #returning to like_a_post() function
                    else:
                        print colored("No likes!","red")    #print when no likes
                else:
                    print colored("The request url is not in accepted state","red")  # print when status is in "not accepted" state
            except:
                KeyError         #catching keyerror
                print KeyError        #printing key error



def like_a_post(instaname):
    """
     This function gets input as instagram username of your friend and then it check if you have already liked the post or not.
     if you have already liked then i will print "'OH! You have already liked this pic! :)"" otherwise it will like the post

    :param instaname: this is the username of instagram which client use to login into instagram
    :return: --
    """

    username=get_self_name()        #calling get_self_name()
    list=get_like_list(instaname)       #calling get_like_list()
    if username in list:  #comparing if you have already liked the post or not
        print colored("OH! You have already liked this pic! :) ","green")           #print if already liked the pic
    else:
        user_id = get_user_id(instaname)        #calling get_user_id
        if user_id == None:
            print colored("There is no data in this account","red")    # print when user id is null
        else:
            media_id = get_media_id(user_id)        #calling get_media_id()
            if media_id == None:                #check if media id none
                print colored("There is no media in this account","red")  # print when media id is null
            else:
                try:
                    request_url = (BASE_URL + 'media/%s/likes') % (media_id)        #url to like the post using media id
                    payload = {"access_token": ACCESS_TOKEN}        # payload as a dictionary
                    print 'POST request url : %s' % (request_url)       # display the POST url
                    post_like = requests.post(request_url, payload).json()      #posting  the data to the url above mentioned using requests package and using json()
                except:
                    print colored("POST request is not working properly", "red")  # print when incorrect url

                try:
                    if post_like['meta']['code'] == 200:        # checking the status code of request. if 200 then it is accepted otherwise the else part will work
                        print colored("SUCESSFULLY LIKED THE POST","green")     #print if post is sucessfully liked
                    else:
                        print colored("You couldn't like the POST :( ","red")           #printing if post is not sucessfully liked
                except:
                    KeyError        #catch keyerror
                    print KeyError      #printing keyerror



def unlike_a_post(instaname):
    """
     This function gets input as instagram username of your friend and unlike the recent post of your friend

    :param instaname:  this is the username of instagram which client use to login into instagram
    :return: --
    """

    user_id = get_user_id(instaname)         #calling get_user_id()
    if user_id == None:
        print "There is no data in this account"  # print when id is null
    else:
        media_id = get_media_id(user_id)        #calling get_media_id()
        if media_id == None:
            print "There is no media in this account"  # print when media id is null
        else:
            try:
                request_url = (BASE_URL + 'media/%s/likes?access_token=%s') % (media_id,ACCESS_TOKEN)      #url of liking the recent post corresponding to media id
                post_del = requests.delete(request_url).json()      #deleteing the data to the url above mentioned using requests package and using json()
            except:
                print colored("DELETE request is not working properly", "red")  # print when incorrect url

            try:
                if post_del['meta']['code'] == 200:       # checking the status code of request. if 200 then it is accepted otherwise the else part will work
                    print colored("SUCESSFULLY UNLIKED THE POST", "green")      #print if post is sucessfully unliked
                else:
                    print colored("You couldn't unlike the POST :( ", "red")          #printing if post is not sucessfully unliked
            except:
                KeyError        #catching keyerror
                print KeyError     #printing keyerror



def get_comment_list(instaname):
    """
     it checks the recent comments of self on user's recent post and it displays comments
    :param instaname: this is the username of instagram which client use to login into instagram
    :return: --
    """
    user_id = get_user_id(instaname)        #calling get_user_id()
    if user_id == None:
        print "There is no data in this account"  # print when id is null
    else:
        media_id = get_media_id(user_id)        #get_media_id called to get recent media of user
        if media_id == None:
            print "There is no media in this account"  # print when media id is null
        else:
            try:
                request_url = (BASE_URL + "media/%s/comments?access_token=%s") % (media_id, ACCESS_TOKEN)       #url of fetching the comments on the recent post corresponding to media id
                print "The GET request url is %s" % (request_url)  # display the GET url
                user_comment = requests.get(request_url).json()     #getting the data of the url above mentioned using requests package and using json()

            except:
                print colored("GET request is not working properly", "red")  # print when incorrect url
            try:
                if (user_comment['meta']['code']) == 200:  # checking the status code of request. if 200 then it is accepted otherwise the else part will work
                    if len(user_comment['data']):  # checking if we have anything in data of friend's id
                        for comnt in range(len(user_comment['data'])):      #for loop works till the data available in user_comment
                            #fetching the comments and fullname of person who has commented on media
                            print colored(" Comment : %s \n Posted by : %s", "green") % (user_comment['data'][comnt]['text'],user_comment['data'][comnt]['from']['full_name'])
                    else:
                        print colored("There is no recent comment!", "red")     #print when no recent comments are there
                else:
                    print colored("The request url is not in accepted state","red")  # print when status is in "not accepted" state
            except:
                KeyError        #catching Key error
                print KeyError  #printing keyerror



def comment_on_post(instaname):
    """
    this function make comment on recent post of user
    :param instaname:this is the username of instagram which client use to login into instagram
    :return:--
    """
    user_id = get_user_id(instaname)        #calling get_user_id()
    if user_id == None:
        print "There is no data in this account"  # print when id is null
    else:
        media_id = get_media_id(user_id)         #get_media_id called to get recent media of user
        if media_id == None:
            print "There is no media in this account"  # print when  media id is null
        else:
            try:
                comment = raw_input("Enter you comment= ")      #taking the comment you want to post as input
                payload = {"access_token": ACCESS_TOKEN, "text": comment}       #creating payload dictionary as passing accesstoken and comment text in it
                request_url = (BASE_URL + 'media/%s/comments') % (media_id)     #url of posting the comments on the recent post corresponding to media id
                print "POST request url : %s" % (request_url)       #printing post url
                post_comment = requests.post(request_url, payload).json()       #posting the data of the url above mentioned using requests package and using json()
            except:
                print colored("Incorrect URL!","red")       #print when incorect request url
            try:

                if post_comment['meta']['code'] == 200:     # checking the status code of request. if 200 then it is accepted otherwise the else part will work
                    print colored("Sucessfully posted the comment! :)","green")     #print when successfull  posted comments
                else:
                    print colored("Failed to post!:( TRY AGAIN","red")      #printing when failed to post the comment
            except:
                KeyError        #catching Keyerror
                print KeyError      #printing keyerror



def delete_negative_comment(instaname):
    """
    THIS function deleted the negative comments on post by analyisng  the comment using textblob
    :param instaname:  this is the username of instagram which client use to login into instagram
    :return: --
    """
    user_id = get_user_id(instaname)                                #calling get_user_id()
    if user_id == None:
        print "There is no data in this account"                 # print when id is null
    else:
        media_id = get_media_id(user_id)                         #get_media_id called to get recent media of user
        if media_id == None:
            print "There is no media in this account"                    # print when media id is null
        else:
            try:
                request_url = (BASE_URL + 'media/%s/comments/?access_token=%s') % (media_id, ACCESS_TOKEN)       #url of fetching the comments on the recent post corresponding to media id
                print 'GET request url : %s' % (request_url)                                                #print get url
                comment_info = requests.get(request_url).json()                                      #getting the data of the url above mentioned using requests package and using json()
            except:
                print colored("GET request is not working properly", "red")  # print when incorrect url

            try:
                if comment_info['meta']['code'] == 200:                                      # checking the status code of request. if 200 then it is accepted otherwise the else part will work
                    if len(comment_info['data']):                                               # checking if we have anything in data of friend's id
                        for cmnt in range(len(comment_info['data'])):                           #for loop works till the data available in comment_info
                            comment_list=comment_info['data'][cmnt]['text']                     #fetching comments
                            comment_id=comment_info['data'][cmnt]['id']                          #fetching comment id
                            blob = TextBlob(comment_list, analyzer=NaiveBayesAnalyzer())        #analysing the comment sentiment
                            if (blob.sentiment.p_neg > blob.sentiment.p_pos):                    #checking if the ratio of negative meaning of greater than positive
                                print colored("Your comment is %s :(" ,"red") %comment_list     #print if negtive comment
                                try:
                                    request_url = (BASE_URL + 'media/%s/comments/%s/?access_token=%s') %(media_id,comment_id,ACCESS_TOKEN)  #url for getting the commments
                                    print "Delete request url :%s" % (request_url)               #dislay url
                                    del_info= requests.delete(request_url).json()                   #deleting the data of the url above mentioned using requests package and using json()
                                except:
                                    print colored("Request URL not coorect!","red")              #print when url not correct
                                if del_info['meta']['code'] == 200:                             # checking the status code of request. if 200 then it is accepted otherwise the else part will work
                                    print colored("Comment deleted :) ","green")                    #print when sucessful in deleting negative comments
                                else:
                                    print colored("Unable to delete comment :(","red")              #print when unsucess in deleting comments
                            elif (blob.sentiment.p_neg==blob.sentiment.p_pos):                      #if comment have 50-50 ratio of positive and negative sentiment
                                print colored("Your comment is 50% positive and 50% negative","red")
                                choice=raw_input(colored("1.Do you want to delete this comment ? \n 2.Do you want to download this image? \n 3.Do want to go back to Main menu? ","blue"))
                                if choice=="1":
                                    try:
                                        request_url = (BASE_URL + 'media/%s/comments/%s/?access_token=%s') % (media_id, comment_id, ACCESS_TOKEN)  # url for getting the commments
                                        print "Delete request url :%s" % (request_url)                       # dislay url
                                        del_info = requests.delete(request_url).json()                       # deleting the data of the url above mentioned using requests package and using json()
                                    except:
                                        print colored("Request URL not coorect!", "red")                 # print when url not correct
                                    if del_info['meta']['code'] == 200:                                  # checking the status code of request. if 200 then it is accepted otherwise the else part will work
                                        print colored("Comment deleted :) ","green")                    # print when sucessful in deleting negative comments
                                    else:
                                        print colored("Unable to delete comment :(","red")               # print when unsucess in deleting comments
                                elif choice=='2':
                                    try:
                                        request_url = (BASE_URL + 'users/%s/media/recent?access_token=%s') % (user_id, ACCESS_TOKEN)  # url for the recent media using userid
                                        print "get request url :%s" % (request_url)                                                  # dislay url
                                        get_img = requests.get(request_url).json()                               # deleting the data of the url above mentioned using requests package and using json()
                                    except:
                                        print colored("Request URL not coorect!", "red")                        # print when url not correct
                                    if (get_img['meta']['code']) == 200:                                             # checking the status code of request. if 200 then it is accepted otherwise the else part will work
                                        if len(get_img['data']):                                                     # checking if we have anything in data of friend's id
                                            image_name = get_img['data'][0]['id'] + '.jpeg'                         # fetching post id from data and storing it in image_name with .jpeg extension
                                            image_url =get_img['data'][0]['images']['standard_resolution']['url']               # getting url of post and storing in image_url
                                            urllib.urlretrieve(image_url,image_name)                                    # retriving the image from image_url and saving in image_name
                                            print colored('Your image has been downloaded! :) ', "green")               # SUCCESS MESSASGE
                                    elif choice=='3':
                                        StartBot()
                                else:
                                    print colored("You entered a wrong choice !","red")                                #print when wrong choicce entered
                            else:
                                print colored("%s is a Positive comment :) ","green") % (comment_list)              #print when its a positive commment
                    else:
                        print colored("No comments present on this post","red")                           #print when no comments present on post
                else:
                    print colored("The request url is not in accepted state","red")                  # print when status is in "not accepted" state
            except:
                KeyError    #catching keyerror
                print KeyError  #printing keyerror



def like_min_liked_post(id):
    """
     This function gets media id as input and like that post

    :param id: this is the media id of the post with minimum likes
    :return: --
    """

    if id == None:  # check if media id none
        print colored("There is no media in this account", "red")  # print when media id is null
    else:
        try:
            request_url = (BASE_URL + 'media/%s/likes') % (id)  # url to like the post using media id
            payload = {"access_token": ACCESS_TOKEN}  # payload as a dictionary
            print 'POST request url : %s' % (request_url)  # display the POST url
            post_like = requests.post(request_url,payload).json()  # posting  the data to the url above mentioned using requests package and using json()
        except:
            print colored("POST request is not working properly", "red")  # print when incorrect url

        try:
            if post_like['meta']['code'] == 200:  # checking the status code of request. if 200 then it is accepted otherwise the else part will work
                print colored("SUCESSFULLY LIKED THE POST :)", "green")  # print if post is sucessfully liked
            else:
                print colored("You couldn't like the POST :( ", "red")  # printing if post is not sucessfully liked
        except:
            KeyError  # catch keyerror
            print KeyError  # printing keyerror



def choose():
    """
    this function choose the post with either minimum no of likes or by searching in caption a particular word or sentence

    :param : --
    :return: --
    """

    print colored("Choose one of the following option:) ","green")       #telling user to choose any of option
    print colored("a.Choose post with minimum likes of user","yellow")
    print colored("b.Choose any recent post by tag of user","yellow")
    choice=raw_input("Enter your choice: ")         #taking choice input from user and storing in choice variable
    if choice=='a':
        instaname=raw_input("Enter the username")
        user_id=get_user_id(instaname)          #calling get_user_id() and passing the user's instagram name as parameter
        if user_id==None:
            print colored("Invalid username :(",'red')      #if user_id returned from get_user_id() is none then print invalid user!.
        else:
            try:
                request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, ACCESS_TOKEN)   # getting users media list from "user/user_id/media/recent" end point
                print "Get url is: %s" % (request_url)      # display the GET url
                user_media = requests.get(request_url).json()       # requesting to get the data from the url above mentioned using requests package and using json()
            except:
                print colored("GET request is not working properly", "red")  # print when incorrect url

            try:
                if user_media['meta']['code'] == 200:       # checking the status code of request. if 200 then it is accepted otherwise the else part will work
                    if len(user_media['data']):     # checking if we have anything in data of user's id
                        like_list=[]        #creating a list
                        for i in range(len(user_media['data'])):        #for every i the data list
                            likes=user_media['data'][i]['likes']['count']       #getting the like count
                            url=user_media['data'][i]['images']['standard_resolution']['url']       #getting url of posts
                            like_list.append(likes)     #appending the no of likes on every post in like_list[]
                        min_count=min(like_list)            #finding minimum in list
                        print colored("Least number of likes is %s" ,"magenta")%(min_count)
                        #providing user with certain options
                        choice=raw_input("What do you want to do with this post with least likes? \n 1. Download this image?\n 2. Like this post? \n 3.Return to main menu? ")
                        if choice=="1":                                             #download  image function
                            for i in range(len(user_media['data'])):             #for every i the data list
                                if user_media['data'][i]['likes']['count']==min_count:      #comparing no of likes of every post with min likes
                                    get_id=user_media['data'][i]['id']      #fetching id of min liked post
                                    image_name = get_id + '.jpeg'
                                    image_url = user_media['data'][i]['images']['standard_resolution']['url']       #fetching image url
                                    urllib.urlretrieve(image_url, image_name)       #downloadinf image
                            print colored('Your image has been downloaded! :)', 'green')
                        elif choice=="2":           #like the post with min no of liked
                            for i in range(len(user_media['data'])):            #for every i the data list
                                if user_media['data'][i]['likes']['count']==min_count:      #comparing no of likes of every post with min likes
                                    id=user_media['data'][i]['id']      #fetching id of min liked post
                                    like_min_liked_post(id)         #calling like_min_liked_post() function and passing id as parameter
                        elif choice=="3":
                            StartBot()          #going back to main menu
                        else:
                            print colored("Enter the correct choice :( ","red")     #print when wrong choice entered
                    else:
                        print colored("There is no data :(", "red")  # print when no data
                else:
                    print colored("The request url is not in accepted state","red")  # print when status is in "not accepted" state
            except:
                KeyError  # catching Key error
                print KeyError  # printing keyerror

    elif choice=='b':
        username=raw_input(colored("Enter the username whose post you want to choose using caption?","blue"))       #getting username
        user_id=get_user_id(username)       #fetching user id from get_user_id() function
        if user_id==None:
            print colored("Invalid user :( ","red")     #if user_id returned from get_user_id() is none then print invalid user!.
        else:
            try:
                request_url = (BASE_URL + 'users/%s/media/recent?access_token=%s') % (user_id,ACCESS_TOKEN)      # getting users media list from "user/user_id/media/recent"
                print "GET request url: %s" % (request_url)     #print GET url
                media_list = requests.get(request_url).json()       # requesting to get the data from the url above mentioned using requests package and using json()
            except:
                print colored("GET request is not working properly", "red")  # print when incorrect url
            try:
                if media_list['meta']['code']==200:      # checking the status code of request. if 200 then it is accepted otherwise the else part will work
                    if len(media_list['data']):# checking if we have anything in data of user's id
                        word=raw_input(colored("Enter the word you want to search in caption : ","green"))      #get the word you want to search in caption or hashtag
                        list=[]         #creating list
                        for i in range(len(media_list['data'])):        #for every i the data list
                            if media_list['data'][i]['caption']!=None:      #checking if caption is there or not
                                caption=media_list['data'][i]['caption']['text']        #if caption is present then store it in variable
                                list.append(caption)            #appending the caption in list
                            else:
                                print colored("You dont have any caption ","red")       #print if no caption present
                        if len(list)>0:         #check if there is any caption in list
                            for i in range(len(list)):      #for every i the data list
                                if word in list[i]:         #if word which is  searched is present in caption
                                    print colored("The caption is : %s ","magenta") % list[i]
                                    choice=raw_input(colored("Do you want to download this image or not? Y/N ","green"))        #asking if user want to download the post retrieved uby searching caption
                                    if choice.upper()=="Y":     #if yes then download
                                        id = media_list['data'][i]['id']        #fetching id
                                        image_name = id + '.jpeg'
                                        image_url = media_list['data'][i]['images']['standard_resolution']['url']       #fetching url
                                        urllib.urlretrieve(image_url, image_name)       #downloading image
                                        print colored('Your image has been downloaded!', 'blue')        #print when image downloaded sucessfully
                                    elif choice.upper()=="N" :           #if no then return None
                                        return None
                                    else:
                                        print colored("Enter either Y or N!","red")     #print when wrong choice entered

                        else:
                            print colored("No Such caption Available ","red")        #no caption in any post
                    else:
                        print colored("No data available!",'red')           # print when no data
                else:
                    print colored("The request url is not in accepted state","red")      # print when status is in "not accepted" state
            except:
                KeyError            #Catching keyerror
                print KeyError      #printing keyerror
    else:
        print colored("Choose either a or b !",'red')       #if wrong choice entered then print this



def recent_media_liked():
    """
    This function download the recent image liked by you/self.
    :return: --
    """

    print colored("Hi! Recent post liked by you is downloading...","cyan")
    try:
        request_url = (BASE_URL + "users/self/media/liked?access_token=%s") %( ACCESS_TOKEN)  # getting like from instagram using "user/self/media/like" end point
        print "The GET request url is %s" % (request_url)  # display the GET url
        liked_post = requests.get(request_url).json()  # requesting to get the data from the url above mentioned using requests package and using json()
    except:
        print colored("GET request is not working properly", "red")  # print when incorrect url
    try:
        if (liked_post['meta']['code']) == 200:  # checking the status code of request. if 200 then it is accepted otherwise the else part will work
            if len(liked_post['data']):  # checking if we have anything in data of friend's id
                image_name = liked_post['data'][0]['id'] + '.jpeg'  # fetching post id from data and storing it in image_name with .jpeg extension
                image_url = liked_post['data'][0]['images']['standard_resolution']['url']  # getting url of post and storing in image_url
                urllib.urlretrieve(image_url, image_name)  # retriving the image from image_url and saving in image_name
                print colored('Your image has been downloaded!', "green")  # SUCCESS MESSASGE
            else:
                print colored("You did'nt liked any post recently !",'red')  # print if no recent post
        else:
            print colored("The request url is not in accepted state","red")  # print when status is in "not accepted" state
    except:
        KeyError  # catching keyerror of dictionary user-info
        print KeyError #printing key error



def display_pie_chart(instaname):
    """
    this fucntion compares the ratio of postive and negative posts on a post and displays a pie chart comparing the percentages
    :param instaname:  this is the username of instagram which client use to login into instagram
    :return: --
    """

    user_id = get_user_id(instaname)        #calling get_user_id()
    if user_id == None:
        print "There is no data in this account"  # print when id is null
    else:
        media_id = get_media_id(user_id)        #get_media_id called to get recent media of user
        if media_id == None:
            print "There is no media in this account"  # print when media id is null
        else:
            request_url = (BASE_URL + 'media/%s/comments/?access_token=%s') % (media_id, ACCESS_TOKEN)  #url of fetching the comments on the recent post corresponding to media id
            print 'GET request url : %s' % (request_url)      #print get url
            comment_info = requests.get(request_url).json()     #getting the data of the url above mentioned using requests package and using json()

            if comment_info['meta']['code'] == 200:      # checking the status code of request. if 200 then it is accepted otherwise the else part will work
                if len(comment_info['data']):        # checking if we have anything in data of friend's id
                    list=[]             #declaring empty string
                    for cmnt in range(len(comment_info['data'])):       #for loop works till the data available in comment_info
                        comment_list = comment_info['data'][cmnt]['text']            #fetching comments
                        list.append(comment_list)       #append the comments in list

                    comment = ''.join(list)     #converting list into string
                    blob = TextBlob(comment, analyzer=NaiveBayesAnalyzer())     #analysing the comment sentiment
                    values = [blob.sentiment.p_pos, blob.sentiment.p_neg]       #storing the postive rativo and negative ratio in a list
                    labels = ['Positive\nComments', 'Negative\nComments']       #label list for pie chart
                    fig = plt.figure()          #calling figure() funtion of plt
                    fig.patch.set_facecolor('pink')     #setting  facecolor to pink
                    fig.patch.set_alpha(0.7)        #setting occupacy to 0.7
                    col = ['blue', 'yellow']        #list of color user respective to list of values
                    #plt.pie is used to plot pie chart. values are the values of slices, labels are label corresponding to value, startange is the from where we can
                    #start printing the slice, autopct calculate percentage, colors is color of corresponding slice, shadow is 3D view, explode is when
                    #one of the slice is coming
                    plt.pie(values, labels=labels, startangle=90, autopct='%1.1f%%', colors=col, shadow=True,explode=(0, 0.1))
                    plt.title("Negative VS Positive Comments \n (Percentage Comparison)")       #printing title of pie chart
                    plt.legend()        #legend places a legend on various types of graphs (line plots, bar graphs, pie charts, etc.).
                                        # For each pie chart plotted, the legend shows a sample of the line type, marker symbol, and color beside the text label you specify.
                    plt.show()      #show the pie chart

                else:
                    print colored("No comments present on this post", "red")        #print if no comments on this post
            else:
                print colored("The request url is not in accepted state","red")  # print when status is in "not accepted" state

def Bar_graph():
    """
    this function prints the bargraph of popular hashtags on instagram
    :return:--
    """
    try:
        default_count = []      #list of hashtags you want to see in bargraph
        choice = raw_input(colored('Make a choice ?\n 1. Enter your own hashtags?\n 2. Use predefined hashtags? \n 3. Back to menu? ',"magenta"))
        hashtags=[]             #creating a list where hastags will be stored
        count=[]            #storing the no of posts on instagram of particular hashtag
        number=0        #no. of bars in your bargraph
        if choice == '1':
            number = int(raw_input('Enter the no. of popular hashtags do you want to enter:'))  #getting no. of hastags you want to enter n storing it in number
            print 'Enter %d hash tags:' % number
            for i in range(number):
                default_count.append(i + 1)     #appending in default count list
                hashtags.append(raw_input())        #getting the input if hashtags and storing in "hashtags" variable
        elif choice=='2':
            default_count= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            hashtags = ['morning','beautiful','cute','smile','love','rain','insta','life','music','dance']      #default hashtags
            number = 10         #number of hashtags by  default is 10
        elif choice=='3':
            StartBot()      #StartBot called
        else:
            print colored("Enter right choice :(","red")
            StartBot()      #StartBot called if wrong choice entered

        for i in range(number):
            try:
                request_url = BASE_URL + "tags/%s/?access_token=%s" % (hashtags[i], ACCESS_TOKEN)       #url of fetching the data of popular hashtags in hashtags[i] list
                print 'GET request url : %s' % request_url          #printing get url
                tag = requests.get(request_url).json()           #getting the data of the url above mentioned using requests package and using json()
            except:
                print colored("GET request is not working properly", "red")  # print when incorrect url
            try:
                if tag['meta']['code'] == 200:  # checking the status code of request. if 200 then it is accepted otherwise the else part will work
                    if len(tag['data']):                  # checking if we have any data or not
                        count.append(tag['data']['media_count'])        #appending the no of times a particular tag is used in count url
                    else:
                        print colored("Tag not found : #%s","red") % hashtags[i]        #print when tag not found
                        StartBot()          #calling startbot function
                else:
                    print colored("The request url is not in accepted state","red")  # print when status is in "not accepted" state
            except:
                print KeyError      #print if any keyerror found

        fig2 = plt.figure()         # calling figure() funtion of plt
        fig2.patch.set_facecolor('pink')         # setting  facecolor to pink
        fig2.patch.set_alpha(0.7)       # setting occupacy to 0.7
        colors=['red', 'blue', 'black', 'yellow', 'green','grey','cyan','orange']       #colors for bars

        # for plt.bar you can see the example and compare what is default_count and count
            # y = [3, 10, 7, 5, 3, 4.5, 6, 8.1]
            #N = len(y)
            #x = range(N)
            #width = 1/1.5
            #plt.bar(x, y, width, color="blue")
        plt.bar(default_count, count, tick_label=hashtags,color=colors, width=0.8)
        plt.xlabel('--Name of hashtags--')      #settinf x axis label
        plt.ylabel('--Number of occurence of hashtag--')        #setting y axis label
        plt.title('BarGraph of frequency of occurence of popular Hashtags :)')      #setting title
        plt.show()          #displays bargraph
    except:
        print colored("Function not working properly","red")        #print when any error in code

#function contaning various menu option
def StartBot():
    """
    This is the main function of this instabot app which contain various menu options .user can use various menu options
    :return:--
    """
    while True:
        print colored("Hey! :) ","magenta")
        print colored("Welcome to InstaBot app","yellow")                         #   ***  WELCOMING INSTABOT USER ***
        print colored('Here are your menu options:',"red")                 #Printing various menu option
        print "a.Get your own details\n"
        print "b.Get details of a user by username\n"
        print "c.Get your own recent post\n"
        print "d.Get user's recent post by username\n"
        print "e.Get list of people who has liked your recent post\n"
        print "f.Like the post of your friend\n"
        print "g.Unlike the post of your friend\n"
        print "h.Get the list of recent comment on your post\n"
        print "i.Comment on post\n"
        print "j.Delete negative comments \n"
        print "k.Display pie chart comparing negative and positive comments on a post \n"
        print "l.To choose post by minimum likes or tag\n"
        print "m.To get the recent media liked by the user \n"
        print "n.Plot the Bar graph of Trending Hash Tags\n"
        print "o.Exit the application"
        choice = raw_input(colored("Enter you choice: ","yellow"))        #getting menu choice from user
        if len(choice)>0 and len(choice)<2 and choice.isalpha()==True and choice.isspace()==False :   #check if correct choice entered
            if choice == "a":
                self_info()         #if choice is "a" then self_info() is called
            elif choice == "b":
                insta_username = raw_input(colored("Enter the username of the user: ","blue"))
                get_user_info(insta_username)     #if choice is "b" then get_user_info() is called and input insta name is passed as parameter
            elif choice == "c":
                get_own_post()      #if choice is "c" then get_own_post() is called
            elif choice == "d":
                insta_username = raw_input(colored("Enter the username of the user: ", "blue"))
                get_user_post(insta_username)  # if choice is "d" then get_user_post() called and input insta name is passed as parameter
            elif choice=="e":
                insta_username = raw_input(colored("Enter the username of the user: ", "blue"))
                get_like_list(insta_username)       # if choice is "e" then get_like_post() called and input insta name is passed as parameter
            elif choice=="f":
                insta_username = raw_input(colored("Enter the username whose post you want to like: ", "blue"))
                like_a_post(insta_username)     # if choice is "f" then like_a_post() called and input insta name is passed as parameter
            elif choice == "g":
                insta_username = raw_input(colored("Enter the username whose post you want to unlike: ", "blue"))
                unlike_a_post(insta_username)       # if choice is "g" then unlike_a_post() called and input insta name is passed as parameter
            elif choice == "h":
                insta_username = raw_input(colored("Enter the username whose comment you want to see on recent post: ", "blue"))
                get_comment_list(insta_username)        # if choice is "h" then get_comment_list() called and input insta name is passed as parameter
            elif choice == "i":
                insta_username = raw_input(colored("Enter the username whose post you want to comment on: ", "blue"))
                comment_on_post(insta_username)     # if choice is "i" then comment_on_post() called and input insta name is passed as parameter
            elif choice=="j":
                insta_username = raw_input(colored("Enter the username on whose id u want to delete the comments:" , "blue"))
                delete_negative_comment(insta_username)     # if choice is "j" then delete_negative_comment() called and input insta name is passed as parameter
            elif choice=="k":
                insta_username = raw_input(colored("Enter the username whose comments-comparison pie chart you want to see : " , "blue"))
                display_pie_chart(insta_username)       # if choice is "k" then display_pie_chart() called and input insta name is passed as parameter
            elif choice=="l":
                choose()       #choose function called
            elif choice=="m":
                recent_media_liked()        #calling recent_media_liked() function
            elif choice=="n":
                Bar_graph()     #calling  bargarph function
            elif choice=='o':
                exit()              #exit the program
            else:
                print colored("You have entered a wrong choice","red")      #print when wrong choice entered
        else:
            print colored("You have entered a wrong choice !Try Again","red")       #print when wrong choice entered

StartBot()      #recall the StartBot()

