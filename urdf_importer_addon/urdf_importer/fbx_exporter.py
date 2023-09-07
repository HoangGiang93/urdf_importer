#!/usr/bin/python3

from bpy_extras.io_utils import ExportHelper
import bpy

from .robot_builder import TMP_TEXTURE_PATH
from shutil import copytree

from os import path


def write_data(filepath):
    bpy.ops.export_scene.fbx(filepath=filepath, object_types={"ARMATURE", "MESH"}, mesh_smooth_type="FACE", add_leaf_bones=False)
    if path.exists(TMP_TEXTURE_PATH):
        copytree(TMP_TEXTURE_PATH, path.dirname(filepath) + "/" + TMP_TEXTURE_PATH, dirs_exist_ok=True)
    return {"FINISHED"}


class FBXExporter(bpy.types.Operator, ExportHelper):
    """Write a FBX file with textures"""

    bl_idname = "export_scene.fbx_with_textures"
    bl_label = "Export FBX with textures"

    # ExportHelper mixin class uses this
    filename_ext = ".fbx"

    def execute(self, _):
        return write_data(self.filepath)
