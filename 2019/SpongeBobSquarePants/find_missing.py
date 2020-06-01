import os
import xml.etree.ElementTree as ET

SCRIPT_PATH = os.path.dirname(__file__)

def ReadEpisodeIdFromXml (file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    episodIds = []
    for child in root:
        seasonNumber = child.find("SeasonNumber")
        if seasonNumber is None:
            continue
        episodeNumber = child.find("EpisodeNumber")
        # episodeName = child.find("EpisodeName")
        episodId = "S{0:02}E{1:02}".format(int(seasonNumber.text), int(episodeNumber.text))
        episodIds.append(episodId)
    return episodIds

###

y = os.path.join(SCRIPT_PATH, "data", "AllEpisodsFromTVDB.xml")
x = ReadEpisodeIdFromXml(y)
print x
print len(x)
