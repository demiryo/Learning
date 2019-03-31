import os
import xml.etree.ElementTree as ET

SCRIPT_PATH = os.path.dirname(__file__)

file_path = os.path.join(SCRIPT_PATH, "data", "AllEpisodsFromTVDB.xml")
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

print episodIds
print len(episodIds)
