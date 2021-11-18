# NAS 系统选择

## 简介

NAS 是 Network-Attached Storage 的缩写，即网路附加存储。

## freeNAS

### 简介

FreeNAS 基于 FreeBSD 开发，主要运行在 x86-64 架构的计算上

### ECC

freeNAS 采用 ZFS(Zettabyte File System)文件系统，ZFS 很多设计依赖于 ECC。
需要专有主板（对服务器）与内存支持 ECC。
freeNAS 推荐使用 ECC 内存（不是必须 ECC），但当在不支持 ECC 的平台跑 freeNAS 时，数据的准确性无法保证。
