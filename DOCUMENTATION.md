# Documentation

In this documentation we will be understanding all the code block by block.

```Python
import facebook
```

The module `facebook` is imported, you can use it by typing `pip install
facebook-sdk` on your terminal.


```Python
access_token = ''
```

Generally getting an access_token for your page is very hard, but thanks to
Max, its extremely easy now!

First make a new page on facebook from your account.

You can leave the part to fill your profile picture/cover photo/description as
you can always do it later

Just go to http://maxbots.ddns.net/token and do the necessary stuff. Then come
back here and within the single quotes after access_token fill in the access
token below you just generated for your page. Remember that the access token is
like a password but for your program and you must not share it to anyone.

```Python
facebook_page_id = ''
```

Filling the facebook_page_id is optional but is suggested by some botmins...

```Python
graph = facebook.GraphAPI(access_token)
```

A graph class is initialised to do all the automation stuff!

```Python
msg = 'Hello facebook! This is my first bot made with Python!'
```

You can change the message to whatever you like but make sure its within quotes
(either double or single, both are valid in Python).

## Uploading photos

```Python
graph.put_photo(image = open('/path/to/photo/<name>.<extension>', 'rb'), message= msg)
print('Photo has been uploaded to facebook!') 
```

The put_photo function posts a photo to your facebook page. Previously you
could just post text, Bbt thanks to facebook, you can't do that anymore. You
NEED to post a picture with your text. This picture can be arbitary but some
botmins made a 400x1 white image to attach with the post If you want the 400x1
image, go to: [https://i.ibb.co/jLdj1ry/IMG-20190926-190753.jpg ](https://i.ibb.co/jLdj1ry/IMG-20190926-190753.jpg)
and download it to some folder and below, replace
`/path/to/photo/<name>.<extension>` with the path to the picture.

For example if you saved the image to C:/downloads/pic.jpg, then next line
would read as `graph.put_photo(image = open('C:/downloads/pic.jpg', 'rb'),
message= msg)`

```Python
post_id = graph.put_photo(image = open('/path/to/photo/<name>.<extension>', 'rb'), message= msg)['post_id']
print('Photo with post id: ' + post_id + ' has been successfully uploaded to facebook!')
```

The put_photo function returns to us a large variety of other important stuff
about the image we just posted but right now, very few of them are necessary.
For instance if you want your bot to place a comment on your newly generated
post automatically, We would need a post_id for reference. Fortunately the
put_photo returns post_id in form of a json variable which we can easily access
by storing it in a variable called post_id!

## Adding comments

```Python
#now we can start the process of putting a comment on our post!
comment_msg = 'This is a bot posted comment!'
graph.put_comment(object_id = post_id, message = comment_msg)
 
# you can also include a picture with your comment with:
graph.put_object(parent_object = post_id, connection_name='comments',message = comment_msg, attachment_url='<url to photo goes here>')
```

For adding comments without a photo you have to use the function `put_comment`
adding to object_id the post id of the post you are commenting and the message
on message. If you want to add with pictures ypu have to use the function
`put_object` as in the example adding the post id to parent_object, `comments`
to connection_name, the message of the comment to message and the url of the
picture to attachment_url.

---

Thats it! These are almost all the basics you need to know for making your first
bot!

Remember, do not be a copy-paster, try to understand everything you type! A
good place to learn python(if you haven't already) is through Automate the
Boring Stuff with Python or Learning Python the Hard Way (trust me its not that
hard though). Otherwise, there are always good youtube tutorials, but try to
avoid those which claim to teach you python in an hour or so.

If you have any problems/query regarding facebook bots or python, you can
contact me at [Facebook](https://www.facebook.com/soumyadipta.despacito) or
[Reddit](https://www.reddit.com/u/Boidushya) or The Bot Appreciation Society
Discord's bot-help section.

If you feel you need even more help, go to
[stackoverflow.com](stackoverflow.com) and submit you question. They generally
get answered within a day or so.

Oh and finally, please don't use Notepad/Notepad++/Python IDLE for
editing/making python scripts, there's no harm but its not that efficient.
Use [Atom](www.atom.io)/Sublime Text/Visual Studio Code instead.

