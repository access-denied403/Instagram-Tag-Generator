tags = """
#coder #codergirl #coderlife #coderpower #coders #coderslife #coding 
#codingbootcamp #codingisfun #codinglife #codingpics #java #javascript 
#programing #programmer #programmerlife #programmerrepublic #programmers 
#programmerslife #programming #programminglife #computerscience 
#softwareengineering #developer #softwareengineer #pythonhub 
#datascience #machinelearning #artificialintelligenc #python3 
#coder #codergirl #coderlife #coderpower #coders #coderslife #coding 
#codingbootcamp #codingisfun #codinglife #codingpics #java #javascript 
#programing #programmer #programmerlife #programmerrepublic #programmers 
#programmerslife #programming #programminglife #computerscience 
#softwareengineering #developer #softwareengineer #pythonhub 
#datascience #machinelearning #artificialintelligenc #python3 
#coder #codergirl #coderlife #coderpower #coders #coderslife 
#coding #codingbootcamp #codingisfun #codinglife #codingpics #java 
#javascript #programacion #programing #programmer #programmerlife 
#programmerrepublic #programmers #programmerslife #programming 
#programminglife #computerscience #js #softwareengineering 
#informationtechnology #developer #softwareengineer #devgirls 
#code #motivation #developer #coding #balancedlife #100daysofdata #lifestyle 
#womenintech #softwaredeveloper #girlswhocode #mindset #100daysofcode 
#artificialintelligence #stemgirls #stemeducation #worklifebalance #womeninstem 
#deeplearning #mindfulness #peoplewhocode #balance #datascientist #neuralnetworks 
#datascience #workhardanywhere #codinglife #dataanalytics #machinelearning 
#programmersday #codingisfun #programmerrepublic #programmer #codingmemes #programming 
#creativecoding #predictiveprogramming #codinglife #codingbootcamp #programminglife 
#programmering #programmingisfun #programminghumor #codingforkids 
#pythonprogramming #computerprogramming #programmingjokes #programmers #programmerjokes 
#codingpics #codingdays #programmerslife #programmingmemes #programmerlife #python 
#coder #coderlife #coderpower #coders #coderslife #coding #codingbootcamp #coding #programacion 
#programing #programmer#programmerlife #programmerrepublic #programmers #programmerslife 
#programming #programminglife #computerscience #pythonprojects #python3 #pythoncode 
#machinelearning #pythonhub #artificialintelligence #informationtechnology #developer 
#softwareengineer #programmerhumor #cybersecurity #curious_programmer 
#coder #codergirl #coderlife #coderpower #coders #coderslife #coding #codingbootcamp #codingisfun 
#codinglife #codingpics #java #javascript #programacion #programing #programmer #programmerlife 
#programmerrepublic #programmers #programmerslife #programming #programminglife #computerscience 
#js #softwareengineering #informationtechnology #developer #softwareengineer #programmerhumor 
#programming #coding #programmer #developer #python #code #technology #coder #javascript #java 
#computerscience #tech #software #html #webdeveloper #webdevelopment #linux #css #codinglife 
#webdesign #hacking #php #development #softwaredeveloper #programmers #programmingmemes 
#programminglife #softwareengineer 
"""

class Tag_Generator(object):
    def __init__(self, tag_list):
        self.tag_list = tag_list

    def sort_function(self):
        sorted_list = []
        _split = self.tag_list.split("#")
        
        for item in _split:
            item = item.strip("\n").strip()
            if item not in sorted_list:
                sorted_list.append(item)
        sorted_list = sorted(sorted_list)
        return sorted_list


    def tag_generator(self):
        sorted_list = self.sort_function()
        generated_tags = []
        while len(generated_tags) < 30:
            tag = random.choice(sorted_list)
            tag = "#" + tag
            if tag not in generated_tags:
                generated_tags.append(tag)
        return generated_tags


    def __repr__(self):
        tags = self.tag_generator()
        list = ""
        for element in tags:
            list += f"{element} "
        return list


if __name__ == "__main__":
    import random

    tag = Tag_Generator(tags)
    print(tag)

    print(f"\nTotal tags: {len(tag.tag_list)}")
    print(f"Unique tags: {len(tag.sort_function())}")
    
