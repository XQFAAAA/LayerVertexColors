import bpy

# 英文 → 中文映射（仅维护一份，注册时自动扩展到多个上下文）
_zh_CN = {
    # Panel
    "Layer Vertex Colors": "分层顶点色",
    # Global ball operators
    "Add Color Ball": "添加颜色球",
    "Create a new global color ball": "创建一个新的全局颜色球",
    "Remove Color Ball": "删除颜色球",
    "Remove the selected global color ball, all slots referencing it will be cleared": "删除当前全局颜色球，所有引用该球的槽位将被清空",
    "Delete": "删除",
    "Delete this global color ball, all slots referencing it will be cleared": "删除该全局颜色球，所有引用该球的槽位将被清空",
    # Slot operators
    "Add Slot": "添加槽位",
    "Add an empty layer vertex color slot to the current object": "为当前物体添加一个空的分层顶点色槽位",
    "Remove Slot": "删除槽位",
    "Remove the current slot and clean up mesh data (higher indices auto-decrement)": "删除当前槽位并清理网格数据（高索引自动递减）",
    "Move Slot": "移动槽位",
    "Move the current slot position": "移动当前槽位的位置",
    "Cleanup Unused Colors": "清理未使用颜色",
    "Delete all unreferenced global color balls": "删除所有未被引用的全局颜色球",
    "Rebuild Slot Data": "重建槽位数据",
    "Rebuild object slot list from mesh layer_vertex_slot attribute": "从网格 layer_vertex_slot 属性重建物体的槽位列表",
    "Add from Active Vertex Group": "从活动顶点组添加",
    "Create a slot from the current active vertex group": "从当前活动的顶点组创建一个槽位",
    "Add from Active Material": "从活动材质添加",
    "Create a slot from the current active material and assign corresponding faces": "从当前活动的材质创建槽位并指定对应面",
    "Set by Material": "按材质设置",
    "Create slots by material and assign faces, clear existing slots": "按材质创建槽位并指定面，清空已有槽位",
    "Set by Loose Parts": "按松散块设置",
    "Create slots by mesh loose parts and assign faces, clear existing slots": "按网格松散块创建槽位并指定面，清空已有槽位",
    "Remove All Colors": "删除所有颜色",
    "Remove all layer vertex color slots and corner data from the current object": "删除当前物体全部分层顶点色槽位和面拐数据",
    # Utility menu
    "Utility Menu": "展开功能",
    # Ball pick/new/clear
    "Pick Color Ball": "选择颜色球",
    "Switch the associated global color ball for the current slot": "为当前槽位切换关联的全局颜色球",
    "Select": "选择",
    "Associate the selected slot with this color ball": "将所选槽位关联到此颜色球",
    "New Color Ball": "新建颜色球",
    "Create a new global color ball and associate it with the specified slot": "新建全局颜色球并关联到指定槽位",
    "New": "新建",
    "Detach": "断开",
    "Detach the current slot from its color ball association": "断开当前槽位的颜色球关联",
    # Face operators
    "Assign": "指定",
    "Assign all corners of selected faces to the current slot": "将选中面的所有面拐分配到当前槽位",
    "Remove": "移除",
    "Reset all corners of selected faces to unassigned": "将选中面的所有面拐恢复为未分配状态",
    "Select Faces": "选择",
    "Select all faces belonging to the current slot": "选择属于当前槽位的所有面",
    "Deselect Faces": "弃选",
    "Deselect all faces belonging to the current slot": "取消选择属于当前槽位的所有面",
    # Toggle view
    "Toggle Vertex Color View": "显示/隐藏顶点色",
    "Toggle show/hide layer_vertex_color vertex colors in viewport": "在视口中切换显示/隐藏 layer_vertex_color 顶点色",
    # UI draw() 硬编码文字
    "No active mesh object": "当前无活动物体",
    "Slot conflict detected, click to rebuild": "槽位存在冲突，点击重建",
    # Property name/description
    "Hash Value": "哈希值",
    "Unique identifier": "唯一标识符",
    "Color": "颜色",
    "Ball Hash": "球哈希",
    "Hash of the associated global color ball": "关联到的全局颜色球哈希值",
    "Limit": "数量限制",
    "Maximum number of loose parts, excess will be merged into the last slot": "最大松散块数量，超出部分合并到最后一个槽位",
}


def _build_translation_dict():
    """将扁平映射扩展为 Blender 要求的 (context, text) → translation 格式，
    同时注册 "*" 和 "Operator" 两个上下文以确保 operator 的 bl_label/bl_description 也能被翻译。
    同时注册 zh_CN 和 zh_HANS 以兼容不同 Blender 版本。"""
    result = {}
    for lang_code in ("zh_CN", "zh_HANS"):
        zh = {}
        for src, trans in _zh_CN.items():
            zh[("*", src)] = trans         # 通配上下文：Property name、draw() 文字等
            zh[("Operator", src)] = trans  # Operator 上下文：bl_label、bl_description
        result[lang_code] = zh
    return result


translation_dict = _build_translation_dict()


def register():
    bpy.app.translations.register(__name__, translation_dict)


def unregister():
    bpy.app.translations.unregister(__name__)
