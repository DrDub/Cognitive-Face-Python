import sys

import cognitive_face as CF

import local_settings as settings # defines KEY, BASE_URL


# usage:
#  train.py name path-to-file

def main():
    CF.Key.set(settings.KEY)
    CF.BaseUrl.set(settings.BASE_URL)
    CF.face_list.add_face(sys.argv[1],1,'{"user":"' + sys.argv[2] + '"}')

if __name__ == '__main__':
    main()

