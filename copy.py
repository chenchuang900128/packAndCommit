#!/usr/bin/python
#coding=utf-8  
import os;  
import shutil;
import time;
import sys 
reload(sys) # Python2.5 初始化后删除了 sys.setdefaultencoding 方法，我们需要重新载入 
sys.setdefaultencoding('utf-8') 

print('ThisISCmd%s',sys.argv[0])            

 
# ipa打包的目录
source_dir = '/Users/llbt/Desktop/MBSiPhone_1.9.5/build/ipa-build/';
# ipa文件放置的svn目录
target_dir =  '/Users/llbt/Desktop/公司svn/2018年%s月份上线功能计划/测试安装包/%s/' %(time.strftime("%m")[-1],time.strftime("%Y-%m-%d"));
# svn账号，密码
svnname = 'chenchuang'
svnpw = 'cc0819'


# 删除目标目录ipa文件
for root, dirs, files in os.walk(target_dir):
    for file in files:
        targetF = os.path.join(root,file);
        if (os.path.splitext(targetF)[1] == '.ipa' and "广东南粤银行" in targetF):
           os.remove(targetF)
           cmd = 'svn delete %s'%targetF
           print('\n执行删除命令：%s\n\n'%cmd)
           os.system(cmd)


# 目标目录不存在 创建目录
if os.path.exists(target_dir):	
	 pass
else:
  os.makedirs(target_dir)
  addCmd = 'svn add %s'%target_dir
  os.system(addCmd)           

# 遍历原目录，将文件拷贝到目标目录
for root, dirs, files in os.walk(source_dir):
    for file in files:
        sourceF = os.path.join(root,file);
        if os.path.isfile(sourceF):
           shutil.copy(sourceF,target_dir);
           addPath = target_dir + file
           addCmd = 'svn add %s'%addPath
           print('\n执行添加命令：%s\n\n'%addCmd)
           os.system(addCmd)
           
          

os.chdir(target_dir)
commitCmd = 'svn commit -m "%s" --username %s --password %s'%('ipa包上传',svnname,svnpw)
print('\n执行提交命令：%s\n\n'%commitCmd)
os.system(commitCmd)
  
# cp -r ~/Desktop/MBSiPhone_1.9.5/build/ipa-build/*  ~/Desktop/公司svn/2018年4月份上线功能计划/测试安装包/2018-04-03/
