# Beacon-Flask

![](https://img.shields.io/badge/Python-3.6.0-blue.svg)
![](https://img.shields.io/badge/Flask-0.12.2-blue.svg)
![](https://img.shields.io/badge/license-GPL-blue.svg)

![](http://ofsabm6nw.bkt.clouddn.com/3.jpg)

## 简介

**Echo** 团队为 **[Beacon](https://github.com/SeaHub/Beacon)** 后端 API 实现代码。

## 工程结构

* _config.yml
* app：主目录
* config.py：配置文件
* data.db：数据库文件
* manage.py：flask-script 
* migrations：数据库迁移目录
* requirements.txt：Pypi 包配置
* venv：virtualenv 环境

## 部署方式

1. `clone` 项目

```bash
$ git clone git@github.com:Desgard/Beacon-Flask.git
```

2. 根据 `requirements.txt` 配置 Pypi 环境

```bash
$ pip install -r requirements.txt
```

3. 使用 `manage.py` 启动 debug 模式下服务器

```bash
$ python manage.py runserver (--host xx.xx.xx.xx)
```

## API 文档

详见 [wiki](https://github.com/Desgard/Beacon-Flask/wiki)。文档中描述的接口是部署在 `heroku` 上的，但是由于其数据库未迁移至 postgresql 所以其返回结果仅供测试使用。而 `server` 分支的服务端是部署在个人服务器上的，不宜公开。

## GNU General Public License v3.0

Permissions of this strong copyleft license are conditioned on making available complete source code of licensed works and modifications, which include larger works using a licensed work, under the same license. Copyright and license notices must be preserved. Contributors provide an express grant of patent rights.
