
"""
               !!!!!!!!!!!    TL;DR at the bottom   !!!!!!!!!!!
"""
 
import facebook
#The facebook module is imported. You can download it via pip with 'pip install facebook-sdk'
 
"""
An optimum way to post on your facebook page is with Max's tool
Generally getting an access_token for your page is very hard,
But thanks to Max, its extremely easy now!
First make a new page on facebook from your account.
You can leave the part to fill your profile picture/cover photo/description as you can always do it later
Just go to http://maxbots.ddns.net/token and do the necessary stuff
Then come back here and within the single quotes after access_token ,
Fill in the access token below you just generated for your page
"""
 
#Your access_token goes below...Never share you access_token with anyone, it is like a password but for your page...
access_token = ''
 
#filling the facebook_page_id is optional but is suggested by some botmins...
facebook_page_id = ''
 
#A graph class is initialised to do all the automation stuff!
graph = facebook.GraphAPI(access_token)
 
#Change the message below to whatever you like but make sure its within quotes(either double or single)
msg = 'Hello facebook! This is my first bot made with Python!'
 
"""
The put_photo function posts a photo to your facebook page. Previously you could just post text
But thanks to facebook, you can't do that anymore. You NEED to post a picture with your text.
This picture can be arbitary but some botmins made a 400*1 white image to attach with the post
If you want the 400*1 image, go to : https://i.ibb.co/jLdj1ry/IMG-20190926-190753.jpg and download it to some folder and below, replace /path/to/photo/<name>.<extension> with the path to the picture
For example if you saved the image to C:/downloads/pic.jpg, then next line would read as
graph.put_photo(image = open('C:/downloads/pic.jpg', 'rb'), message= msg)
"""
 
graph.put_photo(image = open('/path/to/photo/<name>.<extension>', 'rb'), message= msg)
print('Photo has been uploaded to facebook!') #just a confirmation that the photo has been successfully uploaded
 
"""
The put_photo function returns to us a large variety of other important stuff about the image we just posted
But right now, very few of them are necessary.
For instance if you want your bot to place a comment on your newly generated post automatically,
We would need a post_id for reference.
Fortunately the put_photo returns post_id in form of a json variable which we can easily access by storing it in a variable called post_id!
"""
 
post_id = graph.put_photo(image = open('/path/to/photo/<name>.<extension>', 'rb'), message= msg)['post_id']
print('Photo with post id: ' + post_id + ' has been successfully uploaded to facebook!')# a tad bit advanced confirmation!
 
#now we can start the process of putting a comment on our post!
comment_msg = 'This is a bot posted comment!'
graph.put_comment(object_id = post_id, message = comment_msg)
 
# you can also include a picture with your comment with:
graph.put_comment(object_id = post_id, message = comment_msg, attachment_url='<url to photo goes here>')
 
"""
Thats it! These are almost all the basics you need to know for making your first bot!
Remember, do not be a copy-paster, try to understand everything you type!
A good place to learn python(if you haven't already) is through
Automate the Boring Stuff with Python
or
Learning Python the Hard Way (trust me its not that hard though)
otherwise, there are always good youtube tutorials, but try to avoid those which
Claim to teach you python in an hour or so.
If you have any problems/query regarding facebook bots or python, you can contact me at
https://www.facebook.com/soumyadipta.despacito
https://www.reddit.com/u/Boidushya
or The Bot Appreciation Society Discord's bot-help section
If you feel you need even more help, go to stackoverflow.com and submit you question. They generally get answered within a day or so
Oh and finally, please don't use Notepad/Notepad++/Python IDLE for editing/making python scripts
Theres no harm but its not that efficient
Use Atom (www.atom.io) / Sublime Text / Visual Studio Code instead
"""
 
#TL;DR:
 
import facebook
access_token = '' #here goes your access token from http://maxbots.ddns.net/token
graph = facebook.GraphAPI(access_token)
msg = 'Hello facebook! This is my first bot made with Python!' #message for the post
comment_msg = 'This is a bot posted comment!' #message for the comment
post_id = graph.put_photo(image = open('/path/to/photo/<name>.<extension>', 'rb'), message= msg)["post_id"] #photo got posted!
print('Photo has been uploaded to facebook!')
graph.put_comment(object_id = post_id, message = comment_msg, attachment_url='<url to photo goes here>')#comment got posted!
 
"""
If you want to test straight away, generate an access_token from http://maxbots.ddns.net/token
Copy the TL;DR section and paste it to a new file
Save it as main.py
Open your command prompt/powershell/terminal and type
python main.py
Linux/Mac users may need to add a sudo in front and python3 instead of python
"""
