import sys
import json

import cognitive_face as CF

import local_settings as settings # defines KEY, BASE_URL

# usage:
#  detect.py path-to-file

def main():
    CF.Key.set(settings.KEY)
    CF.BaseUrl.set(settings.BASE_URL)
    result = CF.face.detect(sys.argv[1])
    # TODO: check for more than one face
    face_id = result[0]['faceId']
    result = CF.face.find_similars(face_id,face_list_id=1)    
    face_list = CF.face_list.get(1)
    if len(result) > 0:
        # TODO: threshold on confidence
        persisted_id = result[0]['persistedFaceId']
        
        for persisted_face in face_list['persistedFaces']:
            if persisted_face['persistedFaceId'] == persisted_id:
                print(json.loads(persisted_face['userData'])['user'])
                break

if __name__ == '__main__':
    main()

