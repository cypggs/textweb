# textweb

> 本网站完全由chatgpt生成，主要使用GPT4
>
> 功能是一个简易版本的记事本编辑器，方便临时记录一些东西，在多个设备切换
>
> 架构：[Flask](https://flask.palletsprojects.com/) + [SQLite](https://www.sqlite.org/)



## Install <a name="install"></a>

Use docker 

```sh
docker run -dit --name textweb -p 80:88 --network my_network --restart always -v /home/opc/textweb/contents.db:/app/contents.db cypggs/textweb
```

访问 http://127.0.0.1:80  



## Build <a name="build"></a>

Build

```sh
git clone https://github.com/cypggs/textweb.git
cd textweb
sh cd.sh
```