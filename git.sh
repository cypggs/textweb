#保存密码
git config --global user.email "qcypggs@qq.com"
git config --global user.name "qcypggs"

#git config credential.helper store
git pull
git status
git add *
git rm `git status | grep deleted | awk '{print $2}'`
git rm `git status | grep 删除 | awk '{print $3}'`
git commit -m "$1"
git push
