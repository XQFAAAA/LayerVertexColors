# Layer Vertex Colors

中文 | [English](README_en.md)

Blender 分层顶点色管理插件，提供类似于材质的顶点色槽位系统。

## 功能

- **颜色球系统** — 全局颜色球跨物体共享，修改一处即时同步所有引用
- **槽位管理** — 每个物体拥有独立的颜色槽位列表，可添加、删除、排序
- **面指定** — 编辑模式下将选中面分配到指定槽位，支持选择/弃选
- **批量设置** — 按材质、按松散块一键创建槽位并指定面
- **顶点色预览** — 一键切换视口顶点色显示/隐藏
- **数据重建** — 合并物体后从网格属性恢复槽位数据
- **多语言** — 中文/英文自动切换，跟随 Blender 界面语言

## 安装

1. 将 `LayerVertexColors` 文件夹放入 Blender 的 `scripts/addons` 目录
2. 在 Blender 偏好设置中启用 **Layer Vertex Colors**

## 使用

1. 在 3D 视图侧栏找到 **LVC** 面板
2. 点击 `+` 添加颜色槽位
3. 进入编辑模式，选中面后点击 **Assign** 指定颜色
4. 点击色块修改颜色球颜色，所有引用该球的面自动更新

## 属性说明

| 网格属性 | 类型 | 用途 |
|---|---|---|
| `layer_vertex_slot` | INT (CORNER) | 面拐所属槽位索引 |
| `layer_vertex_color` | BYTE_COLOR (CORNER) | 面拐颜色 |
| `layer_vertex_hash` | STRING (CORNER) | 面拐关联的颜色球哈希 |

## 兼容性

- Blender 4.5+
