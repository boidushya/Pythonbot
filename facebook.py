import facebook
 
access_token = ''
 
facebook_page_id = ''
 
graph = facebook.GraphAPI(access_token)
 
msg = 'Hello facebook! This is my first bot made with Python!'
 
graph.put_photo(image = open('/path/to/photo/<name>.<extension>', 'rb'), message= msg)
print('Photo has been uploaded to facebook!')

post_id = graph.put_photo(image = open('/path/to/photo/<name>.<extension>', 'rb'), message= msg)['post_id']
print('Photo with post id: ' + post_id + ' has been successfully uploaded to facebook!')# a tad bit advanced confirmation!
 
comment_msg = 'This is a bot posted comment!'
graph.put_comment(object_id = post_id, message = comment_msg)
 
graph.put_object(parent_object = post_id, connection_name='comments',message = comment_msg, attachment_url='<url to photo goes here>')
 

