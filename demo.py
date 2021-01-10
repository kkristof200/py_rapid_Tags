from rapid_tags import RapidTags, Platform

# print(RapidTags().get_tags('python', debug=True))
# or
print(RapidTags.get_tags_cls('python', platform=Platform.Youtube, debug=True))
print(RapidTags.get_tags_cls('python', platform=Platform.Tiktok, debug=True))