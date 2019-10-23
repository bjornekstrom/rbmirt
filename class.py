# Classification code:

# Science student

students = ["student", "studying", "undergraduate student", "undergrad student", "bsc student", "bachelor student", "msc student", "ma student", "mfa student", "masters student", "doctoral student", "phd student", "doctoral candidate", "phd candidate", "dphil student", "dphil candidate", "graduate school", "gradschool", "history major", "philosophy major", "studies major", "english major", "nursing major" "business major", "marketing major", "fashion major", "dietics major", "psychology major", "biology major", "college major", "justice major", "cyber major"]

value = value.lower()

if any(x in value for x in students):
    return "Science student"
else:
    return ""

# Graduated

graduated = ["MS", "MA", "MBA", "BA", "BS", "educated", "PhD", "college graduate", "university graduate", "graduate"]

value = value.lower()

if any(x in value for x in graduated):
    return "Graduated"
else:
    return ""

# University faculty (academic)

unifac = ["lectur", "prof.", "professor", "professeur", "profesor", "research chair", "dean", "faculty", "distinguished chair", "post doc", "post-doc", "post–doc", "postdoc", "research fellow", "researcher", "scientist"]

value = value.lower()

if any(x in value for x in unifac):
    return "University faculty (academic)"
else:
    return ""

# Other scientist or science-associated group

othersci = ["technician", "academic", "research ass", "research scientist", "lab manager", "oceanographer", "chemist", "ologist", "icist", "ician", "scientist", "scholar", "otanist", "atrist"]

value = value.lower()

if any(x in value for x in othersci):
    return "Other scientist or science-associated group"
else:
    return ""

# Education and outreach professional

eduout = ["museum", "museo", "musee", "curator", "smithsonian", "educator", "teacher", "classrooms", "science class", "librarian", "archivist", "outreach", "education", "teach"]

value = value.lower()

if any(x in value for x in eduout):
    return "Education and outreach professional" 
else:
    return ""

# Applied science organization

applied = ["foundation", "society", "non-governmental", "nongovernmental", "non governmental", "non–governmental", "organisation", "organization", "nonprofit", "non-profit", "non–profit", "philantropy", "stewardship", "policy officer", "capacity development", "international development", "intergovernmental", "nonpartisan", "non-partisan", "non–partisan", "non partisan", "community organisation", "community organization", "think tank", "think-tank", "thinktank", "think–tank"]

value = value.lower()

if any(x in value for x in applied):
    return "Applied science organization"
else:
    return ""

# Other professional

otherprof = ["recruiter", "entrepreneur", "manager", "marketer", "designer", "programmer", "coder", "self-employ", "self employ", "marketing", "strategist", "operator", "consultant", "investor", "engineer", "architect", "doctor", "nurse", "developer", "programming", "coding", "devops", "trader", "consultant", "lawyer", "business owner"]

value = value.lower()

if any(x in value for x in otherprof):
    return "Other professional"
else:
    return ""

# Media professional

media = ["writer", "journalis", "blog", "screenwriter", "publisher", "corresponden", "comms", "communicator", "scicomm", "author", "producer", "production", "audio", "radio", "podcast", "documentar", "film", "photographer", "report", "show", "movie", "copyeditor", "copy editor", "copy-editor", "copy–editor", "broadcast", "television", "communicatio", "freelance", "videograph", "editor", "foto", "publish", "media guy", "newspaper", "youtuber", "influencer"]

value = value.lower()

if any(x in value for x in media):
    return "Media professional"
else:
    return ""

# Policy/decision maker

dm = ["public servant", "government agency", "eu commission", "eucommission", "congressional", "congressman", "congresswoman", "senator", "senate", "parliament", "municipal", "labour candicate", "independent candidate", "legislator", "european commission"]

value = value.lower()

if any(x in value for x in dm):
    return "Policy/decision maker"
else:
    return ""

# General public

students = ["student", "studying", "undergraduate student", "undergrad student", "bsc student", "bachelor student", "msc student", "ma student", "mfa student", "masters student", "doctoral student", "phd student", "doctoral candidate", "phd candidate", "dphil student", "dphil candidate", "graduate school", "gradschool", "history major", "philosophy major", "studies major", "english major", "nursing major" "business major", "marketing major", "fashion major", "dietics major", "psychology major", "biology major", "college major", "justice major", "cyber major",]

graduated = ["MS", "MA", "MBA", "BA", "BS", "educated", "PhD", "college graduate", "university graduate", "graduate"]

unifac = ["lectur", "prof.", "professor", "professeur", "profesor", "research chair", "dean", "faculty", "distinguished chair", "post doc", "post-doc", "post–doc", "postdoc", "research fellow", "researcher", "scientist"]

othersci = ["technician", "academic", "research ass", "research scientist", "lab manager", "oceanographer", "chemist", "ologist", "icist", "ician", "scientist", "scholar", "otanist", "atrist"]

eduout = ["museum", "museo", "musee", "curator", "smithsonian", "educator", "teacher", "classrooms", "science class", "librarian", "archivist", "outreach", "education", "teach"]

applied = ["foundation", "society", "non-governmental", "nongovernmental", "non governmental", "non–governmental", "organisation", "organization", "nonprofit", "non-profit", "non–profit", "philantropy", "stewardship", "policy officer", "capacity development", "international development", "intergorvenmental", "nonpartisan", "non-partisan", "non–partisan", "non partisan", "community organisation", "community organization", "think tank", "think-tank", "thinktank", "think–tank"]

otherprof = ["recruiter", "entrepreneur", "manager", "marketer", "designer", "programmer", "coder", "self-employ", "self employ", "marketing", "strategist", "operator", "consultant", "investor", "engineer", "architect", "doctor", "nurse", "developer", "programming", "coding", "devops", "trader", "consultant", "lawyer", "business owner"]

media = ["writer", "journalis", "blog", "screenwriter", "publisher", "corresponden", "comms", "communicator", "scicomm", "author", "producer", "production", "audio", "radio", "podcast", "documentar", "film", "photographer", "report", "show", "movie", "copyeditor", "copy editor", "copy-editor", "copy–editor", "broadcast", "television", "communicatio", "freelance", "videograph", "editor", "foto", "publish", "media guy", "newspaper", "youtuber", "influencer"]

dm = ["public servant", "government agency", "eu commission", "eucommission", "congressional", "congressman", "congresswoman", "senator", "senate", "parliament", "municipal", "labour candicate", "independent candidate", "legislator", "european commission"]

value = value.lower()

if any(x in value for x in students):
    return ""
if any(x in value for x in graduated):
    return ""
elif any(x in value for x in unifac):
    return ""
elif any(x in value for x in othersci):
    return ""
elif any(x in value for x in eduout):
    return ""
elif any(x in value for x in applied):
    return ""
elif any(x in value for x in otherprof):
    return ""
elif any(x in value for x in media):
    return ""
elif any(x in value for x in dm):
    return ""
else:
    return "General public"

# Unknown

unknown = ""

if value in unknown:
    return "Unknown"
else:
    return "no match"