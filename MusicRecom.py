from pyspark import SparkContext
from pyspark import SparkConf
from pyspark.mllib.recommendation import ALS, MatrixFactorizationModel, Rating

conf = SparkConf().setMaster("local")
sc = SparkContext(conf=conf)

artistAlias = sc.textFile("s3://csdshw52017/audio_data/artist_alias.txt")
artistData = sc.textFile("s3://csdshw52017/audio_data/artist_data.txt")
rawUserArtistData = sc.textFile("s3://csdshw52017/audio_data/user_artist_data.txt")

def parseAlias(data):
    data = data.split("\t")
    if data[0] != "": 
        return [(int(data[0]), int(data[1]))]
    else:
        return ()

artistAlias = artistAlias.flatMap(parseAlias).collectAsMap()

def parseArtist(data):
    if "\t" not in data:
        return ()
    data = data.split("\t")
    try: 
        return [(int(data[0]), data[1].strip())]
    except: 
        return()

artistData = artistData.flatMap(parseArtist)

from pyspark.mllib.recommendation import ALS, Rating
bArtistAlias = sc.broadcast(artistAlias)

def parseUserArtist(data):
    userID, artistID, count = map(int, data.split(" "))
    finalArtistID = bArtistAlias.value.get(artistID)
    if finalArtistID is None:
        finalArtistID = artistID
    return Rating(userID, finalArtistID, count)

trainData = rawUserArtistData.map(parseUserArtist).cache()

model = ALS.trainImplicit(trainData, 10, 5, alpha=1.0)
recID = [i[1] for i in model.call("recommendProducts", 2093760, 10)]
rst = artistData.filter(lambda i: i[0] in recID).values().collect()
for i in range(0, 10):
    print("{}: {}".format(i+1, rst[i]))