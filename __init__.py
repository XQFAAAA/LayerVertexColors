# type: ignore
bl_info = {
    "name": "Layer Vertex Colors",
    "author": "xqfa",
    "description": "Layered vertex color management tool — independent color slot system",
    "blender": (4, 5, 0),
    "version": (1, 0, 0),
    "location": "View3D > Sidebar > LVC",
    "warning": "",
    "category": "Mesh",
}

from . import translations, layer_vertex_colors


def register():
    translations.register()
    layer_vertex_colors.register()


def unregister():
    layer_vertex_colors.unregister()
    translations.unregister()
