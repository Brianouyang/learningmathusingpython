import requests
import json
s = input("请输入av号： ")
target_main_replies='https://api.bilibili.com/x/v2/reply?callback=jQuery&jsonp=jsonp&pn=replace2&type=1&oid=replace1&sort=2' # 获取主评论json的url
target_sub_replies = 'https://api.bilibili.com/x/v2/reply/reply?callback=jQuery&jsonp=jsonp&pn=replace1&type=1&oid=replace2&ps=10&root=replace3' # 获取回复评论json的url
headers = {'Referer':'https://www.bilibili.com','User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
target_for_main_replies = target_main_replies.replace('replace1', s).replace('replace2', '1')
req_main = requests.get(url=target_for_main_replies, headers=headers)
i = req_main.text.find('(') + 1 # 找到第一个括号的位置，+1之后就是大括号的位置
bf = req_main.text[i:-1] # 包含了第一个大括号和最后一个大括号里面的内容
req_main.encoding = 'utf-8' 
hot = json.loads(bf) # 转换成json
num = hot['data']['page']['count'] #获取评论的数目
file = input("输入文件的名字: ")
file = file + str('.txt') # 输出txt文件
with open(file, 'w', encoding='UTF-8') as f:
    for j in range(1, int(num/20+2)): # 遍历所有页数
        target1 = target_main_replies.replace('replace1', s).replace('replace2',str(j))
        req_main = requests.get(url=target1, headers=headers)
        i = req_main.text.find('(') + 1
        bf = req_main.text[i:-1]
        req_main.encoding = 'utf-8'
        hot = json.loads(bf)
        for each in hot['data']['replies']:
            f.write("{}: \n{}\n\n".format(each['member']['uname'] ,each['content']['message'])) # 打印其中的信息
            if each['replies'] is not None: # 如果有回复评论（副评论）
                f.write("\n{}\n\n".format(each['rcount']))
                if each['rcount'] > 3: # 如果回复评论大于3个就要展开 
                    for subeach in each['replies']:
                        root = subeach['root'] # 获得根的id（用于获得扩展的回复评论）
                    target_sub = target_sub_replies.replace('replace1', '1').replace('replace2', s).replace('replace3', str(root))
                    req2 = requests.get(url=target_sub, headers=headers)
                    i2=req2.text.find('(')+1
                    bf2=req2.text[i2:-1]
                    req2.encoding='utf-8'
                    hot2=json.loads(bf2)
                    num2=hot2['data']['page']['count']
                    for k in range(1, int(num2/10+2)): # 遍历所有回复评论的页数
		                    target_sub = target_sub_replies.replace('replace1', str(k)).replace('replace2', s).replace('replace3', str(root))
                    req2 = requests.get(url=target_sub, headers=headers)
                    i2 = req2.text.find('(')+1
                    bf2 = req2.text[i2:-1]
                    req2.encoding='utf-8'
                    hot2 = json.loads(bf2)
                    if hot2['data']['replies'] is not None:
                            for reply in hot2['data']['replies']: 
                                f.write("回复：\n{}： \n{}\n\n".format(reply['member']['uname'], reply['content']['message'])) # 打印其中的信息
                elif each['rcount'] > 0 and each['rcount'] <= 3: # 当回复评论数量大于0，小于等于3个时，就不需要通过获取回复评论的json来打印其中信息（也就是说其信息已经包含在主评论json里）
                    for subeach2 in each['replies']:
                        f.write("回复：\n{}： \n{}\n\n".format(subeach2['member']['uname'], subeach2['content']['message'])) # 打印其中的信息
				# 考虑置顶情况
        if j == int(num/20+1): # 经发现， 置顶评论会出现在每一页的主评论json里，所以就索性使用最后一页的置顶评论了
            if hot['data']['upper']['top'] is not None: # 如果有置顶评论才继续下边的操作
                f.write("{}\n".format(hot['data']['upper']['top']['content']['message'])) # 还不清楚置顶的主评论有没有多于一个的情况，知道的小朋友可以comment一下，，我这里直接按照单个置顶评论处理
                f.write("\n{}\n\n".format(hot['data']['upper']['top']['rcount']))
                if hot['data']['upper']['top']['rcount'] > 3: # 同样，置顶评论是会展开的
                    for top_replies in hot['data']['upper']['top']['replies']:
                        root = top_replies['root']
                    target_sub = target_sub_replies.replace('replace1', '1').replace('replace2', s).replace('replace3', str(root))
                    req2 = requests.get(url=target_sub, headers=headers)
                    i2=req2.text.find('(')+1
                    bf2=req2.text[i2:-1]
                    req2.encoding='utf-8'
                    hot2=json.loads(bf2)
                    num2=hot2['data']['page']['count']
                    for k in range(1, int(num2/10+2)):
                            target_sub = target_sub_replies.replace('replace1', str(k)).replace('replace2', s).replace('replace3', str(root))
                            req2 = requests.get(url=target_sub, headers=headers)
                            i2=req2.text.find('(')+1
                            bf2=req2.text[i2:-1]
                            req2.encoding='utf-8'
                            hot2=json.loads(bf2)
                            for reply in hot2['data']['replies']:
                                f.write("回复：\n{}： \n{}\n\n".format(reply['member']['uname'], reply['content']['message']))
                elif top_replies['rcount'] > 0 and top_replies['rcount'] <= 3:
                    for subeach2 in top_replies['replies']:
                        f.write("回复：\n{}： \n{}\n\n".format(subeach2['member']['uname'], subeach2['content']['message']))