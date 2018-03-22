from mopidypost import Mopidy


mpd = Mopidy("http://192.168.2.100:6680")
#print(mpd.get_poddcast())
print(mpd.currently_playing())
podcasts = mpd.get_poddcast()
for pod in podcasts:
  if "giant".lower() in pod["name"].lower():
    print(pod)
#print(podcasts)
#apodd =  mpd.get_poddcast(podcasts[3]['uri']);

#mpd.add_list(apodd[0]['uri'])

