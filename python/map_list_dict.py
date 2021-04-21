# https://youtu.be/16M9kDdi0sQ
def map_list_dict(itr,fn):
    return dict(zip(itr,map(fn,itr)))

print(map_list_dict([1,2,3,4,5],lambda x:x*x))
