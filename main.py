from app import randImg
import json

if __name__ == "__main__":
    print(json.dumps(randImg(30)))
