import glob


print glob.glob(".*")


for header_filename in glob.glob("*.h"):
    print header_filename
    header_file = open(header_filename,'r+')


