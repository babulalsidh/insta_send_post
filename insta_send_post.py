from instagrapi import Client

# Log in to your account
cl = Client()
cl.login('babulal_sidh_764', '23@2005')

# Upload a photo C:\Users\babul\Pictures\Camera Rollwith a caption
cl.photo_upload("C:\\Users\\babul\\Pictures\\Camera Roll\", "my post")
