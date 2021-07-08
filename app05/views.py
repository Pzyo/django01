from django.shortcuts import render

# Create your views here.

def ab_form(request):
    back_dic = {'username':'','password':''}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if '金瓶梅' in username:
            back_dic['username'] = '不符合社会主义核心价值观'
        if len(password) < 3:
            back_dic['password'] = '不能少于3位'

        """
        无论是post请求还是get请求
        页面都能获取到字典 只不过get请求请求来的时候是空值
        只是post请求可能会有值
        """
    return render(request,'app05/ab_form.html', locals())


from django import forms

class MyForm(forms.Form):
    # username字符串类型最小三位, 最大8位
    username = forms.CharField(min_length=3, max_length=8)
    # password字符串类型最小三位, 最大8位
    password = forms.CharField(min_length=3, max_length=8)
    # email字段必须符合邮箱格式  xxx@xx.com
    email = forms.EmailField()



