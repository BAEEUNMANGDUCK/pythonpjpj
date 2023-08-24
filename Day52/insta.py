from insta_archi import InstaFollower

URL = "https://www.instagram.com/"
USER_NAME = "blahblah@kakao.com"
USER_PASSWORD = "blahblah"
SIMILAR_ACCOUNT = "thekfa"

insta = InstaFollower(url)
insta.login(USER_NAME, USER_PASSWORD)
insta.find_followers(SIMILAR_ACCOUNT)
insta.follow()
