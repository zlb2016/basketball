import os
def sortss(lists):
    j = 0
    while j < len(lists)-1:
        i = 0
        while i < len(lists)-(j+1):
            if lists[i] > lists[i+1]:
                a = lists[i]
                lists[i] = lists[i+1]
                lists[i+1] = a
            i += 1
        j += 1
    return lists
if __name__ == '__main__':
    rgb_list=[]
    depth_list=[]
    for rgb_name in os.listdir(r"./pictures/63_rgb"):
        new_file_name = rgb_name.split(".png")[0].split("_")[1]
        rgb_list.append(new_file_name)
    for rdepth_name in os.listdir(r"./pictures/63_depth"):
        rdepth=rdepth_name.split(".png")[0].split("-")[1]
        depth_list.append(rdepth)
    print(rgb_list)
    print('sort',sortss(rgb_list))
    print(sortss(depth_list))