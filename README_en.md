# Layer Vertex Colors

[中文](README.md) | English

The Blender layered vertex color management plug-in provides a vertex color slot system similar to materials.

## Features

- **Color Ball System** — Global color balls shared across objects, instant sync on change
- **Slot Management** — Each object has its own color slot list, add, remove, reorder
- **Face Assignment** — Assign selected faces to a slot in edit mode, with select/deselect support
- **Batch Setup** — Create slots and assign faces by material or by loose parts in one click
- **Vertex Color Preview** — Toggle vertex color display in viewport
- **Data Rebuild** — Recover slot data from mesh attributes after joining objects
- **Multilingual** — Auto-switch between Chinese and English, following Blender interface language

## Installation

1. Copy the `LayerVertexColors` folder into Blender's `scripts/addons` directory
2. Enable **Layer Vertex Colors** in Blender Preferences

## Usage

1. Find the **LVC** panel in the 3D viewport sidebar
2. Click `+` to add a color slot
3. Enter edit mode, select faces, then click **Assign** to apply color
4. Click the color swatch to edit the color ball — all faces referencing it update automatically

## Mesh Attributes

| Attribute | Type | Purpose |
|---|---|---|
| `layer_vertex_slot` | INT (CORNER) | Slot index of the corner |
| `layer_vertex_color` | BYTE_COLOR (CORNER) | Corner color |
| `layer_vertex_hash` | STRING (CORNER) | Hash of the associated color ball |

## Compatibility

- Blender 4.5+
