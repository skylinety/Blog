# NAS 系统选择

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [NAS 系统选择](#nas-系统选择)
  - [NAS 简介](#nas-简介)
  - [FreeNAS](#freenas)
    - [简介](#简介)
    - [ECC](#ecc)
  - [黑群晖](#黑群晖)
  - [汇总比较](#汇总比较)

<!-- /code_chunk_output -->

## NAS 简介

NAS 是 Network-Attached Storage 的缩写，即网路附加存储。

## FreeNAS

### 简介

FreeNAS 基于 FreeBSD 开发，主要运行在 x86-64 架构的计算上。
FreeNAS 12 之后改名为 TreeNAS，加入了 Linux 的版本

### ECC

FreeNAS 采用 ZFS(Zettabyte File System)文件系统，ZFS 很多设计依赖于 ECC。
需要专有主板（对服务器）与内存支持 ECC。
FreeNAS 推荐使用 ECC 内存（不是必须 ECC），但当在不支持 ECC 的平台跑 FreeNAS 时，数据的准确性无法保证。

## 黑群晖

## OMV

OpenMediaVault 的简写

## 汇总比较

| 系统    | 内核            | 硬件要求 | FS  |
| ------- | --------------- | -------- | --- |
| 黑群晖  | Linux           | 一般     |
| FreeNAS | FreeBSD         | 较高     | ZFS |
| OMV     | Linux（Debian） | 低       |
