import os
#Each website is a new project


#create project diectory
def create_project(directory):
    if not os.path.exists(directory):
        print("Creating project "+directory)
        os.makedirs(directory)


def create_files(projectname,base_url):
    queue = projectname+'/queue.txt'
    crawled = projectname + '/clrawled.txt'

    if not os.path.isfile(queue):
        write_file(queue,base_url)
    if not os.path.isfile(crawled):
        write_file(crawled,'')
#create new file
def write_file(path,data):
    fobj = open(path,'w')
    fobj.write(data)
    fobj.close()

#add data to file
def add_to_file(path,data):
    with open(path,'a') as file:
        file.write(data,'\n')


#override file
def delete_content(path):
    with open(path,'a') :
        pass


#to make a set for storing unique urls
def read_from_file(filename,'rt'):

    results = set()
    with open(filename,'rt') as file:
        for line in file:
            results.add(line.replace("\n"," "))
    return results

#to store urls in file

def set_to_file(links, file_name):
    delete_content(file_name)
    for links in sorted(links):
        add_to_file(file_name,links)


create_project("github_crawl")
create_files("github_crawl","https://github.com/search?utf8=%E2%9C%93&q=django&type=")