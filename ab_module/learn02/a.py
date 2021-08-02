

# 功能
def tell_stu_info(stu_obj):
    print('名字: %s 年龄: %s 性别: %s'%(
        stu_obj['stu_name'],
        stu_obj['stu_age'],
        stu_obj['stu_gender']
    ))

def set_stu_info(stu_obj, x, y, z):
    stu_obj['stu_name'] = x
    stu_obj['stu_age'] = y
    stu_obj['stu_gender'] = z

stu_obj = {
    'stu_name': 'pzyo',
    'stu_age': 23,
    'stu_gender': 'male',
    'tell_stu_info': tell_stu_info,
    'set_stu_info': set_stu_info
}

stu1_obj = {
    'stu_name': 'pzyo',
    'stu_age': 23,
    'stu_gender': 'male',
    'tell_stu_info': tell_stu_info,
    'set_stu_info': set_stu_info
}