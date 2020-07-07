## 待更新

## 代理

寻找代理的网站 这上面比较可用https://www.kuaidaili.com/ops/

查询本机IP的网站 http://httpbin.org/ip

自定义设置代理

```
yum -y install squid # 安装服务
systemctl enable squid.service # 开机启动
vi /etc/squid/squid.conf

http_access allow !Safe_ports    #deny改成allow
http_access allow CONNECT !SSL_ports  #deny改成allow
http_access allow all  #deny改成allow

service squid start # 启动服务代理使用的端口是3128
```

