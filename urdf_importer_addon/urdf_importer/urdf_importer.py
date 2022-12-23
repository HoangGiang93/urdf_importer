#!/usr/bin/python3

import bpy
from bpy_extras.io_utils import ImportHelper

from .robot_builder import RobotBuilder


def read_data(filepath, should_remove_identical_materials, should_rename_materials):
    RobotBuilder(filepath, should_remove_identical_materials, should_rename_materials)

    return {'FINISHED'}


class URDFImporter(bpy.types.Operator, ImportHelper):
    """Load a URDF file"""
    bl_idname = "import_scene.urdf"
    bl_label = "Import URDF"

    should_remove_identical_materials: bpy.props.BoolProperty(name="Remove identical materials", default=True)
    should_rename_materials: bpy.props.BoolProperty(name="Rename materials", default=True)

    # ImportHelper mixin class uses this
    filename_ext = ".urdf"

    def execute(self, _):
        return read_data(self.filepath, self.should_remove_identical_materials, self.should_rename_materials)
