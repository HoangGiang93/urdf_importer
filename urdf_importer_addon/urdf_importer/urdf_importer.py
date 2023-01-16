#!/usr/bin/python3

import bpy
from bpy_extras.io_utils import ImportHelper

from .robot_builder import RobotBuilder


def read_data(filepath, merge_same_name_materials, merge_duplicate_materials, rename_materials, apply_weld):
    RobotBuilder(filepath, merge_same_name_materials, merge_duplicate_materials, rename_materials, apply_weld)

    return {'FINISHED'}


class URDFImporter(bpy.types.Operator, ImportHelper):
    """Load a URDF file"""
    bl_idname = "import_scene.urdf"
    bl_label = "Import URDF"

    merge_same_name_materials: bpy.props.BoolProperty(name="Merge same name materials", default=True)
    merge_duplicate_materials: bpy.props.BoolProperty(name="Merge duplicate materials", default=True)
    rename_materials: bpy.props.BoolProperty(name="Rename materials", default=True)
    apply_weld: bpy.props.BoolProperty(name="Apply weld modifier", default=True)

    # ImportHelper mixin class uses this
    filename_ext = ".urdf"

    def execute(self, _):
        return read_data(self.filepath, self.merge_same_name_materials, self.merge_duplicate_materials, self.rename_materials, self.apply_weld)
