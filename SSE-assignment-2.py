from git import Repo
import json

def printSeparator():
	print("")
	print("-------------------------------------------------")
	print("")

# setting up repo
repo = Repo("/mnt/d/hw/2020/s2/SSE/cordova-android")
assert not repo.bare
git = repo.git

# setting up constant variables
file_path = "./framework/src/org/apache/cordova/"
fix_commit = "af2969dec58ca89150b84b5d57edcf63d4ce1302"
file_name = "CordovaWebViewImpl.java" 

print("Part 3 info:")
print(git.diff(fix_commit, fix_commit + "^"))
printSeparator()
print(git.blame("-L 226,232", fix_commit, file_path + file_name))
printSeparator()
vcc_info = git.blame("-L 226,232", fix_commit + "^", file_path + file_name)
print(vcc_info)
printSeparator()

vcc = []
for line in vcc_info.splitlines():
	vcc_id = line.split(" ", 1)[0]
	if vcc_id not in vcc:
		vcc.append(vcc_id)




print("Part 5 info:")
for each_vcc in vcc:
	print(each_vcc)
	printSeparator()
	print(git.show("--stat", each_vcc))
	printSeparator()

	git_log = git.log(file_path + file_name)
	authors = {}
	for log_line in git_log.splitlines():
		log_info = log_line.split(" ", 1)
		if(log_info[0] == "Author:"):
			if(log_info[1] in authors):
				authors[log_info[1]] += 1
			else:
				authors[log_info[1]] = 1

	print("Commit(s) made per author:")
	print(json.dumps(authors, indent=1))

