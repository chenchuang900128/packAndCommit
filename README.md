# packAndCommit

首先打开python脚本copy.py，修改配置:

# ipa打包的目录
source_dir = '/Users/llbt/Desktop/MBSiPhone_1.9.5/build/ipa-build/';
# ipa文件放置的svn目录
target_dir =  '/Users/llbt/Desktop/公司svn/2018年%s月份上线功能计划/测试安装包/%s/' %(time.strftime("%m")[-1],time.strftime("%Y-%m-%d"));
# svn账号，密码
svnname = 'chenchuang'
svnpw = 'cc0819'


使用方法：在MAC上打开终端，输入一下命令

/Users/llbt/Movies/xcode_shell-master/ipa-build（你放在电脑上ipa-build文件路径） /Users/llbt/Desktop/我的的App（Xcode工程目录） AdHoc
