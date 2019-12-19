num_str = input("Please input function number:")
#Check if input is a number.
if not num_str.isdigit():
	print("Invalid input! The function number must be a number.")
else:
	num = int(num_str)

#在接收raw_input方法后，判断接收到的字符串是否为数字

#例如：

str = raw_input("please input the number:")

if str.isdigit():

#为True表示输入的所有字符都是数字，否则，不是全部为数字

#str为字符串
str.isalnum() #所有字符都是数字或者字母
str.isalpha() #所有字符都是字母
str.isdigit() #所有字符都是数字
str.islower() #所有字符都是小写
str.isupper() #所有字符都是大写
str.istitle() #所有单词都是首字母大写，像标题
str.isspace() #所有字符都是空白字符、\t、\n、\r

 
'''
上述的主要是针对整型的数字，但是对于浮点数来说就不适用了，那么浮点数怎么判断呢，一直在纠结这个问题，为什么非要区分整型和浮点数呢，既然都是参与运算的，全部适用浮点数不是一样吗，在得到结果后，直接转换为int型不是一样吗，为什么非要纠结在前期去判断是否整型或者浮点数呢，有了这样的思路，下面就好做了，例如：

我们可以通过异常来判断，异常语法如下：

try:
    {statements}
exception: {Exception Objects}
    {statements}
'''
str = raw_input("please input the number:")

try:
    f = float(str)
exception ValueError:
    print("输入的不是数字！")